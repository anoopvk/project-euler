# import sys 
 
# sys.setrecursionlimit(10000000)
import time
start=time.time()
def collatz(num,count):
    if num==1:
        return count+1
    elif num%2==0:
        return collatz(num//2,count+1)
    else:
        return collatz((3*num)+1,count+1)
        
maxcount=0
for i in range(1,10000):
    count=collatz(i,0)
    if count>maxcount:
        maxcount=count
#     print(i,"-----",count,"-----",maxcount)
    
    
    

end=time.time()
print(end-start)