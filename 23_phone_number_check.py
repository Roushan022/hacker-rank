N = int(input())
for i in range(N):
    K = input().strip()
   if K.isdigit() and len(K) == 10 and K[0] in "789": # check all the criteria
        print("YES")
    else:
        print("NO")
