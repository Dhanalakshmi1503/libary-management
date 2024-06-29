n=int(input())
c=ord('a')
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(chr(c+j-1),end=" ")
    for j in range(i-1,0,-1):
        print(chr(c+j-1),end=" ")
    print()
