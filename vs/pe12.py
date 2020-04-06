import math
def trianglenumber(num):
    return (num*(num+1))//2



def factors(num):
    count=0
    for i in range(1,math.floor(math.sqrt(num+1))):
        if num%i==0:
            count+=1
    return count*2


flag=1
i=1
maxcount=0
while(flag):
    trnum=trianglenumber(i)
    count=factors(trnum)
    if count>maxcount:
        maxcount=count
    print(i ,"------",trnum ,"------",count,"------",maxcount)

    if count>500:
        flag=0
    i+=1
print(trnum)
