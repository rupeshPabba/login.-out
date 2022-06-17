#import os 
import re
#os.system=("cls")
txt="the walls of the chambers of the heart are made up of muscles"
txt2="used water is waste water, waste water could be reused"


x=re.findall("water",txt2)
#print(x)

k=re.search("^the",txt)
#print(k)
#if k:
 #   print("the line starts with the")
#else:
 #   print("the line does not end start with the")

r=re.split(",",txt2)
#print(r)

m=re.sub("water","ice",txt2)
print(m)