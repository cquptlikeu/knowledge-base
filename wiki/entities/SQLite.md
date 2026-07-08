---
type: entity
created: 2026-07-07
updated: 2026-07-07
tags: [数据库, 嵌入式, SQL, NAS]
aliases: [SQLite, modernc.org/sqlite]
---

# SQLite

轻量级嵌入式关系数据库，在本架构中用于存储业务元数据与审计存证数据。

## 核心特征

- **零配置**：无独立服务进程，无端口、无守护进程，随应用启动
- **单文件存储**：整个数据库为一个文件（.nas.db），备份即复制，迁移零成本
- **ACID 事务**：完整事务语义，操作日志写入与哈希链节点生成保持原子性
- **modernc 纯 Go 实现**：无 CGO 依赖，保证后端二进制静态编译

## 主要应用场景

- **NAS/边缘设备**：资源受限环境下替代 PostgreSQL/MySQL
- **审计日志**：certified_operations 表（22 字段）记录每次文件/身份操作的完整上下文
- **哈希链存证**：proof_records 表以链式哈希结构串联所有操作记录

## 与其他实体的关系

- **配合 [[entities/Go]]**：通过 modernc.org/sqlite + sqlx 访问，保持纯 Go 静态编译
- **配合 [[concepts/哈希链可信存证]]**：存储哈希链节点数据
- **vs [[entities/OpenLDAP]]**：SQLite 管理业务元数据（关系数据），LDAP 管理身份数据（目录数据），各司其职

## 选择理由

> 零依赖、单文件存储、ACID 事务语义完备、无需独立数据库服务进程，完全契合 NAS 设备的轻量化运行需求。

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 4.5 节数据存储、第 12.4 节业务元数据层
