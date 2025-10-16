# 🌀 CRC Language (Circle Runtime Compiler)

> The next-generation high-speed programming language for CircleOS — combining the simplicity of Python, the safety of Rust, and the raw speed of C.

---

## 🚀 Overview

**CRC (Circle Runtime Compiler)** is a new programming language designed for the **CircleOS** ecosystem.  
Built initially in **Python**, compiled to **bytecode**, and executed by a **Rust-based virtual machine (VM)** — CRC is a **high-performance hybrid language** that aims to achieve **near-native execution speeds**.

CRC source files end with `.crc` and compile into `.crcb` bytecode binaries.

---

## ✨ Features

| Feature | Description |
|----------|-------------|
| 🧠 **Pythonic Syntax** | Easy to learn, minimal, and elegant |
| ⚙️ **Rust-Level Safety** | Type inference, no unsafe memory access |
| 🧩 **Compiled Runtime** | Converts `.crc` → `.crcb` (bytecode) |
| ⚡ **Ultra Fast VM** | Rust-based JIT (Cranelift backend) |
| 🔒 **Safe Concurrency** | Built-in parallel execution primitives |
| 🧱 **Extensible** | Integrates with Rust, C, and C# through FFI |
| 🎮 **Game & App Ready** | Designed for game engines and interactive apps |
| 🌍 **Cross-Platform** | Linux, macOS, Windows, Android |

---
#crc-lang/

├── compiler/ # Python frontend compiler

├── vm/ # Rust bytecode runtime (VM + JIT)

├── examples/ # Example .crc programs

├── docs/ # Specs and developer documentation

├── tests/ # Automated testing suite

└── tools/ # Profiling and benchmarking utilities


---

# 🧱 Example Program 
`examples/hello.crc`
```crc
fn main() {
    let name = "World"
    print("Hello, " + name + "!")
}

Compile and run :
python -m compiler examples/hello.crc
./target/debug/crcvm examples/hello.crcb

Output:

Hello, World!
Execution time: 0.0000000000001ms


Getting Started
Requirements

Python 3.12+

Rust (≥ 1.75)

Cargo (for VM)

Optional: Cranelift or LLVM (for JIT)

Build Steps:

git clone https://github.com/yourname/crc-lang.git
cd crc-lang
cargo build -p vm
python -m compiler examples/hello.crc


Run Bytecode:

cargo run -p vm -- examples/hello.crcb
Design Goals

-Zero-runtime overhead

-Predictable performance

-Cross-platform binaries

-Parallel by default

-Safe systems programming

CRC represents the foundation of CircleOS applications, designed to outperform Python while maintaining developer friendliness.

🛣️ Roadmap

See docs/roadmap.md
 for the detailed release plan.

 Credits

Built with 🦀 Rust and 🐍 Python —
for the dreamers building the future of computing with CircleOS.


---

## ⚖️ `LICENSE`

MIT License

Copyright (c) 2025 CircleOS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


⚖️ License

Licensed under the MIT License.
See LICENSE for full details.

