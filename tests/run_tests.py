#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPILER = ROOT / "compiler"
VM_BIN = "cargo"
TEST_DIR = ROOT / "tests"

def compile_crc(src: Path):
    print(f"[+] compiling {src.name}")
    # run python -m compiler <file>
    cmd = [sys.executable, "-m", "compiler", str(src)]
    subprocess.check_call(cmd, cwd=ROOT)

def run_vm(crcb: Path):
    print(f"[+] running vm on {crcb.name}")
    # cargo run --manifest-path vm/Cargo.toml -- <crcb>
    cmd = ["cargo", "run", "--release", "--manifest-path", str(ROOT/"vm"/"Cargo.toml"), "--", str(crcb)]
    subprocess.check_call(cmd)

def main():
    tests = list(TEST_DIR.glob("*.crc"))
    if not tests:
        print("no test crc files found")
        return
    for t in tests:
        compile_crc(t)
        crcb = t.with_suffix(".crcb")
        if not crcb.exists():
            print("compiled file missing:", crcb)
            continue
        run_vm(crcb)

if __name__ == "__main__":
    main()
