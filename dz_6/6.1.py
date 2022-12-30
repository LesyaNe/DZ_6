
ln_in = input('Введите выражение: ').split()

print(ln_in)

def aka_eval(args):
    while len(args) != 1:
        while '(' in args or ')' in args:
            try:
                bracket1_index = args.index('(')
            except:
                bracket1_index = 100
            try:
                bracket2_index = args.index(')')
            except:
                bracket2_index = 100

            if bracket1_index < bracket2_index:
                args[bracket1_index - 1] = int(args[bracket1_index - 1]) + int(args[bracket1_index + 1])
                args.pop(bracket1_index + 1)
                args.pop(bracket1_index)
            else:
                args[bracket2_index - 1] = int(args[bracket2_index - 1]) - int(args[bracket2_index + 1])
                args.pop(bracket2_index + 1)
                args.pop(bracket2_index)
        while '*' in args or '/' in args:
            try:
                prod_index = args.index('*')
            except:
                prod_index = 100
            try:
                div_index = args.index('/')
            except:
                div_index = 100

            if prod_index < div_index:
                args[prod_index - 1] = int(args[prod_index - 1]) * int(args[prod_index + 1])
                args.pop(prod_index + 1)
                args.pop(prod_index)
            else:
                args[div_index - 1] = int(args[div_index - 1]) / int(args[div_index + 1])
                args.pop(div_index + 1)
                args.pop(div_index)
        while '+' in args or '-' in args:
            try:
                sum_index = args.index('+')
            except:
                sum_index = 100
            try:
                deg_index = args.index('-')
            except:
                deg_index = 100

            if sum_index < deg_index:
                args[sum_index - 1] = int(args[sum_index - 1]) + int(args[sum_index + 1])
                args.pop(sum_index + 1)
                args.pop(sum_index)
            else:
                args[deg_index - 1] = int(args[deg_index - 1]) - int(args[deg_index + 1])
                args.pop(deg_index + 1)
                args.pop(deg_index)

    print(args[0])


aka_eval(ln_in)