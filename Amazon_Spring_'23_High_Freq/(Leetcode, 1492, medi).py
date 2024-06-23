# The kth Factor of n
# https://leetcode.com/problems/the-kth-factor-of-n/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
# Given two positive integers n and k
# return the kth smallest factor of n if it exists, or -1 if n has fewer than k factors.

class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        temp = []
        for i in range(1, int(n**(0.5))+1) : 
            if n%i == 0 : 
                temp.append(i)
                if i != n//i : 
                    temp.append(n//i)

        temp = sorted(temp)

        if len(temp) < k : 
            return -1

        return temp[k-1]




