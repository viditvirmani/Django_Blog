li =[1,2,4,5,6,7,7,7,8,9]
def even_max(li):
    global_max=0
    cnt=0
    for i in li:
        if(i%2!=0):
            cnt=0
        else:
            cnt=cnt+1
            global_max=max(global_max,cnt)
    return global_max
