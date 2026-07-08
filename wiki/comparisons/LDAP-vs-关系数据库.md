---
type: comparison
created: 2026-07-07
updated: 2026-07-07
tags: [身份认证, 数据库, 架构决策, NAS]
---

# LDAP vs 关系数据库（作为身份源）

## 对比维度

| 维度 | LDAP | 关系数据库（MySQL/PG） |
|------|------|----------------------|
| 数据模型 | 树形层级（X.500 DIT） | 关系表（SQL） |
| 读/写比例 | 读多写少（优化读取） | 读写均衡 |
| 系统集成 | Samba ldapsam、NFS libnss-ldap、Linux PAM **原生支持** | 需要自研适配层 |
| 认证协议 | LDAP Bind（密码哈希在服务端比对） | 需自研认证逻辑 |
| Schema 扩展 | LDIF + ObjectClass 扩展（posixAccount 等） | DDL 迁移 |
| 备份 | LDIF 纯文本（人类可读、版本控制） | SQL dump |
| 部署复杂度 | 需理解 LDAP 概念 | 运维人员更熟悉 |

## 为什么选 LDAP

Samba、NFS、Linux PAM 等核心系统组件**原生支持 LDAP，不支持直接查询关系数据库**。若用关系数据库存储用户，必须在 Samba 与 NFS 之间单独维护账号同步逻辑，引入一致性风险。LDAP 作为目录服务天然适合作为统一身份源。

> 所谓统一身份源，不是"把所有数据放一个库"，而是"所有子系统都从同一个地方查询——且这个地方是它们原生支持的"。

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 4.3 节身份认证技术栈
