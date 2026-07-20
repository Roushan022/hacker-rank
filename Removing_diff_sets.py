M = int(input("Enter the number of elements in set A: "))
A = []

for i in range(M):
    A.append(input(f"Enter the value of element {i+1}: "))

N = int(input("Enter the number of elements in set B: "))
B = []

for i in range(N):
    B.append(input(f"Enter the value of element {i+1}: "))

a = set(A)
b = set(B)

print(a.intersection(b))
