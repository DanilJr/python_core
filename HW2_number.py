number=input('Please, enter your four-digit number:')
lenght=len(number)
if lenght!=4:
    print('Your number should be four-digit (for example"1234")')
else:
    a=int(number)%10
    b=int(number)//10
    a1=b%10
    b1=b//10
    a2=b1%10
    b2=b1//10
    a3=b2%10
    b3=b2//10
    print('multiply:'+str(a3*a2*a1*a))
    print('reverse number is:'+str(a)+str(a1)+str(a2)+str(a3))
    print('sort:'+str(sorted([a, a1, a2, a3])))
