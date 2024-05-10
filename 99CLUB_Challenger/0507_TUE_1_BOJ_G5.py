# Fly me to the Alpha Centauri
# https://www.acmicpc.net/problem/1011
# 특정 거리 특정 조건으로 이동, 최소 이동 횟수 return  

n = int(input())

for i in range(n) :                                  # dp 생성 
    a, b = map(int, input().split())
    dist = b - a
    
    temp = 0
    count = 0
    count_dist = 1

    while temp < dist : 
        count += 1        
        temp += count_dist

        if count % 2 == 0 : 
            count_dist += 1
  
    print(count)

# 01 => 1, 1        

# 02 => 2, 1 0 1    

# 03 => 3, 1 1 1
# 04 => 3, 1 2 1    

# 05 => 4, 1 2 1 1
# 06 => 4, 1 2 2 1  

# 07 => 5, 1 2 2 1 1
# 08 => 5, 1 2 2 2 1 
# 09 => 5, 1 2 3 2 1  

# 10 => 6, 1 2 3 2 1 1 
# 11 => 6, 1 2 3 2 2 1
# 12 => 6, 1 2 3 3 2 1 