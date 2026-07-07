---
type: entity
created: 2026-07-06
updated: 2026-07-07
tags: [rust, programming-language, systems, memory-safety]
aliases: [Rust 语言, Rust 编程语言]
---

# Rust

Rust 是由 Mozilla 创立、现由 Rust 基金会维护的系统编程语言。核心卖点是**零成本抽象、内存安全（无 GC）、无畏并发**。

## 核心特征

- **所有权系统**：编译期保证内存安全，无需垃圾回收——这是 Rust 区别于 C/C++ 和 GC 语言的最核心设计
- **借用检查器**：编译时防止数据竞争和悬垂指针
- **零成本抽象**：高级语法不产生运行时开销
- **trait 系统**：基于 trait 的多态，类似 Haskell typeclass，比传统 OOP 更灵活
- **enum 和模式匹配**：代数数据类型 + 穷尽匹配，消除 null 和未处理分支
- **Cargo**：内置的包管理器和构建系统，生态集中在 crates.io

## 主要应用场景

| 场景 | 为什么适合 |
|------|----------|
| 系统编程 | 无 GC、细粒度内存控制、与 C ABI 互操作 |
| WebAssembly | 零运行时、极小二进制体积 |
| CLI 工具 | 跨平台编译、单二进制分发 |
| 网络服务 | 高并发、低延迟、内存安全防止安全漏洞 |
| 嵌入式 | no_std 支持、裸金属编程 |
| 区块链/加密 | 内存安全 + 性能 = 适合安全关键场景 |

## 版本发布节奏

Rust 每 6 周发布一个新稳定版本，版本号以 `1.x.0` 递增。每个版本的详细变更记录在官方博客的 release notes 中。

已收录的版本：
- **1.76.0** (2024-02-08)：[[summaries/Rust-1.76.0]] — ABI 兼容性文档、`type_name_of_val`、9 项 API 稳定化

## 与相关技术的关系

- vs [[entities/Go]]：都是系统级语言，但 Rust 更侧重零成本安全和表达力，Go 更侧重简洁和编译速度
- vs C/C++：Rust 的内存安全是编译期保证的，不需要 sanitizer 或 valgrind 来防 UB
- vs Zig：都在挑战 C 的地位，Zig 更接近 C 的哲学（手动内存管理），Rust 走的是类型系统强行安全路线

## 学习资源

未收录但值得关注：Rust Book、Rust by Example、Rustnomicon（unsafe Rust 指南）

## 参考

- [[summaries/Rust-1.76.0]]
- [[concepts/ABI-Compatibility]]
- [[concepts/type-name-of-val]]
