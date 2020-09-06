#Author: Lzj
#mail: harry_lee2683@outlook.com
import numpy as np
A = [91,95,97,99]
B = [92,93,96,98]
c=A.copy()
c.extend(B)
c=sorted(c)
e=[]
avg=np.median(c)
print(avg)
for i in c:
    if i<avg:
        e.append(i)
print(e)
