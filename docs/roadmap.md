
---

## ⚙️ `docs/bytecode_format.md`

```markdown
# ⚙️ CRC Bytecode Format Specification

> Internal binary format for `.crcb` (compiled CRC bytecode)

---

## 🧩 File Layout

+------------------+
| Magic Header | (CRC0)
+------------------+
| Version (u16) |
+------------------+
| Constant Pool |
+------------------+
| Function Table |
+------------------+
| Bytecode Section |
+------------------+
| EOF Marker |
+------------------+




---

## 🧠 Constant Pool

Each constant is stored as:

[u8: type_tag][len: u16][bytes: data]

| Tag | Type | Example |
|------|------|----------|
| `0x01` | Int | 42 |
| `0x02` | Float | 3.14 |
| `0x03` | String | "Hello" |
| `0x04` | Bool | true |

---

## 🧩 Function Table

Each function entry:

[u16: name_index][u16: arg_count][u32: bytecode_offset][u32: bytecode_length]


---

## 🔢 Instruction Encoding

Each instruction is **1–3 bytes**:
[OPCODE][OPERAND1?][OPERAND2?]



| Opcode | Mnemonic | Description |
|---------|-----------|-------------|
| `0x01` | LOAD_CONST idx | Push constant |
| `0x02` | LOAD_VAR idx | Load variable |
| `0x10` | ADD | Pop 2, push result |
| `0x11` | SUB | Pop 2, push result |
| `0x30` | RETURN | Return from fn |
| `0xFF` | HALT | End of program |

---

## 🧱 Example Encoding

CRC code:
```crc
let x = 1 + 2
print(x)



Bytecode (pseudo):

0x01 00  // LOAD_CONST 0 (1)
0x01 01  // LOAD_CONST 1 (2)
0x10     // ADD
0x03 00  // STORE_VAR 0
0x02 00  // LOAD_VAR 0
0x20     // CALL print
0xFF     // HALT


📦 Example File Header
Field	Bytes	Example
Magic	4	CRC0
Version	2	0001
Const Count	2	0005
Func Count	2	0002
Bytecode Size	4	00 00 00 84


Future Additions

Compressed constant pool (LZ4)

Debug symbols

Checksum validation

Native JIT precompiled section


---

## 🚀 `docs/roadmap.md`

```markdown
# 🗺️ CRC Language Roadmap

> Development roadmap for the Circle Runtime Compiler language.

---

## 🧩 Phase 1 — Bootstrap (Python Compiler)

**Goal:** Implement the CRC compiler frontend in Python.  
**Deliverables:**
- [x] Lexer + parser
- [x] AST builder
- [ ] Type inference engine
- [ ] Bytecode generator
- [ ] `.crcb` binary writer

---

## ⚙️ Phase 2 — Rust Virtual Machine

**Goal:** Create a high-performance VM for executing CRC bytecode.

**Deliverables:**
- [x] Stack-based VM
- [ ] Register-based execution model
- [ ] Cranelift JIT compiler
- [ ] Native Rust FFI bindings

---

## ⚡ Phase 3 — JIT Engine & Optimizations

**Goal:** Achieve real-time, zero-lag performance.

**Deliverables:**
- [ ] Integrate Cranelift JIT
- [ ] Constant folding & DCE
- [ ] Inline caching
- [ ] Parallel execution primitives

---

## 🎮 Phase 4 — Game and App Framework

**Goal:** Enable `.crc`-based game engines and Android apps.

**Deliverables:**
- [ ] CRC Game SDK
- [ ] Graphics APIs (OpenGL, Vulkan)
- [ ] CircleOS app runtime integration

---

## 🌍 Phase 5 — Cross-Platform Expansion

**Goal:** Bring CRC to all devices.

**Deliverables:**
- [ ] Android runtime (NDK)
- [ ] WebAssembly backend
- [ ] CircleOS integration layer
- [ ] VSCode / Neovim plugins (LSP)

---

## 🧱 Phase 6 — v1.0 Stable

**Goal:** Release CRC v1.0 with:
- Full standard library
- CircleOS SDK
- Native compilation
- Optimized JIT runtime
- Security-hardened memory model

---

## 🧩 Long-Term Goals

- Distributed CRC (networked VM)
- CircleCloud compiler farm
- AI-assisted CRC optimization
- Hardware-assisted CRC cores (FPGA)

---

## 🧭 Timeline (Estimate)

| Version | Target Date | Focus |
|----------|--------------|--------|
| v0.1 | Q1 2025 | Parser + Bytecode |
| v0.2 | Q2 2025 | Rust VM |
| v0.3 | Q3 2025 | JIT Compiler |
| v0.5 | Q4 2025 | Game SDK |
| v1.0 | 2026 | Stable release |



