import struct
from .parser import Node

# Basic bytecode instructions
OPCODES = {
    "LOAD_CONST": 0x01,
    "STORE_VAR":  0x02,
    "LOAD_VAR":   0x03,
    "ADD":        0x10,
    "SUB":        0x11,
    "MUL":        0x12,
    "DIV":        0x13,
    "HALT":       0xFF
}

def emit_bytecode(ast: Node) -> bytes:
    consts = []
    code = []

    def add_const(value):
        if value not in consts:
            consts.append(value)
        return consts.index(value)

    def gen(node):
        if node.type == "PROGRAM":
            for child in node.children:
                gen(child)
            code.append((OPCODES["HALT"],))
        elif node.type == "ASSIGN":
            gen(node.children[0])
            idx = add_const(node.value)
            code.append((OPCODES["STORE_VAR"], idx))
        elif node.type == "NUM":
            idx = add_const(node.value)
            code.append((OPCODES["LOAD_CONST"], idx))
        elif node.type == "VAR":
            idx = add_const(node.value)
            code.append((OPCODES["LOAD_VAR"], idx))
        elif node.type == "BINOP":
            gen(node.children[0])
            gen(node.children[1])
            if node.value == "+": code.append((OPCODES["ADD"],))
            elif node.value == "-": code.append((OPCODES["SUB"],))
            elif node.value == "*": code.append((OPCODES["MUL"],))
            elif node.value == "/": code.append((OPCODES["DIV"],))

    gen(ast)

    out = bytearray()
    out += b"CRC0"
    out += struct.pack("<H", 1)  # version
    out += struct.pack("<H", len(consts))
    for c in consts:
        if isinstance(c, float):
            out += b"\x01" + struct.pack("<d", c)
        else:
            data = str(c).encode()
            out += b"\x02" + struct.pack("<H", len(data)) + data
    for op in code:
        out += struct.pack("B", op[0])
        if len(op) > 1:
            out += struct.pack("<H", op[1])
    return bytes(out)
