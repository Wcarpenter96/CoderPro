class Solution:

    def calculate(self, s: str) -> int:
        return self.eval(s,0)[0]

    def eval(self,s,i):
        op = '+'
        res = 0
        while i < len(s):
            char = s[i]
            if char in ('+','-'):
                op = char
            else:
                val = 0
                if char.isdigit():
                    val = int(char)
                elif char == '(':
                    (val, i) = self.eval(s, i+1)
                if op == '+':
                    res += val
                if op == '-':
                    res -= val 
            i += 1
        return (res, i)



print(Solution().calculate('4-5+6'))
