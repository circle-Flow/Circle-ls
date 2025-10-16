// Minimal GC stub - currently no-op. Placeholder for future allocators and memory management.

pub struct GC {}

impl GC {
    pub fn new() -> Self { GC {} }
    pub fn collect(&self) { /* no-op for now */ }
}
