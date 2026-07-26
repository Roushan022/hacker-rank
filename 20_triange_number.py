# 1
# 121
# 12321
# 1234321
# 123454321
for i in range(1, 6):
    print(''.join(str(j) for j in range(1, i + 1)) + ''.join(str(j) for j in range(i - 1, 0, -1)))
  
