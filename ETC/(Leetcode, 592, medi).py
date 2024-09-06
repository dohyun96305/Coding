# Fraction Addition and Subtraction
# https://leetcode.com/problems/fraction-addition-and-subtraction/description
# Given a fraction expression string, return the result as an irreducible fraction, or as an integer with a denominator of 1.


import re

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """ 
        def gcd(a, b):                  # To calculate GCD of the given Fraction
            while b != 0:
                a, b = b, a % b
            
            return abs(a)

        def add1(a_0, a_1, b_0, b_1, symbol):       # Calculation of Two Fraction 
            c_0 = a_0 * b_1 + symbol * a_1 * b_0
            c_1 = a_1 * b_1

            return c_0, c_1

        symbols = list(map(lambda x: -1 if x == '-' else 1, re.findall(r'[-+]', expression))) # Find all the Expression symbols (+, -) in Expression
        nums = re.split(r"[-+]", expression) # Find all the fraction in Expression, If first Fractions is Minus, then nums[0] = ''

        a_0, a_1 = 0, 1 # Initial Value of Fraction (If first Fraction is Minus, Need to Calculate it)
        
        for i, num in enumerate(nums): 
            if num:
                b_0, b_1 = map(int, num.split('/'))
                symbol = symbols[i-1] if i > 0 else 1 # First Fraction also be +, -
                a_0, a_1 = add1(a_0, a_1, b_0, b_1, symbol)

        temp = gcd(a_0, a_1) # To calculate the GCD (최대공약수, Gradient Common Divisor)
        a_0 //= temp
        a_1 //= temp

        return "{}/{}".format(a_0, a_1)