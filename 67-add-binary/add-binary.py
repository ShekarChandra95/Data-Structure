class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        s = []
        indA, indB = len(a)-1, len(b)-1
        while indA >=0 or indB >=0 or carry ==1:
            if indA>= 0:
                carry +=int(a[indA])
                indA -= 1
            if indB>=0:
                carry += int(b[indB])
                indB -=1
            
            s.append(str(carry%2))
            carry //= 2

        return "".join(s[::-1])