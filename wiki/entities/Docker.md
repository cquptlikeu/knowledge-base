---
type: entity
created: 2026-07-07
updated: 2026-07-07
tags: [容器化, 部署, DevOps, NAS]
aliases: [Docker, Docker Compose, 容器]
---

# Docker & Docker Compose

容器运行时与多容器编排工具，在本架构中用于实现服务的环境隔离与单命令部署。

## 核心特征

- **环境一致性**：将服务及其所有依赖封装为独立镜像，开发、测试、生产环境运行完全相同的制品
- **Docker Compose 多容器编排**：以 YAML 声明多容器服务栈及其依赖关系
- **数据卷（Volume）**：与容器生命周期解耦的持久化存储

## 主要应用场景

- **异构服务编排**：OpenLDAP、Samba、NFS、Nginx、Go 后端等多个异构服务统一管理
- **简化部署**：`docker compose up -d` 单条命令启动完整服务栈
- **升级安全**：镜像版本化，升级可回滚

## 与其他实体的关系

- **配合 [[entities/OpenLDAP]]**：以 osixia/openldap 镜像部署，数据通过 Volume 持久化
- **配合 [[entities/authd]]**：编译为静态二进制后打包进 nas 主容器
- **配合 Samba/NFS/Nginx**：四项服务运行于同一容器，通过 localhost 通信

## 架构中的特殊考量

采用 `network_mode: host` 而非默认 bridge 模式。原因：SMB 协议依赖广播/多播进行设备发现，在 bridge 模式下无法工作；NFS 的 RPC 端口映射依赖宿主机端口；host 模式消除了 NAT 层，协议行为与裸机一致。

## 四容器架构

1. openldap 容器 — 身份数据持久化
2. ldap-init 容器 — 一次性初始化，完成后自动退出
3. nas 主容器 — authd + Samba + NFS + Nginx 四项服务
4. （规划中）nas-agent 容器 — AI Agent 服务

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 4.8 节、第 13 章
