def remove_spaces(x):
    return x.replace(" ", "")

def split_by_operator(string):
    # Initialize the operator variable to None
    operator = None

    # Check if each operator is in the string
    if "+" in string:
        # If + is in the string, set the operator to +
        operator = "+"
    elif "-" in string:
        # If - is in the string, set the operator to -
        operator = "-"
    elif "*" in string:
        # If * is in the string, set the operator to *
        operator = "*"
    elif "/" in string:
        # If / is in the string, set the operator to /
        operator = "/"

    # If an operator was found, split the string around it
    if operator:
        split_string = string.split(operator)
        return split_string, operator
    # If no operator was found, return the original string and None for the operator
    else:
        return [string], None

def ev_al(g):
    g1=eval(g) #evaluate after all euqation
    g+="1"
    return g1,g