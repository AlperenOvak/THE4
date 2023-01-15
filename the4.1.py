def remove_spaces(x):
    return eval(x.replace(" ", ""))
def spliter(function,subtree):
    name=function[0]
    function=function.split("=")[1]
    ops=["+","-","*","^"]
    for i in ops:
        if i in function:
            oper=i
            vars=function.split(i)
            if vars[0][0] not in "1234567890x":
                subtree.append(vars[0][0])
            if vars[1][0] not in "1234567890x":
                subtree.append(vars[1][0])
            var1,var2=[vars[0]],[vars[1]]
    return [name,oper,var1,var2]
def creative(input):
    nospace=remove_spaces(str(input))
    forest={}
    subtree=[]
    for i in range(len(nospace)):
        create_dic=spliter(nospace[i],subtree)
        forest[create_dic[0]]=create_dic
    return forest,subtree
def datum(tree):return tree[0]   
def opera(tree):return tree[1]   
def left(tree):return tree[2]   
def right(tree):return tree[3]    
def recursive(tree,forest):
    if left(forest[tree])[0][0] not in "1234567890x" and len(left(forest[tree]))==1 and right(forest[tree])[0][0] not in "1234567890x" and len(left(forest[tree]))==1:
        forest[tree]=[datum(forest[tree]),opera(forest[tree]),recursive(left(forest[tree])[0][0],forest),recursive(right(forest[tree])[0][0],forest)]
    if left(forest[tree])[0][0] not in "1234567890x" and len(left(forest[tree]))==1:
        forest[tree]=[datum(forest[tree]),opera(forest[tree]),recursive(left(forest[tree])[0][0],forest),right(forest[tree])]
    if right(forest[tree])[0][0] not in "1234567890x" and len(right(forest[tree]))==1:
        forest[tree]=[datum(forest[tree]),opera(forest[tree]),left(forest[tree]),recursive(right(forest[tree])[0][0],forest)] 
    return forest[tree]

def construct_forest(input):
    forest,subtree=creative(input)
    result=[]
    for i in forest:
        if i not in subtree:
            recursive(i,forest)
            result.append(forest[i])
    return(result)
    
#Defs = ["g(x) = j(x) +k(x) ", "h(x) = x * 100","j(x)=x-500","k(x)=x+h(x)"]
#Defs=["   a    ( x )    = x+       230","b(x) = x-a(x)","c(x)= 15^x","d(x)= c(x)-b(x)","e(x)=d(x)-x","f(x)=9*x","g(x)=59^f(x)","m(x)=g(x)+e(x)"]
"""Defs=["g(x) =h(x)+f(x)", 
      "h(x) = x * 100", 
      "f(x) = 20 * x",
      "n(x)=g(x)+10",
      "v(x)=x+20",
      "o(x)=v(x)+n(x)",
      "u(x)=12^x",
      "y(x)=u(x)+10",
      "j(x)=10+x",
      "p(x)=x*29",
      "l(x)=j(x)*p(x)",
      "b(x)=x*7",
      "d(x)=x*123",
      "s(x)=x^21",
      "a(x)=d(x)+s(x)",
      "z(x)=o(x)^a(x)"]"""
#print(construct_forest(Defs))

    


