# 잃어버린 괄호 
# https://www.acmicpc.net/problem/1541
# 식 확인 후 괄호를 통해 식의 값을 최소로 만듬
# '-' 사이의 식을 전부 괄호로 묶음.

n = str(input())
m = n.split('-')

answer = 0
# 첫번째는 -로 시작할 경우의 수가 있어서 따로 작업
x = sum(map(int, (m[0].split('+'))))
if n[0] == '-':
    answer -= x
else:
    answer += x

for x in m[1:]: # 첫번째 작업은 이미 했기때문에 인덱스 1부터 시작
    x = sum(map(int, (x.split('+'))))
    answer -= x
    
print(answer)