operator=[]
output=[]
precedence={"(":0,"+":1,"-":1,"*":2,"/":2,"^":3}
exp=input()
for ch in exp:
    if ch =="(":
        operator.append(ch)
    if ch== ")":
        while operator and operator[-1] != "(":
            ele = operator.pop()
            output.append(ele)
        operator.pop()
    if ch== "+" or ch== "-" or ch== "*" or ch== "/" or ch== "^":
        while precedence[operator[-1]]>precedence[ch]:
            ele=operator.pop()
            output.append(ele)
        operator.append(ch)
    else:
        output.append(ch)
while (len(operator)):
    ele= operator.pop()
    output.append(ele)
print("infix expression is: ",exp)
print("post expression is: ",end=" ")
for ch in output:
    if ele != "(":
        print(ch,end=" ")
