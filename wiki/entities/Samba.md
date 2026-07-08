---
type: entity
created: 2026-07-07
updated: 2026-07-07
tags: [文件共享, SMB, CIFS, Linux, NAS]
aliases: [Samba, SMB, CIFS]
---

# Samba

Linux 上实现 SMB/CIFS 协议的开源套件，是 Windows 文件共享的标准解决方案。

## 核心特征

- 完整实现 SMB/CIFS 协议栈，Windows 客户端可像操作本地磁盘一样操作 NAS 文件
- **ldapsam 认证后端**：直接向 OpenLDAP 查询 sambaNTPassword 属性进行 NTLM 口令验证
- **遵从内核 ACL**：不引入独立权限逻辑，完全依赖 Linux 内核 POSIX ACL
- 监听 445 端口

## 主要应用场景

- **Windows 文件共享**：企业 Windows 工作站的 NAS 挂载
- **Office 文档在线编辑**：多用户协作编辑同一文件
- **Windows 备份目标**：系统备份到网络存储

## 与其他实体的关系

- **依赖 [[entities/OpenLDAP]]**：通过 ldapsam 读取 NT Hash 进行 NTLM Challenge-Response 认证
- **依赖 [[entities/POSIX-ACL]]**：文件访问权限完全由内核 ACL 控制
- **配合 NFS/Nginx/HTTP API**：四种协议并行，共享同一文件系统

## 优势与局限

**优势**：Windows 原生支持，用户体验最佳；与 LDAP 身份源直接集成；权限与其他协议完全统一。
**局限**：协议设计复杂，防火墙需开放 445 端口；macOS/Linux 兼容性相对较弱；旧版客户端需额外配置 SMB3 加密。

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 7.2 节文件服务
