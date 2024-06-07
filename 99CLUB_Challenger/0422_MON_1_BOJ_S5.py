# 영화감독 숌 
# https://www.acmicpc.net/problem/1436
# 자연수 내 특정 숫자 포함 여부 확인 

n = 665
count = 0
k = int(input())

while True : 
    n += 1
    if '666' in str(n) : 
        count += 1
        if count == k : 
            print(n)
            break

    
    
    