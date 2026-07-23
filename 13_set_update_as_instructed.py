n=int(input())
A=set(map(int,input().split()))
m=int(input())
for i in range(m):
    operation,size=input().split()
    other = set(map(int, input().split()))  
    if operation == "intersection_update":
        A.intersection_update(other)
    elif operation == "update":
        A.update(other)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other)
    elif operation == "difference_update":
        A.difference_update(other)
print(sum(A))
    
