# https://leetcode.com/problems/min-stack/description/
# Min stack
# stack 구조, 객체 구조화

# stack : LIFO (Last In First Out)

class MinStack(object):

    def __init__(self):
        self.output = []
        self.min = [] # getmin을 위해 minv 따로 저장

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.minv = min(val, self.min[-1] if self.min else val) # self.minv 확인 

        self.output.append(val) # output 저장
        self.min.append(self.minv) # minval 저장 (min[-1]에는 push 이후 minv 저장)
        
    def pop(self):
        """
        :rtype: None
        """
        self.output.pop()
        self.min.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.output[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()