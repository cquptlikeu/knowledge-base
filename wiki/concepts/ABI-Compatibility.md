---
type: concept
created: 2026-07-06
updated: 2026-07-07
tags: [rust, abi, ffi, binary-interface]
aliases: [ABI 兼容性, Application Binary Interface]
---

# ABI 兼容性

ABI（Application Binary Interface）定义了两个已编译的程序模块在机器码层面的交互协议。**API 是源码层面的契约，ABI 是二进制层面的契约**——API 兼容意味着代码能编译通过，ABI 兼容意味着编译后的二进制能正确链接和调用。

## 核心思想

ABI 定义了：
- 函数参数如何传递（寄存器还是栈）
- 返回值放在哪里
- 结构体在内存中的布局（字段顺序、对齐、填充）
- 虚函数表的布局
- 符号名称修饰（name mangling）

## Rust 中的 ABI

[[entities/Rust]] 默认不使用稳定的 ABI——Rust 编译器保留随时改变结构体布局和函数调用约定的权利，以获得更好的优化空间。

当需要与 C 或其他语言交互时，使用 `extern "C"` 来指定 C ABI，这是跨语言 FFI 的事实标准。

### Rust 1.76.0 的改进

1.76.0 新增了函数指针文档中的 ABI 兼容性章节，列出了当前被认为 ABI 兼容的 Rust 类型。最重要的是 `char` 和 `u32` 被正式确认为 ABI 等价。

## 什么时候关心 ABI

- 写 FFI 代码（Rust 调用 C，或 C 调用 Rust）
- 动态加载库（`dlopen` / `LoadLibrary`）
- 跨编译单元共享 trait object
- 插件系统

## 什么时候不关心 ABI

- 纯 Rust 项目内部——编译器自己处理一切
- 不暴露 `extern` 接口的应用代码
- 使用 `wasm-bindgen` 等有自己 ABI 层的框架

## 常见误区

> 「类型大小相同 = ABI 兼容」

不成立。ABI 兼容不仅要求大小相同，还要求对齐、寄存器分配策略等一致。`char` 和 `u32` 在 1.76 之前就大小相同，但 Rust 官方没有承诺 ABI 等价——直到 1.76 才正式补上这个保证。

## 相关概念对比

| 概念 | 层面 | 稳定性 |
|------|------|--------|
| API 兼容 | 源码 | 重命名/改签名就破坏 |
| ABI 兼容 | 二进制 | 改了内部布局就破坏 |
| 语义兼容 | 行为 | 改了返回值内容就破坏 |

## 参考

- [[summaries/Rust-1.76.0]]
- [[entities/Rust]]
