class Solution:
    def calPoints(self, operations: List[str]) -> int:
        final = []
        for i, char in enumerate(operations):
            if char == '+':
                add = final[-2] + final[-1]
                final.append(add)
            elif char == 'D':
                double = final[-1] * 2
                final.append(double)
            elif char == 'C':
                final.pop()
            else:
                final.append(int(char))
        
        return sum(final)
