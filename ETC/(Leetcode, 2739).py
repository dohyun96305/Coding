# https://leetcode.com/problems/total-distance-traveled/
# Total Distance Traveled
# 총 거리 km return, mainTank 5L 마다 additionalTank에서 1L씩 옮긴다

class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """

        dist = 0 # 총 거리수 
        while mainTank : # while 반복문, mainTank = 0이면 종료

            if mainTank < 5 : 
                dist += mainTank*10
                return dist # mainTank 5L 이하면 더하고 종료

            else : 
                mainTank -= 5 
                if additionalTank : # additionalTank에 1L라도 있어야 mainTank로 옮김  
                    mainTank += 1
                    additionalTank -= 1
                
                dist += 50 # 5L * 10km/L

        return dist

# 10km per liter
# 5 liters of main tank used up => 1 liters of additional tank will transferred to main tank
# return maximum km