---
type: entity
created: 2026-07-07
updated: 2026-07-07
tags: [近场通信, 认证, 移动端, 安全]
aliases: [Near Field Communication, 碰一碰登录]
---

# NFC（Near Field Communication）

近场通信技术，在本架构中用于实现碰一碰免密登录，消除密码输入操作。

## 核心特征

- **标签无凭据原则**：NFC 标签仅存储 UID（物理唯一标识），不存储任何密码、密钥或 Token
- **设备绑定**：绑定关系以 ANDROID_ID + 标签 UID 双重验证，防标签复制攻击
- **绑定数据存储于 LDAP**：ou=nfc_bindings 组织单元，与用户身份同源管理

## 主要应用场景

- **家庭场景便捷登录**：用户用手机会碰触 NFC 标签即可登录 NAS
- **企业快捷接入**：无需记忆密码，物理接触完成认证
- **Kotlin 原生实现**：通过 Android HCE/NDEF API 实现 NFC 读写

## 与其他实体的关系

- **依赖 [[entities/OpenLDAP]]**：NFC 绑定关系存储于 LDAP ou=nfc_bindings
- **配合 [[entities/authd]]**：authd 的 /api/nfc-login 端点处理 NFC 登录流程
- **配合 [[entities/React-Native]]**：Kotlin NFC 原生模块通过 JSB 暴露给 React Native

## 安全设计

> NFC 标签本身不存储任何凭据（密码、密钥），仅作为触发认证流程的物理媒介。即使 NFC 标签被复制，在原绑定设备之外也无法用于登录。

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 10.3 节 NFC 登录
