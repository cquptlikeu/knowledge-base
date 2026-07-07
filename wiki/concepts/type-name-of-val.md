---
type: concept
created: 2026-07-06
updated: 2026-07-07
tags: [rust, debugging, reflection, type-system]
aliases: [type_name_of_val, 类型名反射]
---

# type_name_of_val

`std::any::type_name_of_val(&T)` 是 [[entities/Rust]] 标准库中的类型名反射函数，于 1.76.0 稳定化。它通过**值引用**（而非类型参数）获取类型的运行时名称字符串。

## 核心思想

Rust 的类型信息在编译后大部分被擦除（单态化），但编译器仍保留了足够的元数据来生成类型名称。`type_name_of_val` 提供了一个标准化的入口来访问这些信息。

## API 设计

```rust
pub fn type_name_of_val<T: ?Sized>(val: &T) -> &'static str
```

- 参数是 `&T`（而非 `T`），消耗的是一个引用而非值的所有权
- 返回 `&'static str`，字符串是编译时生成的，生命周期为整个程序
- `T: ?Sized` 约束允许对 trait object 和切片也使用

## 与 `type_name` 的区别

| 特性 | `type_name::<T>()` | `type_name_of_val(&T)` |
|------|---------------------|------------------------|
| 指定类型 | 显式泛型参数 | 从引用自动推断 |
| 闭包 | ❌ 不可用（闭包类型无名） | ✅ 可用 |
| `impl Trait` 返回值 | ❌ 不可用 | ✅ 可用 |
| 引入版本 | 1.38 | 1.76 |
| 消耗值 | 否 | 否（引用） |

## 适用场景

- **调试**：想知道某个复杂泛型/闭包/不透明类型的实际类型
- **日志**：记录「这个值是什么类型」而不需要 `Debug` trait
- **错误消息**：生成包含类型名称的友好错误

## 不适用场景

- **生产逻辑**：不要基于 `type_name_of_val` 的返回值做分支判断——类型名称不是稳定保证的，可能在编译器版本间变化
- **序列化/反序列化**：这个函数返回的是 Rust 编译器的内部类型名，不是序列化格式
- **性能敏感路径**：`type_name_of_val` 返回的是静态字符串，理论上零开销，但它的存在可能阻止某些编译器优化（需要验证）

## 常见误区

> 「`type_name_of_val` 可以做运行时类型判断」

不可以。返回的字符串内容**不是稳定 API**——编译器可能在不同版本改变类型名的格式。只用于调试/日志。

## 示例

```rust
fn get_iter() -> impl Iterator<Item = i32> {
    [1, 2, 3].into_iter()
}

fn main() {
    let iter = get_iter();
    // type_name 在此无法使用——impl Iterator 没有可写的类型名
    let name = std::any::type_name_of_val(&iter);
    println!("{name}");
    // 输出: "core::array::iter::IntoIter<i32, 3>"
}
```

## 参考

- [[summaries/Rust-1.76.0]]
- [[entities/Rust]]
