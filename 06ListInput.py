nms=[]
choice='yes'

while choice.lower()=='yes':
    n=input('Enter name ')
    if n not in nms:
        nms.append(n)
    choice=input('Do you want to continue? ')
else:
    print(nms)
