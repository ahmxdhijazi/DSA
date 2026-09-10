class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[pos,spd] for pos, spd in zip(position, speed)]
        stack = [] #results

        #Pair looks like [(pos, speed), (pos, speed)..... length n]
        #So now we have an array with tuples of the position and speeds

        #Sort them by the first index and go through it in reverse
        for pos, spd in sorted(pair)[::-1]:
            stack.append((target-pos)/spd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
