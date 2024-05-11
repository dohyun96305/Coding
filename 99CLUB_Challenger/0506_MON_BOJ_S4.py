# 동전 0 
# https://www.acmicpc.net/problem/11047
# 가지고 있는 동전 n개, k원을 만들 수 있는 최소 개수

n, k = map(int, input().split())

money = []

for i in range(n) : 
    money.append(int(input()))

money.sort(reverse=True)

answer = 0
for money_temp in money : 
    if money_temp > k : 
        continue
    else : 
        answer += k // money_temp
        k = k % money_temp

    if k == 0 : 
        break

print(answer)