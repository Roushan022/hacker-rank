import random
import string
#code 
code=input("ENter a string ;- ")
#if strign length is less then 3
if len(code)<3:
    msg="".join(reversed(code))
else: 
    new_code=code[1:]+code[0] #take the 0 index and add to the last  then genrate three random number in front and back
    msg="".join(random.choices(string.ascii_lowercase, k=3))+new_code+"".join(random.choices(string.ascii_lowercase, k=3))
print(msg)

#Decodes
if len(msg)<3:
    decode="".join(reversed(msg))
step_1=msg[3:-3]
step_2=step_1[-1]
step_3=step_2+step_1[:-1]
decode=step_3
print(decode)
    
