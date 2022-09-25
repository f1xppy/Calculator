import Calc


def RunApp():
    s = input("Введите выражение: ")
    ans = 0
    sign = ""
    a = 0
    b = 0

    for i in range(0, len(s)):
        if (s[i] >= "0") and (s[i] <= "9"):
            b = b * 10 + int(s[i])
        else:
            sign = s[i]
            a = b
            b = 0
    ans = Calc.Calculate(a, b, sign)
    s = input(str(ans))

    while s != "":
        sign = Calc.GetSign(s)
        a = Calc.GetNumber(s)
        ans = Calc.Calculate(ans, a, sign)
        s = input(str(ans))

    print("Ответ: " + str(ans))
