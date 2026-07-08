---
type: entity
created: 2026-07-07
updated: 2026-07-07
tags: [文件系统, 网络协议, Linux, NAS]
aliases: [Network File System, NFS协议]
---

# NFS（Network File System）

Linux/Unix 原生的网络文件系统协议，通过 UID/GID 映射实现权限控制，以高性能、低延迟著称。

## 核心特征

- **内核级挂载**：通过 Linux 内核 NFS 模块实现，性能优于用户态文件服务
- **UID/GID 权限模型**：客户端和服务端以相同 UID 数值识别用户身份
- 监听 2049 端口（TCP/UDP）
- 通过 libnss-ldap 将用户名解析指向 LDAP，结合 Kerberos 强认证确保 UID 一致性

## 主要应用场景

- **Linux 服务器挂载**：高性能文件共享
- **CI/CD 构建系统**：构建产物存储
- **容器持久化存储**：Kubernetes NFS PV
- **视频监控写入**：大吞吐量的连续写入

## 与其他实体的关系

- **依赖 [[entities/OpenLDAP]]**：通过 libnss-ldap 解析 UID/GID，结合 Kerberos 强认证
- **依赖 [[entities/POSIX-ACL]]**：透明复用内核 ACL 权限
- **配合 Samba/Nginx/HTTP API**：四种协议并行

## 优势与局限

**优势**：内核级挂载，性能最优；无客户端软件依赖；适合高吞吐写入。
**局限**：跨互联网安全性低（通常限于局域网）；NFSv3 无内置加密，建议叠加 VPN 或 Kerberos；Windows 客户端 NFS 支持有限。

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 7.3 节文件服务
