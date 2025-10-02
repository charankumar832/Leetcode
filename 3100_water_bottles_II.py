class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:

        emptyBottles=numBottles
        total=numBottles
        
        while emptyBottles>=numExchange:
            
            total+=1
            emptyBottles-=numExchange
            numExchange+=1
            emptyBottles+=1 

        return total