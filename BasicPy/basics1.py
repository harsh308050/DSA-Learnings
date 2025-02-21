print("Hello")
print("My Name is", end=' ')
print("Harsh")
a=10
print(a)
b=10.4
print(b)
print(type(b))
c="A"
print(type(c))
print(a+b)
print(a/b)
print(a//b)
print(a*b)
print(a**b)
print(a and b) #return Second element
print(a or b) #return first element
# print(~ b) #return first element
print(~a)
d=9
print(a ^ d)
comp1=2
comp2=4
print(complex(comp2*comp1,comp1+comp2))
# print(complex(1,comp1+comp2))
l1=[6,2.6,"A",27,"CSE1"]
print(l1)
print(l1[2])
l1[2]=45
print(l1)
l2=[1,5,7,2,3,4]
print(sum(l2))
print(max(l2))
print(min(l2))
print(len(l2))
#difference b/w sort and sorted 
#in sorted it will just show you how the sorted list will be
#in sort it will change the order of element in sorted form but 
print(sorted(l2))
l2.sort()
mul=1
for i in l2:
    mul=i*mul
print(mul)
#difference b/w remove and pop
# pop will take index value of element but 
# remove will take element value  
print(l2.pop())
print(l2.pop(1))
l2.remove(1)
print(l2)
l3=[4,7,1]
print(l2+l3)
l2.append(l3)
print(l2)
print(l2[0:2])
print(l2[::-1])
t1=(1,5,7,2,3,4)
print(t1)
print(type(t1))
t2=(4,7,1)
print(t1+t2)
print(t1[0:2])

l6=[1,5,7,2,3,4]
l4=[]
l5=[]

for j in range(len(l6)):
    if l6[j] % 2 == 0:
        l4.append(l6[j])
    else:
        l5.append(l6[j])
print(l4)
print(l5)
li=[1,3,4,5,5,6,7,7]
print(li.count(5))
freq = {}
for item in li:
    freq[item] = freq.get(item, 0) + 1
print(freq)