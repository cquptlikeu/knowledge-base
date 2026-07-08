---
type: entity
created: 2026-07-07
updated: 2026-07-07
tags: [权限控制, 文件系统, Linux, NAS]
aliases: [POSIX ACL, 可访问控制列表, Access Control List]
---

# POSIX ACL

POSIX 标准的可扩展访问控制列表（Access Control List），是 Linux 文件系统对传统 Unix 三元权限（Owner/Group/Other）的扩展。

## 核心特征

- 支持为**任意具名用户或组**单独设置独立的读/写/执行权限（ACE，Access Control Entry）
- 通过 `setfacl` / `getfacl` 命令行工具管理
- 权限数据作为文件系统扩展属性（xattr）与文件数据不可分离
- **内核强制执行**：所有文件系统操作均经内核 ACL 子系统校验，应用层无法绕过

## 主要应用场景

- **跨协议统一权限**：在同一文件系统上通过 SMB/NFS/WebDAV/HTTP 访问时，权限结果完全一致
- **企业多人协作**：为不同用户/组精细化授权，突破传统 Unix 三元权限的局限
- **安全合规**：内核级强制访问控制（MAC），满足等保要求

## 与其他实体的关系

- **vs 传统 Unix 权限**：Unix 权限只有 Owner/Group/Other 三个主体，无法为特定用户单独授权。POSIX ACL 通过 ACE 扩展了任意数量具名用户的权限条目
- **配合 Samba**：Samba 直接遵从内核 ACL，不引入额外权限层——一次 setfacl 变更，SMB 客户端立即感知
- **配合 NFS**：通过 UID/GID 映射，NFS 客户端透明复用服务端 ACL 权限
- **配合 [[entities/authd]]**：authd 的 permission 模块封装 setfacl/getfacl 系统调用，提供 HTTP API 形式的权限管理接口

## 为什么是 POSIX ACL 而非自研权限表

自研权限表方案需要为每个协议实现权限同步逻辑，代码量大、可靠性低。POSIX ACL 由操作系统内核保证，引入代码量更少、可靠性更高、维护成本更低。

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 6 章权限控制体系，第 4.4 节
