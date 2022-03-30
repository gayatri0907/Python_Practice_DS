dic={}.fromkeys(['soham','rishit','praffull','sharayu'],0)
print(dic)

dic['praffull']+=1
print(dic)

dic['sharayu']-=1
print(dic)

lst='you will never walk alone'.split(' ')
print(lst)

dicwords={}.fromkeys(lst,1)
print(dicwords)

word=None

while word!='stop':
    word=input('Enter a word : ')
    if word in dicwords:
        dicwords[word]+=1
    else:
        dicwords[word]=1

print(dicwords)

