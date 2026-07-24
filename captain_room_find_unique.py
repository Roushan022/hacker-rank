k=int(input())
n=list(map(int,input().split()))
#it will find the unique from a given repeted number 
print((sum(set(n))*k-sum(n)) //(k-1)     

#if the number are repeated twice then 
      result=0
for i in nums:
  result^=i  #XOR operation

print(result)
