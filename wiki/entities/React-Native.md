---
type: entity
created: 2026-07-07
updated: 2026-07-07
tags: [移动开发, 跨平台, React, Android]
aliases: [React Native, RN, nas-app]
---

# React Native

Meta 开发的跨平台移动应用框架，在本架构中用于构建 Android 移动客户端（nas-app）。

## 核心特征

- **JS + Kotlin 混合架构**：JS 层负责业务逻辑与 UI，Kotlin 原生模块负责访问 Android 系统 API（NFC、WiFi P2P）
- **JSB（JavaScript Bridge）**：JS 层与原生层之间的通信机制，保证跨平台代码与平台能力的解耦
- 版本 0.85

## 主要应用场景

- **移动端文件管理**：浏览、上传、下载、移动 NAS 文件
- **三级连接回退**：WiFi P2P → mDNS → 缓存 IP 的自动设备发现
- **NFC 碰一碰登录**：Kotlin 原生 NFC 模块 + React Native UI
- **照片自动备份**：登录后自动上传相册照片

## 与其他实体的关系

- **配合 [[entities/NFC]]**：Kotlin 原生 NFC 模块通过 JSB 暴露给 React Native
- **配合 [[entities/WiFi-P2P]]**：Kotlin WifiP2pModule 通过 JSB 通信
- **依赖 [[entities/authd]]**：所有网络请求通过 authd HTTP API 进行

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 10 章移动接入
