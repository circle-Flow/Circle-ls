import re
from typing import List, Tuple

Token = Tuple[str, str]  # (TYPE, VALUE)

TOKEN_SPEC = [
    ("NUMBER",   r"\d+(\.\d+)?"),
    ("STRING",   r"\".*?\""),
    ("IDENT",    r"[A-Za-z_][A-Za-z0-9_]*"),
    ("ASSIGN",   r"="),
    ("OP",       r"[+\-*/]"),
    ("LPAREN",   r"\("),
    ("RPAREN",   r"\)"),
    ("LBRACE",   r"\{"),
    ("RBRACE",   r"\}"),
    ("COMMA",    r","),
    ("NEWLINE",  r"\n"),
    ("SKIP",     r"[ \t]+"),
    ("MISMATCH", r".")
]

TOKEN_REGEX = re.compile("|".join(f"(?P<{name}>{regex})" for name, regex in TOKEN_SPEC))

def lex(code: str) -> List[Token]:
    tokens = []
    for mo in TOKEN_REGEX.finditer(code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == "NEWLINE" or kind == "SKIP":
            continue
        elif kind == "MISMATCH":
            raise SyntaxError(f"Unexpected character: {value}")
        tokens.append((kind, value))
    tokens.append(("EOF", ""))
    return tokens
