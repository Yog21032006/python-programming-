def eval_postfix(expr):
    stack=[]
    for token in expr.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a+b)
            elif token =='-': stack.append(a-b)
            elif token =='*': stack.append(a*b)
            elif token =='/': stack.append(int(a/b))
    return stack[0]
print(eval_postfix("5 2 * 3 +"))