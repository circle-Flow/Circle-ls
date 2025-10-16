use anyhow::{Result, bail};
use byteorder::{LittleEndian, ReadBytesExt};
use std::io::Cursor;
use std::collections::HashMap;

#[derive(Debug, Clone)]
pub enum Constant {
    Number(f64),
    Str(String),
}

#[derive(Debug, Clone)]
pub enum Instr {
    LoadConst(u16),
    StoreVar(u16),
    LoadVar(u16),
    Add,
    Sub,
    Mul,
    Div,
    Halt,
    // future: Call, Return, etc.
}

#[derive(Debug)]
pub struct Bytecode {
    pub version: u16,
    pub consts: Vec<Constant>,
    pub code: Vec<Instr>,
}

impl Bytecode {
    pub fn from_bytes(bytes: &[u8]) -> Result<Self> {
        let mut cursor = Cursor::new(bytes);
        // header: 4 bytes "CRC0"
        let mut magic = [0u8; 4];
        cursor.read_exact(&mut magic)?;
        if &magic != b"CRC0" {
            bail!("invalid header");
        }
        let version = cursor.read_u16::<LittleEndian>()?;
        let const_count = cursor.read_u16::<LittleEndian>()?;
        let mut consts = Vec::with_capacity(const_count as usize);
        for _ in 0..const_count {
            let tag = cursor.read_u8()?;
            match tag {
                0x01 => {
                    // float
                    let v = cursor.read_f64::<LittleEndian>()?;
                    consts.push(Constant::Number(v));
                }
                0x02 => {
                    // string (u16 len)
                    let len = cursor.read_u16::<LittleEndian>()?;
                    let mut buf = vec![0u8; len as usize];
                    cursor.read_exact(&mut buf)?;
                    let s = String::from_utf8(buf)?;
                    consts.push(Constant::Str(s));
                }
                other => bail!("unknown const tag: {}", other),
            }
        }
        // rest are instructions
        let mut code = Vec::new();
        while (cursor.position() as usize) < bytes.len() {
            let op = cursor.read_u8()?;
            match op {
                0x01 => {
                    let idx = cursor.read_u16::<LittleEndian>()?;
                    code.push(Instr::LoadConst(idx));
                }
                0x02 => {
                    let idx = cursor.read_u16::<LittleEndian>()?;
                    code.push(Instr::StoreVar(idx));
                }
                0x03 => {
                    let idx = cursor.read_u16::<LittleEndian>()?;
                    code.push(Instr::LoadVar(idx));
                }
                0x10 => code.push(Instr::Add),
                0x11 => code.push(Instr::Sub),
                0x12 => code.push(Instr::Mul),
                0x13 => code.push(Instr::Div),
                0xFF => {
                    code.push(Instr::Halt);
                    break;
                }
                other => bail!("unknown opcode: 0x{:02x}", other),
            }
        }
        Ok(Bytecode { version, consts, code })
    }

    pub fn const_as_number(&self, idx: usize) -> Option<f64> {
        match self.consts.get(idx) {
            Some(Constant::Number(v)) => Some(*v),
            _ => None,
        }
    }

    pub fn const_as_str(&self, idx: usize) -> Option<&str> {
        match self.consts.get(idx) {
            Some(Constant::Str(s)) => Some(s.as_str()),
            _ => None,
        }
    }
}
