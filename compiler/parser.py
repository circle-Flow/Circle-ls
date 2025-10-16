from typing import List, Any
from .lexer import Token

class Node:
    def __init__(self, type_: str, value: Any = None, children=None):
        self.type = type_
        self.value = value
        self.children = children or []

    def __repr__(self):
        return f"Node({self.type}, {self.value}, {self.children})"


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos]

    def eat(self, type_: str):
        tok = self.peek()
        if tok[0] == type_:
            self.pos += 1
            return tok
        raise SyntaxError(f"Expected {type_}, got {tok}")

    def parse(self):
        nodes = []
        while self.peek()[0] != "EOF":
            nodes.append(self.statement())
        return Node("PROGRAM", children=nodes)

    def statement(self):
        tok_type, tok_val = self.peek()
        if tok_type == "IDENT" and self._lookahead("="):
            return self.assignment()
        elif tok_val == "fn":
            return self.function()
        else:
            return self.expression()

    def assignment(self):
        name = self.eat("IDENT")[1]
        self.eat("ASSIGN")
        expr = self.expression()
        return Node("ASSIGN", name, [expr])

    def expression(self):
        node = self.term()
        while self.peek()[1] in ("+", "-"):
            op = self.eat("OP")[1]
            right = self.term()
            node = Node("BINOP", op, [node, right])
        return node

    def term(self):
        node = self.factor()
        while self.peek()[1] in ("*", "/"):
            op = self.eat("OP")[1]
            right = self.factor()
            node = Node("BINOP", op, [node, right])
        return node

    def factor(self):
        tok_type, tok_val = self.peek()
        if tok_type == "NUMBER":
            self.eat("NUMBER")
            return Node("NUM", float(tok_val))
        elif tok_type == "STRING":
            self.eat("STRING")
            return Node("STR", tok_val.strip('"'))
        elif tok_type == "IDENT":
            self.eat("IDENT")
            return Node("VAR", tok_val)
        elif tok_type == "LPAREN":
            self.eat("LPAREN")
            node = self.expression()
            self.eat("RPAREN")
            return node
        else:
            raise SyntaxError(f"Unexpected token: {tok_type}")

    def _lookahead(self, value):
        if self.pos + 1 < len(self.tokens):
            return self.tokens[self.pos + 1][1] == value
        return False
