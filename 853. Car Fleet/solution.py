class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        pairs = []
        stack = []

        #creating pairs of position and speed for each car fleet
        for x in range(len(speed)):
            pairs.append([position[x], speed[x]])

        #sorting the pairs based on position using descending order
        pairs = sorted(pairs)[::-1]

        #iterating throigh sorted pairs
        for p, s in pairs:
            #calculating itme to reach the target from the current car
            time = (target-p) / s

            #adding the time to the stack
            stack.append(time)

            #checking if there are atleast two cars in the stack and current car
            #it takes less or equal time than the previous car if thats the case pop previous car
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        #length of the stack is the num of car fleets
        return len(stack)