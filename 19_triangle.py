import math
AB=int(input())
BC=int(input())
# a tan inverse keyward atan use 
# chr(176) use for printing degree  
#see hacker rank question math traingle
print(f"{round(math.degrees(math.atan(AB/BC)))}{chr(176)}")
