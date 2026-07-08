---
type: entity
created: 2026-07-07
updated: 2026-07-07
tags: [认证, 安全, 令牌, HTTP]
aliases: [JSON Web Token, JWT令牌]
---

# JWT（JSON Web Token）

JSON Web Token，一种无状态会话载体，在本架构中用于 HTTP API 层的身份认证。

## 核心特征

- **无状态**：服务端无需维护会话存储，天然适合多实例扩展
- **自包含**：Token 中携带用户名与角色声明，中间件层可在不查询后端的情况下完成身份核验
- **HS256 算法**：HMAC-SHA256 对称签名，验证快速
- **24 小时有效期**：平衡安全性与用户体验，到期后客户端重新登录

## 主要应用场景

- **HTTP API 无状态认证**：移动 App 和 Web 管理台的身份凭证
- **微服务认证**：无状态令牌适合多实例水平扩展
- **权限路由守卫**：基于 Token 中 role 声明区分 admin/user 接口访问权

## 与其他实体的关系

- **依赖 [[entities/OpenLDAP]]**：LDAP Bind 验证成功后由 authd 签发 JWT
- **配合 [[entities/Gin]]**：Gin 中间件链解析并校验 JWT
- **配合 [[entities/authd]]**：authd 的 golang-jwt 模块负责签发与验证

## 安全设计

- 密钥通过容器环境变量注入，不硬编码于代码，支持运维周期性轮换
- 管理员专属接口由独立中间件守卫，普通用户 JWT 携带 `role: user` 时直接返回 403

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 5.5 节 JWT 令牌设计
