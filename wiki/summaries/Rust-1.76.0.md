---
type: summary
created: 2026-07-06
updated: 2026-07-07
tags: [Rust, release, 1.76]
source: "[[raw/casually/2024-02-08-Rust-1.76.0]]"
---

# Rust 1.76.0 发布摘要

Rust 1.76.0 于 2024-02-08 发布，是一个相对较小的增量版本。但 Rust 团队的发布哲学是「每次增量改进累积成更大的整体」——这个版本在 ABI 稳定性和调试体验上做了有意义的推进。

## 核心更新

### ABI 兼容性规范文档化

Rust 1.76 在函数指针文档中新增了 [[concepts/ABI-Compatibility]] 章节，这是 Rust 首次以文档形式系统描述函数签名的 ABI 兼容性规则。

**为什么重要**：在此之前，Rust 的 ABI 兼容性大多是「事实标准」而非「明确保证」。没有文档，FFI 开发者只能靠经验和社区传闻来判断哪些类型跨 FFI 边界是安全的。现在有了官方列表，降低了 unsafe 代码的出错概率。

**具体内容**：该章节列出了当前在 Rust 中被认为是 ABI 兼容的参数类型和返回类型。大部分内容只是**描述现有状态**而非新增保证。

**唯一的新增保证**：`char` 和 `u32` 现在被明确视为 ABI 兼容。它们的大小和对齐一直相同（4 字节），但此前没有在函数调用 ABI 层面正式承诺等价。对于 FFI 代码来说，现在可以安全地在 extern 函数签名中将 `char` 替换为 `u32`（反之亦然）。

> 原文关键句：*"For the most part, this documentation is not adding any new guarantees, only describing the existing state of compatibility."*

### `type_name_of_val` — 让类型名不再「不可描述」

1.76 新增了 `std::any::type_name_of_val(&T)`，解决了 [[concepts/type-name-of-val]] 长期以来的一个痛点。

**问题**：自 Rust 1.38 起就有 `any::type_name::<T>()` 获取类型名称，但它要求显式指定泛型参数 `T`。对于 `impl Trait` 返回类型和闭包——这些类型根本没有可写的类型名——`type_name` 形同虚设。

**解决方案**：`type_name_of_val` 接受一个引用而非类型参数，让编译器自动推断类型：

```rust
fn get_iter() -> impl Iterator<Item = i32> {
    [1, 2, 3].into_iter()
}

fn main() {
    let iter = get_iter();
    let iter_name = std::any::type_name_of_val(&iter);
    let sum: i32 = iter.sum();
    println!("The sum of the `{iter_name}` is {sum}.");
}
// 输出: The sum of the `core::array::iter::IntoIter<i32, 3>` is 6.
```

**实际价值**：这在调试泛型代码、宏展开、以及 `impl Trait` 密集的代码时非常有用。不是生产代码用的，但调试时能省大量时间——你不再需要靠编译器错误信息来反推变量的实际类型。

### 稳定化的 API（共 9 项）

**智能指针**：
- `Arc::unwrap_or_clone` / `Rc::unwrap_or_clone` — 当引用计数为 1 时取出内部值，否则克隆。相比手动 `match` 写法更简洁

**调试/检查**：
- `Result::inspect` / `Result::inspect_err` — 对 Ok/Err 值做副作用操作而不改变结果，类似 Iterator 的 `inspect`。日志记录场景常用
- `Option::inspect` — 同上，对 Some 值做副作用操作

**类型反射**：
- `type_name_of_val` — 见上文

**指针工具**：
- `ptr::from_ref` / `ptr::from_mut` — 从引用创建原始指针，比 `&T as *const T` 更显式
- `ptr::addr_eq` — 比较两个指针是否指向同一地址（而非比较指向的值）

**哈希基础设施**：
- `std::hash::{DefaultHasher, RandomState}` — 原本藏在 `std::collections::hash_map` 下，现在可以在不引入 HashMap 的情况下使用标准哈希算法

## 评级

| 维度 | 评价 |
|------|------|
| 影响范围 | 中低 — 日常 Rust 用户可能感知不强 |
| API 质量 | 高 — 新 API 填补的都是真实存在的痛点 |
| ABI 意义 | 重要 — 规范化 ABI 文档是 Rust 走向更正式 FFI 保证的一步 |
| 值得升级 | 是 — 无破坏性变更，新 API 有用 |

## 相关实体与概念

- [[entities/Rust]] — Rust 编程语言
- [[concepts/ABI-Compatibility]] — ABI 兼容性
- [[concepts/type-name-of-val]] — 类型名调试函数
