#!/usr/bin/env python3
import subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VM_MANIFEST = ROOT / "vm" / "Cargo.toml"

def profile(crcb):
    cmd = ["cargo", "run", "--manifest-path", str(VM_MANIFEST), "--", str(crcb)]
    start = time.perf_counter()
    subprocess.check_call(cmd)
    end = time.perf_counter()
    print("elapsed:", end - start)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: profiler.py <file.crcb>")
        sys.exit(1)
    profile(sys.argv[1])
