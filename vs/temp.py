from math import factorial as fact
def nthperm(pos,L):
    sizeL = len(L)
    perm = []
    offset = 0
    i=sizeL-1
    L2 = L
    done = False 
        
    while i>=0:
        for n in range(1,sizeL+1):    
            temp =  (n)*(fact(i))
            #Make sure we find the smallest n such that
            # n(i!)> pos
            if temp+offset >= pos and done is False:
                done = True
                offset += (n-1)*(fact(i))

                perm.append(L2[n-1])
                L2.remove(L2[n-1])
        done = False
        i-=1
        
    return perm 
for i in range(1000000):
    print(nthperm(i,[0,1,2,3,4,5,6,7,8,9]))