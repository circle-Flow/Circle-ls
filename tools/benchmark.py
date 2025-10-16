#!/usr/bin/env python3
import subprocess, time, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPILER = ROOT / "compiler"
VM_MANIFEST = ROOT / "vm" / "Cargo.toml"

def compile(src):
    print(f"[+] compile {src}")
    subprocess.check_call([sys.executable, "-m", "compiler", src], cwd=ROOT)

def run_vm(crcb):
    cmd = ["cargo", "run", "--release", "--manifest-path", str(VM_MANIFEST), "--", crcb]
    start = time.perf_counter()
    subprocess.check_call(cmd)
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: benchmark.py <examples/xxx.crc> [runs]")
        sys.exit(1)
    src = sys.argv[1]
    runs = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    compile(src)
    crcb = Path(src).with_suffix(".crcb")
    times = []
    for i in range(runs):
        t = run_vm(str(crcb))
        print(f"run {i}: {t:.6f}s")
        times.append(t)
    print(f"avg: {sum(times)/len(times):.6f}s")
