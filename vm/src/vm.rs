use crate::bytecode::{Bytecode, Instr, Constant};
use anyhow::{Result, bail};
use std::collections::HashMap;

#[derive(Debug, Clone)]
pub enum Value {
    Number(f64),
    Str(String),
    None,
}

pub struct VM {
    stack: Vec<Value>,
    globals: HashMap<String, Value>,
    stdlib: HashMap<String, fn(&mut VM) -> Result<()>>,
}

impl VM {
    pub fn new() -> Self {
        Self {
            stack: Vec::new(),
            globals: HashMap::new(),
            stdlib: HashMap::new(),
        }
    }

    pub fn load_stdlib(&mut self, lib: HashMap<String, fn(&mut VM) -> Result<()>>) {
        self.stdlib = lib;
    }

    pub fn run(&mut self, bc: &Bytecode) -> Result<()> {
        let mut ip: usize = 0;
        while ip < bc.code.len() {
            let instr = &bc.code[ip];
            match instr {
                Instr::LoadConst(idx) => {
                    let idx = *idx as usize;
                    if let Some(c) = bc.consts.get(idx) {
                        match c {
                            Constant::Number(n) => self.stack.push(Value::Number(*n)),
                            Constant::Str(s) => self.stack.push(Value::Str(s.clone())),
                        }
                    } else {
                        bail!("const index out of range: {}", idx);
                    }
                    ip += 1;
                }
                Instr::StoreVar(idx) => {
                    let idx = *idx as usize;
                    let name = match bc.consts.get(idx) {
                        Some(Constant::Str(s)) => s.clone(),
                        Some(Constant::Number(n)) => n.to_string(),
                        None => "".to_string(),
                    };
                    let val = self.stack.pop().unwrap_or(Value::None);
                    self.globals.insert(name, val);
                    ip += 1;
                }
                Instr::LoadVar(idx) => {
                    let idx = *idx as usize;
                    let name = match bc.consts.get(idx) {
                        Some(Constant::Str(s)) => s.clone(),
                        Some(Constant::Number(n)) => n.to_string(),
                        None => "".to_string(),
                    };
                    if let Some(v) = self.globals.get(&name) {
                        self.stack.push(v.clone());
                    } else {
                        self.stack.push(Value::None);
                    }
                    ip += 1;
                }
                Instr::Add => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    let res = Self::binary_arith(a, b, |x, y| x + y)?;
                    self.stack.push(Value::Number(res));
                    ip += 1;
                }
                Instr::Sub => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    let res = Self::binary_arith(a, b, |x, y| x - y)?;
                    self.stack.push(Value::Number(res));
                    ip += 1;
                }
                Instr::Mul => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    let res = Self::binary_arith(a, b, |x, y| x * y)?;
                    self.stack.push(Value::Number(res));
                    ip += 1;
                }
                Instr::Div => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    let res = Self::binary_arith(a, b, |x, y| x / y)?;
                    self.stack.push(Value::Number(res));
                    ip += 1;
                }
                Instr::Halt => {
                    // For demonstration, print top-of-stack if any
                    if let Some(v) = self.stack.last() {
                        match v {
                            Value::Number(n) => println!("(vm) result: {}", n),
                            Value::Str(s) => println!("(vm) result: {}", s),
                            Value::None => println!("(vm) result: <none>"),
                        }
                    } else {
                        println!("(vm) halted with empty stack");
                    }
                    return Ok(());
                }
            }
        }
        Ok(())
    }

    fn binary_arith<F>(a: Value, b: Value, f: F) -> Result<f64>
    where F: FnOnce(f64, f64) -> f64 {
        let xa = match a {
            Value::Number(n) => n,
            Value::Str(s) => s.parse::<f64>().unwrap_or(0.0),
            Value::None => 0.0,
        };
        let xb = match b {
            Value::Number(n) => n,
            Value::Str(s) => s.parse::<f64>().unwrap_or(0.0),
            Value::None => 0.0,
        };
        Ok(f(xa, xb))
    }
}
