---
type: entity
created: 2026-07-07
updated: 2026-07-07
tags: [文件协议, HTTP, 跨平台, NAS]
aliases: [WebDAV, Web Distributed Authoring and Versioning]
---

# WebDAV

扩展 HTTP 协议支持文件操作（创建、删除、移动、复制、属性查询）的网络协议，适用于跨平台文件访问。

## 核心特征

- 基于 HTTP 协议扩展，新增 PUT、DELETE、MKCOL、COPY、MOVE、PROPFIND 等方法
- 穿透防火墙能力强（使用标准 HTTP 端口）
- macOS Finder、Linux davfs2、Rclone 等工具原生支持
- 本架构中以 Nginx ngx_http_dav_module 提供，监听 8081 端口

## 主要应用场景

- **macOS 客户端**：Finder 原生支持 WebDAV 挂载
- **跨平台文档协作**：Obsidian、Joplin 等笔记工具同步
- **云存储备份**：Rclone 通过 WebDAV 备份数据
- **企业 OA 附件存储**：HTTP 协议易于集成

## 与其他实体的关系

- **配合 [[entities/Nginx]]**：Nginx 的 DAV 模块 + auth_request 回调 authd 完成认证委托
- **依赖 [[entities/authd]]**：每次请求由 Nginx auth_request 子请求向 authd /internal/verify-password 验证凭据
- **依赖 [[entities/OpenLDAP]]**：最终认证指向 LDAP Bind
- **配合 Samba/NFS/HTTP API**：四种协议并行

## 优势与局限

**优势**：基于 HTTP，穿透防火墙能力强；macOS 和 Linux 原生支持；无需安装专用客户端。
**局限**：性能低于 SMB/NFS（HTTP 协议开销更大）；大目录 PROPFIND 延迟较高；标准 WebDAV 不支持追加写入。

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 7.4 节文件服务
