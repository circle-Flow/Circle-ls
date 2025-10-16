# 📘 CRC Language Specification

> Draft v0.1 — Circle Runtime Compiler (CRC) Language Design Document

---

## 🎯 Purpose

CRC is a **compiled, high-performance programming language** that unifies:
- Python’s readable syntax
- Rust’s memory safety
- C’s performance

---

## 🧩 Core Concepts

### 1️⃣ File Format
- Source files: `.crc`
- Compiled bytecode: `.crcb`

### 2️⃣ Data Types
| Type | Description |
|------|--------------|
| `int` | 64-bit signed integer |
| `float` | 64-bit floating point |
| `bool` | true / false |
| `string` | UTF-8 string |
| `list[T]` | Generic dynamic array |
| `map[K, V]` | Key-value storage |
| `fn` | Function, first-class citizen |

### 3️⃣ Variables

```crc
let x = 42
let y: float = 3.14

4️⃣ Functions

fn add(a: int, b: int) -> int {
    return a + b
}

5️⃣ Parallelism

fn main() {
    let data = [1, 2, 3, 4, 5]
    let doubled = parallel_map(data, |x| x * 2)
    print(doubled)
}


6️⃣ Error Handling

try {
    open("file.txt")
} catch e {
    print("Error: " + e)
}

7️⃣ Imports

import std.math
import std.io

🧱 Execution Model

CRC compiles to bytecode executed on a register-based virtual machine.
Each .crcb file contains:

Header (magic bytes, version, checksum)

Constant pool

Function table

Bytecode instructions

🔢 Instruction Set (Excerpt)
Opcode	Mnemonic	Description
0x01	LOAD_CONST	Push constant to stack
0x02	LOAD_VAR	Load variable
0x03	STORE_VAR	Store variable
0x10	ADD	Addition
0x11	SUB	Subtraction
0x20	CALL	Call function
0x30	RETURN	Return from function
0xFF	HALT	Stop execution

🧠 Type System

CRC uses static type inference — types are inferred unless explicitly declared.
Functions and operators are monomorphic at compile-time for performance.

🔒 Memory Management

CRC uses reference counting (ARC) initially, with a future arena allocator for the VM to achieve deterministic memory reuse.

🧩 FFI and Interop

CRC supports:

Rust plugins (compiled .so / .dll)

C# bindings (via CircleOS interop layer)

Python embedding (for early integration)

🌍 Platform Support

Platform	Status
Linux	✅ Supported
macOS	✅ Supported
Windows	✅ Supported
Android	🧩 Planned
WebAssembly	🧩 Future

let x = 42
let y: float = 3.14
