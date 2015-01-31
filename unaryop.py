import ast

#This function assumes it is NOT in NodeWalker
def visit_UnaryOp(node):
    #Creating a list that represents the string to be outputted
    list = []
    #First, adding the unary operator to the list
    if(type(node.op).__name__ == "UAdd"):
        list.append("+")
    elif(type(node.op).__name__ == "USub"):
        list.append("-")
    elif(type(node.op).__name__ == "Invert"):
        list.append("!")
    elif(type(node.op).__name__ == "Not"):
        list.append("~")
    #Next, add the operand to the list
    if(type(node.operand).__name__ in literals):
        list.append(tokenize(node))
    else:
        list.append(NodeWalker.generic_visit(node))