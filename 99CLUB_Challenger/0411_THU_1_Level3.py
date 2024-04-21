# 섬 연결하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/42861
# 크루스칼 알고리즘
# 모든 섬이 연결될 때 필요한 최소 비용 확인
# 가장 작은 비용부터 연결, 전체가 연결된다면 전체 비용 return

def find_parent(parent, x) : 
    if parent[x] != x : 
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y) :
    x = find_parent(parent, x)
    y = find_parent(parent, y) 
    
    if x < y : 
        parent[y] = x
    else : 
        parent[x] = y
    
def solution(n, costs): # n 섬 개수 , cost 연결된 섬에 대한 비용
    answer = 0
    number = 0
    parent = [i for i in range(0, n)] # 동일 집합 여부 확인
    
    costs.sort(key = lambda x : (x[2])) # 비용 낮은 간선부터 확인 
    
    for a, b, c in costs : 
        if find_parent(parent, a) != find_parent(parent, b) : 
            union(parent, a, b)
            number += 1
            answer += c
    
    return answer if number == (n - 1) else -1