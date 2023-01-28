n=int(input("enter number of rows"'\n'))
for i in range(n,100):
    for j in range(i+1):
        print(chr(j+65), end=" ")
    print('\r')
if n>100 :
    print(chr(65)*1000)