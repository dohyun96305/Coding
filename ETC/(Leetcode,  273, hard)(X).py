# Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/description
# Convert a non-negative integer num to its English words representation.

# Recursion

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        Less_than_20 = ["", "One", "Two", "Three", "Four", "Five",  # Setting Less than 20 str 
                            "Six", "Seven", "Eight", "Nine", "Ten", 
                            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", 
                            "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        Tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty",  # Setting Tens str
                "Sixty", "Seventy", "Eighty", "Ninety"]

        Thousands = ["", "Thousand", "Million", "Billion"] # Setting Thousands, Millions, Billon str

        if num == 0 : 
            return "Zero"
        
        def num_to_str(n) : 
            if n == 0 : 
                return ""
            
            elif n < 20 : 
                return Less_than_20[n] + " "

            elif n < 100 : 
                return Tens[n//10] + " " + num_to_str(n%10)
            
            else : 
                return Less_than_20[n//100] + " Hundred " + num_to_str(n%100)

        i = 0
        answer = ""

        while num > 0 :
            if num % 1000 != 0 : 
                answer =  num_to_str(num%1000) + Thousands[i] + " " + answer
                
            num //= 1000
            i += 1

        return answer.strip()


