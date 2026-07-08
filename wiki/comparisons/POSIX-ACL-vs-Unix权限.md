---
type: comparison
created: 2026-07-07
updated: 2026-07-07
tags: [权限控制, 文件系统, Linux, 安全]
---

# POSIX ACL vs 传统 Unix 权限

## 对比维度

| 维度 | 传统 Unix 权限（rwx） | POSIX ACL |
|------|----------------------|-----------|
| 权限主体 | 3 个（Owner/Group/Other） | 无限（任意具名用户/组） |
| 精细度 | 粗粒度（三类人） | 细粒度（每个用户/组独立设置） |
| 权限类型 | r、w、x 三种 | r、w、x 三种（可扩展到 default ACL） |
| 企业场景 | ❌ 无法为特定用户单独授权 | ✅ 支持任意用户的精细化授权 |
| 默认权限 | umask | default ACL（目录继承） |
| 跨协议一致性 | 一致（但粒度粗） | 一致（Samba/NFS/VFS 原生支持） |
| 工具 | chmod | setfacl / getfacl |
| 存储 | inode 权限位 | 文件系统扩展属性（xattr） |

## 典型场景

**新增成员访问共享目录**：
- 传统 Unix：只能把他加到共享组 → 影响范围过大（组内所有权限都给了）
- POSIX ACL：`setfacl -m u:zhangsan:r /data/shared/project-a` → 只给他这一个目录的读权限

## 为什么即使"够用"也要选 POSIX ACL

传统 Unix 权限理论上也能满足基本需求，但当企业场景要求"给张三访问 A 目录但不能访问 B 目录，给李四访问 B 但不能访问 A"时，Unix 权限完全无法表达。POSIX ACL 是 Linux 内核原生能力，选择它的额外成本几乎为零，但能力上限远高于 Unix 权限。

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 6.2 节
