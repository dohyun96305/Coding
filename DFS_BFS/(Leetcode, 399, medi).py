# https://leetcode.com/problems/evaluate-division/description
# Evaluate Division
# equation => a, b, values = a / b, queries => b, a, b/a값 return, 값을 구할 수 없으면 -1.0 return 

from collections import defaultdict, deque

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]    equations = [["a","b"],["b","c"]]
        :type values: List[float]           values = [2.0,3.0]
        :type queries: List[List[str]]      queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        :rtype: List[float]                 [6.00000,0.50000,-1.00000,1.00000,-1.00000]
        """

        def BFS(start, end) : # BFS 함수 
            q = deque()
            q.append((start, 1))    # start, 계산값
            temp = set()            # visited list (set)

            while q : 
                for _ in range(len(q)) : 
                    node, res = q.popleft() # 
                    if node == end : 
                        return res
                    temp.add(node) # visited 추가

                    for n in graph[node] : 
                        if n not in temp : 
                            q.append((n, res*graph[node][n]))

            return -1.0
        
        graph = defaultdict(dict) # BFS value를 위한 dict 생성

        for (str1, str2), val in zip(equations, values) : 
            graph[str1][str1] = graph[str2][str2] = 1.0     # a/a = 1
            graph[str1][str2] = val                         # a/b = val
            graph[str2][str1] = 1 / val                     # b/a = 1/val

        answer = []

        for a, b in queries : 
            if a not in graph or b not in graph : 
                answer.append(-1.0)
            elif a == b : 
                answer.append(1.0)
            else : 
                answer.append(BFS(a, b))

        return answer