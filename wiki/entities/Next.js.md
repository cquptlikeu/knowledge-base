---
type: entity
created: 2026-07-07
updated: 2026-07-07
tags: [前端框架, React, Web开发, SSR]
aliases: [Next.js 16, NextJS, App Router]
---

# Next.js

Vercel 开发的 React 全栈框架，在本架构中用于构建 Web 管理台（nas-web）。

## 核心特征

- **App Router 架构**：基于文件系统的路由（/app/files/page.tsx 对应 /files 路径）
- **SSR/CSR 混合**：登录页/首屏用 SSR 提升首屏速度，交互密集页面用 CSR 保证流畅度
- **前后端分离**：Next.js 应用独立构建与部署，通过 HTTP 调用 authd RESTful API

## 主要应用场景

- **Web 管理后台**：仪表盘、文件管理、用户管理、审计日志、存证查询
- **产品落地页**：nas-landing 使用 Three.js + React Three Fiber 实现 3D 展示

## 与其他实体的关系

- **配合 React 19**：Next.js 基于 React 19 的并发渲染能力
- **配合 TypeScript 5.5**：编译期类型检查，降低前后端联调错误
- **配合 shadcn/ui + Radix UI**：构建管理台 UI
- **依赖 [[entities/authd]]**：所有数据操作通过 authd HTTP API 进行

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 4.6 节前端技术栈
