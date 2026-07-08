---
type: entity
created: 2026-07-07
updated: 2026-07-07
tags: [Web框架, Go, HTTP, REST API]
aliases: [Gin, Gin v1.9]
---

# Gin

Go 生态中性能最优的 HTTP 路由框架之一，在本架构中用于构建 authd 的 RESTful API 层。

## 核心特征

- **中间件链**：JWT 验证、跨域（CORS）、请求日志等可组合中间件
- **路由分组**：公开端点 / 认证端点 / 管理端点 / 内部端点（仅 localhost）
- **参数绑定与校验**：结构体 tag 驱动的请求参数自动绑定和验证
- **Swagger 集成**：自动生成 API 文档

## 主要应用场景

- **HTTP RESTful API 开发**：轻量级、高性能的 API 服务
- **中间件架构**：需要灵活组合认证、日志、限流等横切关注点的场景

## 与其他实体的关系

- **配合 [[entities/Go]]**：作为 Go Web 框架，是 Go 后端开发的标准选择之一
- **配合 [[entities/JWT]]**：通过中间件链实现 JWT 无状态认证
- **配合 [[entities/authd]]**：authd 的 HTTP 路由层基于 Gin 构建

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 4.2 节后端技术栈
