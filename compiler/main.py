import sys
from pathlib import Path
from .lexer import lex
from .parser import Parser
from .analyzer import analyze
from .optimizer import optimize
from .bytecode import emit_bytecode
from .runtime_stub import run_bytecode

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m compiler <file.crc>")
        sys.exit(1)

    path = Path(sys.argv[1])
    code = path.read_text()

    print(f"[+] Compiling {path.name} ...")

    tokens = lex(code)
    ast = Parser(tokens).parse()
    analyze(ast)
    optimized = optimize(ast)
    bytecode = emit_bytecode(optimized)

    out_path = path.with_suffix(".crcb")
    out_path.write_bytes(bytecode)
    print(f"[✓] Compiled to {out_path.name} ({len(bytecode)} bytes)")

    # Run using runtime stub
    run_bytecode(bytecode)

if __name__ == "__main__":
    main()
