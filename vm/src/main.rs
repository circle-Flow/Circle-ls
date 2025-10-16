use std::env;
use std::fs;
use anyhow::Result;
mod vm;
mod bytecode;
mod stdlib;
mod gc;
mod jit;
mod ffi;

use bytecode::Bytecode;
use vm::VM;

fn main() -> Result<()> {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Usage: crcvm <file.crcb>");
        std::process::exit(1);
    }
    let path = &args[1];
    let data = fs::read(path)?;
    let bc = Bytecode::from_bytes(&data)?;
    let mut vm = VM::new();
    vm.load_stdlib(stdlib::make_stdlib());
    vm.run(&bc)?;
    Ok(())
}
