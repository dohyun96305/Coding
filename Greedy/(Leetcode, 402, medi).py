# Remove K Digits
# https://leetcode.com/problems/remove-k-digits/description/?envType=daily-question&envId=2024-06-30
# Remove k digits from num to make smallest integer

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        temp = []
        answer = "" # return str

        for num1 in num :
            while k > 0 and temp and temp[-1] > num1 : # 현재 숫자와 비교, 원래 자릿수 유지 및 가장 작은 수가 최대한 앞에 올 수 있도록 
                temp.pop()
                k -= 1 # 제거할 경우 k -= 1
            temp.append(c) # 현재 숫자 append, 자릿수 유지 

        while k > 0 : # K가 남았을 경우 추가로 pop
            temp.pop()
            k -= 1

        for num1 in temp : 
            if not answer and c == '0': # 처음에 오는 num1이 0일 경우 continue
                continue
            answer += num1

        return answer if answer else '0'