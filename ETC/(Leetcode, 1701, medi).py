# Average Waiting Time 
# https://leetcode.com/problems/average-waiting-time/description/?envType=daily-question&envId=2024-07-09
# Calculate the average waiting time for all customers at a restaurant, where each customer is served in the order they arrive, given their arrival times and the time needed to prepare their orders.

class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        time = customers[0][0] # First start time
        answer = 0.0

        for a, b in customers : 
            if time > a : # If customers need to wait
                answer += (time + b - a) # Waiting time
                
            else : # If customers don't need to wait
                time = a
                answer += b # Only for waiting time

            time += b 

        return answer / len(customers)
        