brackets={'}':'{',
        "]":"[",
        ")":"("}
    
def isBalanced(s):
    a=list()
    for c in s:
        if a and a[-1]==brackets.get(c):
            a.pop()
        else:
            a.append(c)
    if a:
        return 'NO'
    else:
        return 'YES'