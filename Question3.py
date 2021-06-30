a = int(input('Please enter your first whole number: '))
b = int(input('Please enter your second whole number: '))
c = int(input('Please enter your third whole number: '))
if a < b and b < c:
    print (a,b,c)
elif b < a and a < c:
    print (b,a,c)
elif c < a and a < b:
    print (c,a,b)
elif b < c and c < a:
    print (b,c,a)
elif c < b and b < a:
    print (c,b,a)
elif a < c and c < b:
    print (a,c,b)
