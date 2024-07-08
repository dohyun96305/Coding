# Maximum Total Importance of Roads
# https://leetcode.com/problems/maximum-total-importance-of-roads/description
# Assign unique integer values from 1 to n to n cities connected by bidirectional roads to maximize the total importance, defined as the sum of values of connected cities, and return this maximum total importance.

class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        answer = 0 # total importacnes
         
        cities = [0] * n # connection time of cities
        imp = [x for x in range(n)] # importance of cities
        values = [0] * n # importance value of cities

        for a, b in roads : # connection time of cities
            cities[a] += 1
            cities[b] += 1

        imp.sort(key = lambda x : -cities[x]) # reverse sorting cities by importance
    
        for a in imp : # importance value of cities
            values[a] = n
            n -= 1

        for a, b in roads : # sum of roads 
            answer += (values[a] + values[b])

        return answer