---
type: entity
created: 2026-07-07
updated: 2026-07-07
tags: [WiFi, 点对点, Android, 网络]
aliases: [WiFi P2P, Wi-Fi Direct, WiFi直连]
---

# WiFi P2P（Wi-Fi Direct）

Android 设备间的点对点 WiFi 直连技术，无需接入点（AP）即可建立连接。

## 核心特征

- **无 AP 直连**：在手机与 NAS 之间建立点对点 WiFi 连接
- **固定 IP**：NAS 作为 P2P 组长（Group Owner），IP 固定为 192.168.49.1
- **Kotlin 原生实现**：通过 Android WiFi P2P API 实现，经 JSB 暴露给 React Native

## 主要应用场景

- **基础网络不可用场景**：没有路由器/AP 的环境下直接连接 NAS
- **移动端三级连接回退的 Level 1**：最高优先级的连接方式

## 与其他实体的关系

- **配合 [[concepts/三级连接回退]]**：WiFi P2P 是第一优先级（Level 1）的连接方式
- **配合 [[entities/mDNS]]**：Level 2 主力发现，P2P 是无 AP 的兜底
- **配合 [[entities/Next.js]]**：由 Kotlin 原生模块实现，JSB 暴露给 JS 层

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 10 章移动接入
