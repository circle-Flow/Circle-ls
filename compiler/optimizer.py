from .parser import Node

def optimize(ast: Node) -> Node:
    # Constant folding for simple arithmetic
    def fold(node):
        for i, c in enumerate(node.children):
            node.children[i] = fold(c)
        if node.type == "BINOP":
            left, right = node.children
            if left.type == "NUM" and right.type == "NUM":
                if node.value == "+":
                    return Node("NUM", left.value + right.value)
                if node.value == "-":
                    return Node("NUM", left.value - right.value)
                if node.value == "*":
                    return Node("NUM", left.value * right.value)
                if node.value == "/":
                    return Node("NUM", left.value / right.value)
        return node
    return fold(ast)
