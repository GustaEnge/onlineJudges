# -*- coding: utf-8 -*-
def check_triangle(args):
    cond_three = False
    triangle = "N"
    a=b=c=0
    while not cond_three:
        args.sort(reverse=True)
        highest = args[0]
        args.remove(highest)
        if len(args) >= 2:
            b,c = int(args[0]), int(args[1])
            a = highest
            if b+c>a :
                triangle = "S"
                cond_three = True
        else:
            cond_three = True
    return triangle

list_args = list(map(int,input().split(" ")))
print(check_triangle(list_args))