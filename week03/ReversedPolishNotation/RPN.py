def update_list(index, result, expr):
    expr[index] = result
    del expr[index - 1]
    del expr[index - 2]
    return expr    

def rpn_calculate(expr):
    split_expr = [symbol for symbol in expr.split(' ')]
    operations = ['+', '-', '*', '/']
    
    if len(split_expr) == 1:
        return int(split_expr[0])
    
    while len(split_expr) > 1:
        for index, symbol in enumerate(split_expr):
            if symbol in operations:
                if symbol == '+':
                    result = int(split_expr[index - 2]) + int(split_expr[index - 1])
                    split_expr = update_list(index, result, split_expr)
                    break
                elif symbol == '-':
                    result = int(split_expr[index - 2]) - int(split_expr[index - 1])
                    split_expr = update_list(index, result, split_expr)
                    break
                elif symbol == '*':
                    result = int(split_expr[index - 2]) * int(split_expr[index - 1])
                    split_expr = update_list(index, result, split_expr)
                    break
                elif symbol == '/':
                    result = int(split_expr[index - 2]) / int(split_expr[index - 1])
                    split_expr = update_list(index, result, split_expr)
                    break   
    
    return(int(split_expr[0]))

def main():
    print(rpn_calculate('3 5 8 * 7 + *'))

if __name__ == '__main__':
    main()

