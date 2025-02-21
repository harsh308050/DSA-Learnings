operator = []
output = []
precedence = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

exp = input()
exp = exp[::-1]

for ch in exp:
    if ch == ")": 
        operator.append(ch)
    if ch == "(":  
        while operator and operator[-1] != ")":
            ele = operator.pop()
            output.append(ele)
        operator.pop() 
    if ch in precedence:
        while operator and operator[-1] != ")" and precedence[operator[-1]] >= precedence[ch]:
            ele = operator.pop()
            output.append(ele)
        operator.append(ch)
    else:
        output.append(ch)

while operator:
    ele = operator.pop()
    output.append(ele)

output = output[::-1]

print("Infix expression is:", exp[::-1]) 
print("Prefix expression is:", end=" ")
for ch in output:
    print(ch, end=" ")
