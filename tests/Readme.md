How to wire everything and run

Place the Python compiler package at crc-lang/compiler/ (the compiler you already created earlier).

Place the Rust VM sources under crc-lang/vm/ as above.

Build the Rust VM (release recommended):

cd crc-lang/vm
cargo build --release


Compile & run a sample .crc using your Python compiler and VM:

From repo root:

# compile a file
python -m compiler examples/hello.crc

# run VM
cargo run --release --manifest-path vm/Cargo.toml -- examples/hello.crcb


You should see VM output showing the result or a message.

Run the test runner (which compiles tests then runs VM):

python tests/run_tests.py


Run benchmark:

python tools/benchmark.py examples/parallel_sum.crc 3

Notes, limitations & next steps

This VM is intentionally minimal: it implements the opcodes emitted by the simple Python compiler (LOAD_CONST, STORE_VAR, LOAD_VAR, arithmetic ops, HALT).

The VM prints the top-of-stack on HALT — this is useful for interactive debugging. Later you’ll add PRINT opcode or I/O syscalls.

gc.rs, jit.rs, and ffi.rs are stubs/placeholders now. The JIT will be implemented with Cranelift when you move to JIT stage.

To reach your extreme performance targets you’ll:

Design a compact register-based bytecode,

Implement a high-performance VM in Rust,

Add Cranelift JIT to compile hot functions to native machine code,

Replace dynamic Value enum with typed machine values and minimize boxing,

Implement specialized builtins (math, vectorized ops, parallel primitives).

The project is arranged so you can iteratively replace parts (compiler, VM, JIT) while keeping the same .crcb file format.
