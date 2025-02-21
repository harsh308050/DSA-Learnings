#Check Frequency of Element
# li=[1,3,4,5,5,6,7,7]
# print(li.count(5))
# freq = {}
# for item in li:
#     freq[item] = freq.get(item, 0) + 1
# print(freq)

# #Dictionay and Convert in Table Form Using Pandas
# d1={1: 2, 2:3, 3:4}
# print(d1)
emp={
    "Employee": {
        "Raj":{"id":1,"Salary":20000, "Post": "Developer"},
        "Ajay":{"id":2,"Salary":10000, "Post": "Manager"},
        "Harsh":{"id":3,"Salary":30000, "Post": "Developer"}
    }
}
# print(emp)
# import pandas as pd
# df= pd.DataFrame(emp["Employee"])
# print(df)
print(emp.items())

print(emp.popitem("Employee"))
