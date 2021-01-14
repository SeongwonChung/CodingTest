N = int(input())
plans = list(input().split())

cur = [1,1]
for plan in plans:
    if plan =="R" and cur[1]+1 <= N:
        cur[1]+=1
    elif plan == "L" and cur[1]-1 >= 1:
        cur[1]-=1
    elif plan == "U" and cur[0]-1 >= 1:
        cur[0]-=1
    elif plan == "D" and cur[0]+1 <= N:
        cur[0]+=1

print(cur[0], cur[1])