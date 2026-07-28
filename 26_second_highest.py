n=int(input())
arr=list(set(map(int,input().split())))
arr.sort() 
print(arr[-2])

#input 5
#2 3 5 6 6
#second highest is 5 so , set is used to remove dublicate and list is use to sort 
