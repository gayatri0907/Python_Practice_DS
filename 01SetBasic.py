country={'england','russia','germany','france','usa','england','germany'}
print(country)
print(type(country))

#a={} creates a dictionary not a set
a=set()
print(type(a))

print(len(country))
print(max(country))
print(min(country))

country.add('italy')
country.remove('russia')
print(country)
#country.clear()
#print(country[0]) 'set' object is not subscriptable
print(country.pop())
print(country)


