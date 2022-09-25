def GetSign(s):
    for i in range(0, len(s)):
        if (s[i] < "0") or (s[i] > "9"):
            return (s[i])


def GetNumber(s):
    b = 0
    for i in range(0, len(s)):
        if (s[i] >= "0") and (s[i] <= "9"):
            b = b * 10 + int(s[i])
    return (b)


def Calculate(a, b, sign):
    if sign == "+":
        return (a + b)
    if sign == "-":
        return (a - b)
    if sign == "*":
        return (a * b)
    if sign == "/":
        return (a / b)
