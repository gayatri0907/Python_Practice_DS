soft={'microsoft','eclipse','apple','apache','oracle','google','vmware'}
hard={'samsung','hp','dell','microsoft','ibm','apple','lenovo'}

print('UNION-all from both sets')
#res=soft.union(hard)
res=soft | hard
print(res)

print('INTERSECTION- common from both sets')
#res=soft.intersection(hard)
res=soft & hard
print(res)

print('DIFFERENCE- values from first but not in second')
#res=soft.difference(hard)
res=soft - hard
print(res)

print('SYMMETRIC DIFFERENCE- all from both except common')
#res=soft.symmetric_difference(hard)
res=soft ^ hard
print(res)

print('set operations with lists')
cri=['england','india','australia','pakistan','bangladesh']
foo=['germany','france','england','italy']

res=set(cri).intersection(foo)
print(res)

