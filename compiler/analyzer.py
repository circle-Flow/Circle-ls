from .parser import Node

def analyze(ast: Node):
    # Basic semantic check
    defined_vars = set()
    def visit(node):
        if node.type == "ASSIGN":
            defined_vars.add(node.value)
            visit(node.children[0])
        elif node.type == "VAR":
            if node.value not in defined_vars:
                raise NameError(f"Undefined variable: {node.value}")
        for child in node.children:
            visit(child)
    visit(ast)
