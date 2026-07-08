---
type: summary
created: 2026-07-07
updated: 2026-07-07
tags: [NAS, 系统架构, 身份认证, 权限控制, 智能存储, 容器化]
source: "[[raw/definitely/NAS智能存储平台技术架构设计说明书]]"
---

# NAS 智能存储平台 — 技术架构设计说明书

一份面向企业与高价值家庭用户的下一代 NAS 平台架构设计文档（56 页，V1.1），核心主张：**以统一身份 + 统一权限为底座，以智能检索 + 可信存证为差异化能力**。

## 行业痛点

传统 NAS 产品存在六大共性问题：
- **权限割裂**：SMB、NFS、HTTP API 各自维护独立权限体系，变更需多处同步，极易漂移
- **身份孤岛**：用户账号散落各子系统，缺乏统一目录服务
- **智能能力缺失**：仅提供静态文件浏览，无法回答语义查询（如"我的合同里有哪些到期提醒"）
- **存证薄弱**：操作日志可被静默篡改，无法满足合规审计
- **移动体验差**：需手动填写 IP，无自动发现与近场免密登录
- **国产化适配不足**：缺乏国密算法与国产硬件安全模块扩展路径

## 架构核心：七大设计原则

| 原则     | 实现                               |
| ------ | -------------------------------- |
| 统一身份管理 | OpenLDAP 作为单一身份源，所有协议同库认证        |
| 统一权限管理 | POSIX ACL 作为单一权限源，跨协议透明复用        |
| 多协议兼容  | SMB / NFS / WebDAV / HTTP API 并存 |
| 智能扩展   | Agent + MCP + RAG 架构，可插拔 AI 能力   |
| 可信存储   | 哈希链审计日志，导出可独立验证的证明包              |
| 云边协同   | 本地完整运行，预留云端扩展接口                  |
| 国产化演进  | SM2/SM3/PUF 接口预留，逐步替换国际算法        |

## 七层架构

从下至上：硬件基础层 → 驱动层（Linux VFS/POSIX/ACL）→ 数据资源层（LDAP + 文件系统 + SQLite）→ 统一管理层（身份 + 权限 + 审计）→ 服务能力层（SMB/NFS/WebDAV/HTTP）→ 智能应用层（Agent + RAG）→ 用户与应用场景层。

> 关键洞察：统一管理层是整个平台的"控制面"——所有上层服务在执行任何操作前必须经过身份认证和权限校验。

## 统一身份源设计（Single Source of Truth）

以 OpenLDAP 为唯一用户信息源，通过扩展三套 Schema（posixAccount、shadowAccount、sambaSamAccount）同时覆盖 Linux 系统账号、密码策略、Windows NT Hash 三类需求。

**为什么选 LDAP 而非关系数据库？**
- Samba 的 `ldapsam` 认证后端、NFS 的 UID 映射（libnss-ldap）、Linux PAM 模块均**原生支持 LDAP**，不支持直接查关系数据库
- 若用 MySQL 存用户，必须在 Samba 与 NFS 之间单独维护账号同步逻辑，引入一致性风险

> "四条路径殊途同归，都指向同一个 OpenLDAP 目录"

多协议认证路径：
- HTTP API → authd → LDAP Bind（JWT 后续请求）
- SMB → Samba ldapsam → NTLM Challenge-Response
- NFS → 内核 libnss-ldap → UID 数值映射
- WebDAV → Nginx auth_request → authd → LDAP Bind
- NFC → authd → LDAP 绑定表查询

## 统一权限源设计（Single Permission Source）

以 **POSIX ACL** 为全系统唯一权限执行器。核心理由：Samba、NFS、VFS 层均**内核原生支持** POSIX ACL，无需任何桥接或转换层。一次 `setfacl` 变更立即对所有协议可见。

> "权限变更通过内核 ACL 生效，所有协议立即感知，无同步延迟，不会漂移"

权限结构：用户私有空间（`/data/<username>`，mode 700）+ 管理员特权 + 共享授权机制。

## 多协议文件服务

四种协议并行运行于同一文件系统之上：

| 协议 | 目标终端 | 认证方式 | 优势 | 局限 |
|------|---------|---------|------|------|
| SMB | Windows | NTLM（ldapsam → LDAP） | Windows 原生，体验最佳 | 跨互联网安全性低 |
| NFS | Linux/Unix | UID/GID + Kerberos | 内核级挂载，性能最优 | 跨互联网需 VPN |
| WebDAV | macOS/跨平台 | HTTP Basic → authd | 穿透防火墙强，无专用客户端 | 性能低于 SMB/NFS |
| HTTP API | 移动端/脚本 | JWT Bearer | JSON 接口，与审计深度集成 | 不适合 OS 级挂载 |

## 自研核心服务：authd

authd（Authentication Daemon）是整个系统的统一业务入口——一个 Go 进程内集中了身份认证、权限决策、文件服务、审计记录、系统管理五大职责。

**为什么不用微服务？** NAS 设备通常由非专业运维管理，单进程部署更易排查、备份、迁移；认证/权限/文件操作在同一进程减少网络跳数；文件操作与审计日志在同一进程内顺序完成，无分布式事务问题；内存占用可控制在数十 MB 级别。

## AI 智能服务体系

**核心架构：Agent + MCP + RAG**，将 NAS 文件系统转化为可语义检索的知识库。

**RAG 三层混合检索**（在成本与质量之间取得平衡）：
1. **Layer 1 — 元数据检索**（零 AI 成本）：文件名、路径、日期、类型等结构化属性精确匹配，覆盖绝大多数"找文件"需求
2. **Layer 2 — 内容混合检索**（低成本）：SQLite FTS5 全文检索 + bge-m3 语义向量检索，两路融合排序
3. **Layer 3 — VLM 按需处理**（高成本兜底）：仅在前两层无法满足时触发，处理图片/PDF 内容理解

**MCP 选择理由**：LLM 提供商无关（可切换 DeepSeek / Ollama / Claude 无需改工具代码）；Schema 约束减少模型格式错误；生态兼容。

> 关键安全设计：Agent 不自行维护权限逻辑，所有工具调用完全委托给 authd。Agent 用户在 NAS 上能做什么，Agent 就只能做什么，不多不少。

**Agent Loop**：「感知 → 规划 → 工具调用 → 观察 → 回答」循环，每次工具调用前经过 Permission Hook，最多 10 轮，写操作需二次确认。

## 可信存证体系

通过两张表实现不可篡改的操作记录：
- **certified_operations**（22 字段）：每次文件/身份操作的完整上下文
- **proof_records**（哈希链）：每节点 hash 依赖前一节点，形成因果锁链。篡改任一条记录会导致其后所有节点哈希失效

> "即使数据库管理员也无法静默修改历史记录而不留痕迹"

支持导出标准 JSON 格式存证包，第三方可独立验证，满足 ISO 27001 / 等保 2.0 合规要求。

## 移动接入：三级连接回退 + NFC 碰一碰

移动端设计目标：**零配置、零输入**。

**三级回退机制**：WiFi P2P 直连（无 AP 环境）→ mDNS 自动发现（99% 场景）→ 缓存 IP 验证（兜底）

**NFC 碰一碰登录**：标签只存 UID，不存任何凭据。绑定关系以 ANDROID_ID + 标签 UID 双重验证，防标签复制攻击。

## 容器化部署

Docker Compose 四容器架构：openldap → ldap-init（一次性） → nas 主容器（authd + Samba + NFS + Nginx）。采用 `network_mode: host` 以支持 SMB 广播/多播和 NFS RPC 端口映射。

## 安全纵深防御

四层防御：身份安全（SSHA/NT Hash 存储、LDAP Bind 认证）→ 访问控制（JWT HS256 24h、角色守卫、接口隔离、路径穿越防护）→ 数据安全（POSIX ACL 内核强制、目录 mode 700、SHA-256 内容哈希）→ 审计安全（哈希链不可篡改、设备溯源）。

## 国产化演进路径

| 方向 | 当前 | 目标 |
|------|------|------|
| 哈希算法 | SHA-256 | SM3 |
| 签名算法 | 设备 ID | SM2 + PUF 硬件 |
| 硬件安全 | 软件模拟 | CCM3302 PUF 芯片 |
| 加密算法 | AES（规划中） | SM4 |

架构已预留可插拔算法接口，国密替换不影响上层业务逻辑。

## 关键架构决策（ADR 摘录）

- **ADR-001**：LDAP 作为唯一身份源 — Samba ldapsam 原生支持，消除多账号同步
- **ADR-002**：POSIX ACL 作为权限真相 — 内核强制执行，跨协议零漂移
- **ADR-003**：文件 API 独立于 WebDAV — HTTP API 需要细粒度权限与审计
- **ADR-006**：PUF 存证采用哈希链+签名分离 — 签名可独立升级，哈希链不依赖签名即可验证

## 技术栈一览

- **后端**：Go 1.25 + Gin v1.9（单二进制静态编译，高并发低开销）
- **身份**：OpenLDAP 1.5 + JWT HS256
- **文件服务**：Samba 4.x + NFS（内核）+ Nginx WebDAV
- **数据**：SQLite（modernc 纯 Go）+ LDAP（LMDB）
- **前端**：Next.js 16 + React 19 + TypeScript 5.5 + shadcn/ui + Tailwind CSS 4
- **移动端**：React Native 0.85 + Kotlin 原生模块（NFC/WiFi P2P）
- **AI**：MCP 协议 + RAG 三层混合检索 + bge-m3 + VLM
- **部署**：Docker + Docker Compose（host 网络模式）

## 相关实体与概念

**实体**：[[entities/OpenLDAP]]、[[entities/POSIX-ACL]]、[[entities/Docker]]、[[entities/Go]]、[[entities/Gin]]、[[entities/Samba]]、[[entities/NFS]]、[[entities/WebDAV]]、[[entities/JWT]]、[[entities/SQLite]]、[[entities/MCP]]、[[entities/RAG]]、[[entities/Next.js]]、[[entities/React-Native]]、[[entities/NFC]]、[[entities/PUF]]、[[entities/SHA-256]]、[[entities/Nginx]]、[[entities/mDNS]]、[[entities/authd]]

**概念**：[[concepts/统一身份源]]、[[concepts/统一权限源]]、[[concepts/哈希链可信存证]]、[[concepts/多协议融合]]、[[concepts/Agent-Loop]]、[[concepts/RAG-三层混合检索]]、[[concepts/纵深防御]]、[[concepts/容器化部署]]、[[concepts/三级连接回退]]、[[concepts/国产化演进]]

**对比**：[[comparisons/LDAP-vs-关系数据库]]、[[comparisons/四种文件协议对比]]、[[comparisons/POSIX-ACL-vs-Unix权限]]
