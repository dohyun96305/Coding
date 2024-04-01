# 이중우선순위 큐
# https://school.programmers.co.kr/learn/courses/30/lessons/42628
# heapq 이용, maxheap, minheap 사용
# 기존 배열 문제로 풀었으나 heap 예제 확인
# https://johnyejin.tistory.com/135

import heapq

def changeHeap(heap): # minheap, maxheap 변동에 따른 동기화
    h = []
    for num in heap:
        heapq.heappush(h, -num)
    return h

def solution(operations):
    answer = []  # [최댓값, 최솟값]
    minheap = [] # num에 대해 최솟값으로 저장
    maxheap = [] # num에 대해 최댓값으로 저장 

    for oper in operations:
        command, num = oper.split(' ')
        num = int(num)
        if command == 'I':
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, -num)
        elif command == 'D':
            try:
                if num == 1: # maxheap 삭제 및 동기화
                    heapq.heappop(maxheap)
                    minheap = changeHeap(maxheap)
                else: # minheap 삭제 및 동기화
                    heapq.heappop(minheap)
                    maxheap = changeHeap(minheap)
            except:
                continue

    if len(maxheap) != 0:
        answer.append(-maxheap[0])
    else:
        answer.append(0)

    if len(minheap) != 0:
        answer.append(minheap[0])
    else:
        answer.append(0)

    return answer

# heapq.nlargest( n, heaplist )
# heaplist 내 n개의 최댓값 list return
# heapq.heappop( heaplist ) 
# 최솟값 return

'''

def solution(operations):
    h = []

    for i in operations:
        a, b = i.split()
        if a == 'I':
            heapq.heappush(h, int(b))
        else:
            if len(h) > 0:
                if b == '1':
                    h.pop(h.index(heapq.nlargest(1, h)[0]))
                else:
                    heapq.heappop(h)

    if len(h) == 0:
        return [0, 0]
    else:
        return [heapq.nlargest(1, h)[0], h[0]]
        
'''