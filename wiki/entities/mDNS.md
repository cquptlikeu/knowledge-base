---
type: entity
created: 2026-07-07
updated: 2026-07-07
tags: [网络发现, 局域网, Zeroconf, 移动端]
aliases: [Multicast DNS, Zeroconf, mDNS协议]
---

# mDNS（Multicast DNS）

多播 DNS / Zeroconf 协议，用于局域网内零配置服务发现，无需 DNS 服务器或手动 IP 配置。

## 核心特征

- **零配置**：设备自动向局域网广播服务信息，客户端自动扫描发现
- **标准协议**：RFC 6762，被 macOS Bonjour、Linux Avahi 等广泛实现
- **Go 实现**：本架构使用 grandcat/zeroconf 库

## 主要应用场景

- **NAS 设备发现**：移动 App 无需手动输入 IP 即可找到 NAS
- **局域网服务广播**：authd 启动时广播 `_nas._tcp.local.` 服务记录
- **家庭/办公室网络**：覆盖 99% 的局域网场景

## 与其他实体的关系

- **配合 [[concepts/三级连接回退]]**：mDNS 是三级回退中的 Level 2，作为主力发现机制
- **配合 [[entities/authd]]**：authd 启动时通过 mdns/server.go 广播服务信息
- **配合 [[entities/WiFi-P2P]]**：Level 1（P2P 直连）和 Level 3（缓存 IP）作为兜底

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 10 章移动接入
