"""def remove_spaces(x):
    return eval(x.replace(" ", ""))
def spliter(function,subtree):
    name=function[0]
    function=function.split("=")[1]
    ops=["+","-","*","/"]
    for i in ops:
        if i in function:
            oper=i
            vars=function.split(i)
            if vars[0][0] not in "1234567890x":
                subtree.append(vars[0][0])
                var1="recursive(%s)"%[vars[0][0]] 
            else:
                var1=[vars[0]] 
            if vars[1][0] not in "1234567890x":
                subtree.append(vars[1][0])
                var1="recursive(%s)"%[vars[1][0]] 
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
def recursive(tree,forest,calc):
    if tree not in calc:
        calc.append(tree)
        
        
def construct_forest(input):
    forest=creative(input)
    calc=[]#list which take calculated func names  
    for tree in forest:
        recursive(tree,forest,calc)"""

def remove_spaces(x):
    return eval(x.replace(" ", ""))
def spliter(function,subtree):
    name=function[0]
    function=function.split("=")[1]
    ops=["+","-","*","/"]
    for i in ops:
        if i in function:
            oper=i
            vars=function.split(i)
            if vars[0][0] not in "1234567890x":
                subtree.append(vars[0][0])
                var1=vars[0][0] 
            else:
                var1=[vars[0]] 
            if vars[1][0] not in "1234567890x":
                subtree.append(vars[1][0])
                var1=vars[1][0] 
            else:
                var2=[vars[1]]
    return [name,oper,var1,var2]
def creative(input):
    nospace=remove_spaces(str(input))
    forest={}
    subtree=[]
    for i in range(len(nospace)):
        create_dic=spliter(nospace[i],subtree)
        forest[create_dic[0]]=create_dic
    return forest,subtree
def datum(tree):
    return tree[0]
def opera(tree):
    return tree[1]
def left(tree):
    return tree[2]
def right(tree):
    return tree[3]
def recursive(tree,forest):
    #print(forest[tree])
    
    if left(forest[tree])[0][0] not in "1234567890x":
        #print(left(forest[tree]))
        forest[tree]=[datum(forest[tree]),opera(forest[tree]),recursive(left(forest[tree]),forest),right(forest[tree])]
    if right(forest[tree])[0][0] not in "1234567890x":
        forest[tree]=[datum(forest[tree]),opera(forest[tree]),left(forest[tree])], recursive(right(forest[tree]),forest)
    else:
        return forest[tree]
        
def construct_forest(input):
    forest,subtree=creative(input)
    #print(forest,subtree)
    #calc=[]#list which take calculated func names  
    for tree in forest:
        recursive(tree,forest)
    result=[]
    for i in forest:
        if i not in subtree:
            result.append(forest[i])
    return(result)
    
Defs = ["g(x) = x + 20", "h(x) = x * 100", "f(x) = g(x) * x"]
print(construct_forest(Defs))

    



