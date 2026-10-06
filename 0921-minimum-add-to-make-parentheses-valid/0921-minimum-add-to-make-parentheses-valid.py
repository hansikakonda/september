class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openn = 0
        closed = 0
        for i in s:
            if i == '(':
                openn += 1
            else:
                if openn > 0:
                    openn -= 1
                else :
                    closed += 1
        return openn + closed
