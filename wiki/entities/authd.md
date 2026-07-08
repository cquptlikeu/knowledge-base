---
type: entity
created: 2026-07-07
updated: 2026-07-07
tags: [NAS, 自研服务, 身份认证, Go]
aliases: [Authentication Daemon, 统一业务入口]
---

# authd

NAS 智能存储平台的自研核心服务（Authentication Daemon），是整个系统的统一业务入口。

## 核心特征

- 用 Go 1.25 + Gin v1.9 编写，单进程承载五大职责：身份认证、权限决策、文件服务、审计记录、系统管理
- 监听 8080 端口，接收所有来自 Web 管理台和移动 App 的 HTTP 请求
- 单二进制静态编译，无外部运行时依赖，内存占用数十 MB
- 所有经过 authd 的操作均被记入审计日志，不可绕过

## 主要应用场景

- **统一 HTTP API**：为 Web 管理台和移动 App 提供 RESTful 接口
- **JWT 认证**：签发 24h 有效期的 HS256 令牌，中间件层无状态验证
- **权限管理**：封装 setfacl/getfacl 调用，提供结构化权限管理接口
- **审计记录**：同步写入 certified_operations 表（22 字段完整上下文）
- **NFC 登录**：标签 UID 验证、绑定关系管理
- **mDNS 广播**：启动时向局域网广播 NAS 服务信息

## 与其他实体的关系

- **依赖 [[entities/OpenLDAP]]**：通过 go-ldap 客户端进行所有目录操作
- **依赖 [[entities/POSIX-ACL]]**：通过系统调用管理文件权限
- **配合 Samba/NFS/Nginx**：四项服务共享同一文件系统和权限体系
- **配合 [[entities/MCP]]**：为 Agent 的工具调用提供权限 Hook
- **内部模块**：ldap/client.go（LDAP 封装）、handler/permission.go（权限管理）、handler/nfc.go（NFC 认证）、certified_repo.go（审计日志）、proof_repo.go（哈希链）

## 单进程设计理由

NAS 设备通常由非专业运维管理：单进程比微服务集群更易排查、备份、迁移；认证/权限/文件操作在同一进程减少网络跳数；文件操作与审计日志在同一进程顺序完成，无分布式事务问题。

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 8 章自研核心服务设计
