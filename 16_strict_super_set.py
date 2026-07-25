A=set(map(int,input().split()))
n=int(input())
ans=True
for i in range(n):
    N=set(map(int,input().split()))
    if not A.issuperset(N):   # check if it is not super set
        ans=False
    elif A==N:                # check if all item are set
        ans=False
print(ans)
      
