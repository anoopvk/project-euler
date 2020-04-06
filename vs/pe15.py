count=0
n=5
def path(i,j):
    global count
    global n
    if i==n and j==n:
        count+=1
        print(count)
    elif i==n:
        path(i,j+1)
    elif j==n:
        path(i+1,j)
    else:
        path(i,j+1)
        path(i+1,j)
path(0,0)
print(count)