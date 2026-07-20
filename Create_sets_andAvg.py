def average(array):
    sets=set(array)  # convert array into sets
    total=0
    for i in sets:
         total+=i
    return total/len(sets)    # calculate the avg
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))  # takes input as a string then convert it into integer and then list
    result = average(arr)
    print(result)
