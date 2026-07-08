---
type: entity
created: 2026-07-07
updated: 2026-07-07
tags: [身份认证, 目录服务, LDAP, NAS]
aliases: [LDAP, OpenLDAP 1.5]
---

# OpenLDAP

开源 LDAP（Lightweight Directory Access Protocol）目录服务的事实标准实现。

## 核心特征

- 基于 X.500 树形结构组织数据，天然适合层级化的身份信息存储
- Schema 扩展机制：通过 LDIF 文件扩展 posixAccount、sambaSamAccount 等对象类，覆盖多种认证需求
- 内部使用 LMDB（Lightning Memory-Mapped Database）作为存储后端，高性能嵌入式键值数据库
- 被 Samba、NFS（libnss-ldap）、Linux PAM 等核心系统组件**原生支持**

## 主要应用场景

- **统一身份源**：作为全系统唯一的用户信息存储点，消除多账号同步问题
- **企业目录服务**：替代 Active Directory 的开源方案
- **NAS/存储平台**：同时为 HTTP、SMB、NFS、WebDAV 提供身份认证

## 与其他实体的关系

- **vs 关系数据库**：LDAP 是目录服务，专为读多写少、层级查询优化；关系数据库是通用数据存储。Samba ldapsam、NFS libnss-ldap 等系统组件原生支持 LDAP 而非关系数据库
- **配合 Samba**：通过 ldapsam 认证后端直接读取 NT Hash 进行 SMB 认证
- **配合 [[entities/authd]]**：authd 通过 go-ldap 客户端封装 LDAP 操作，对外提供业务级接口
- **配合 JWT**：LDAP Bind 完成初始认证，JWT 承载后续无状态会话

## 在本架构中的应用

NAS 智能存储平台以 osixia/openldap:1.5.0 容器镜像部署，扩展了 posixAccount、shadowAccount、sambaSamAccount 三套 Schema 及自定义 NFC 绑定条目（ou=nfc_bindings），实现了全协议统一身份认证。

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 5 章身份认证体系设计，第 4.3 节技术栈
