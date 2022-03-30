tup=('cricket','football','rugby','tennis','badminton')
print(tup)
print(type(tup))
print(len(tup))
print(max(tup))
print(min(tup))

#tup.append('running')
#tup.remove('rugby')
#tup.sort()
#tup.reverse()
#print(tup.pop())

print(tup[3])
print(tup[2:])

for spo in tup:
    print(spo.title())

mix=('spider',2004,45.23,True)
print(mix)
for val in mix:
    print(type(val))

nest=('ethan','trainer',('london','chelsea'),['java','python'])
print(nest)

nest[3].append('cloud')
nest[3].append('big data')
print(nest)






