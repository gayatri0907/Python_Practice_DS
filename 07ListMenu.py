countries=[]
cho=None

while cho!=6:
    print("1.Add country")
    print("2.Remove country")
    print("3.Clear list")
    print("4.Display countries")
    print("5.Sort list")
    print("6.Exit")
    cho=int(input('Enter choice : '))
    if cho==1:
        c=input('Enter country ')
        countries.append(c)
    elif cho==2:
        c=input('Enter country to remove ')
        countries.remove(c)
    elif cho==3:
        countries.clear()
    elif cho==4:
        print(countries)
    elif cho==5:
        countries.sort()
        print(countries)
    elif cho==6:
        print('thanks')
    else:
        print('invalid choice')
else:
    print(countries)