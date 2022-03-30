dic={
    'os':'microsoft',
    'database':'oracle',
    'cloud':'amazon',
    'car':'volkswagen',
    'laptop':'hp',
    'mobile':'samsung'
}

key=input('Enter key : ')

if key in dic:
    print(dic[key])
else:
    print('not found')
    val=input('Enter brand : ')
    dic[key]=val
    print(dic)

