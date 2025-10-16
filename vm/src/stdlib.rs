use std::collections::HashMap;
use anyhow::Result;
use crate::vm::VM;

// A tiny stdlib: currently only placeholder for future host functions.
pub fn make_stdlib() -> HashMap<String, fn(&mut VM) -> Result<()>> {
    let mut m = HashMap::new();
    // Example: "print" could be wired here; for the demo we print stack top in HALT.
    m
}
