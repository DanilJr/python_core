number=1357
a=number%10
b=number//10
a1=b%10
b1=b//10
a2=b1%10
b2=b1//10
a3=b2%10
b3=b2//10
mult_number=a*a1*a2*a3
print('1*3*5*7='+ str(mult_number))
reverse=str(a)+str(a1)+str(a2)+str(a3)
print('reversed:'+str(reverse))