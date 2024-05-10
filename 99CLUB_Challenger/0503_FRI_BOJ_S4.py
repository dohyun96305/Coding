# ATM 
# https://www.acmicpc.net/problem/11399
# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값 return
# 기다리는 시간이 없도록 

n = int(input())
lis = sorted(list(map(int, input().split())))

sum1 = 0

for i in range(n) : 
    sum1 += (sum(lis[:i+1]))
    
print(sum1)