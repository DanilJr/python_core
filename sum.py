def solution(number):
    a=[]
    k=0
    l=0
    while number>k:
        a+=[k]
        k+=3
    while number>l:
        a+=[l]
        l+=5
    return sum(set(a))        