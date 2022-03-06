tbl=[]

no=int(input('Enter a number '))

for i in range(1,11):
    tbl.append(no*i)

print(tbl)

print('-'*30)
emp='263,emily blunt,development,programmer,london,45700,eb@outlook.com'
lst=emp.split(',')
print(lst)


print('-'*30)

vals=[x**2 for x in range(41,51)]
print(vals)
