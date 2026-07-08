---
type: entity
created: 2026-07-07
updated: 2026-07-07
tags: [Web服务器, 反向代理, WebDAV, HTTP]
aliases: [Nginx]
---

# Nginx

高性能 HTTP 服务器与反向代理，在本架构中承担 WebDAV 文件服务角色。

## 核心特征

- 高性能事件驱动架构，资源消耗低
- **ngx_http_dav_module**：提供 WebDAV 协议支持
- **auth_request 指令**：将每次请求的身份认证委托给 authd 的内部接口
- 监听 8081 端口

## 主要应用场景

- **WebDAV 文件访问**：macOS / Linux / 跨平台工具的文件挂载
- **认证委托**：Nginx 接收到 WebDAV 请求后，先向 authd /internal/verify-password 发起子请求验证凭据，通过后才放行

## 与其他实体的关系

- **依赖 [[entities/authd]]**：通过 auth_request 回调完成 HTTP Basic Auth 验证
- **依赖 [[entities/OpenLDAP]]**：最终认证链路为 Nginx → authd → LDAP Bind
- **配合 Samba/NFS/HTTP API**：四种协议并行，共享同一文件系统

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 7.4 节 WebDAV
