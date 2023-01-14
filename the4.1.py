def remove_spaces(x):
    return eval(x.replace(" ", ""))
def spliter(function):
    name=function[0]
    function=function.split("=")[1]
    ops=["+","-","*","/"]
    for i in ops:
        if i in function:
            oper=i
            vars=function.split(i)
            if vars[0][0] not in "1234567890x":
                var1=[vars[0][0]] 
            else:
                var1=[vars[0]] 
            if vars[1][0] not in "1234567890x":
                var2=[vars[1][0]] 
            else:
                var2=[vars[1]]
    return [name,oper,var1,var2]
def creative(input):
    nospace=remove_spaces(str(input))
    forest={}
    for i in range(len(nospace)):
        create_dic=spliter(nospace[i])
        forest[create_dic[0]]=create_dic
    return forest
def datum(tree):
    return tree[0,1]
def left(tree):
    return tree[2]
def right(tree):
    return tree[3]
def construct_forest(input):
    forest=creative(input)
    



