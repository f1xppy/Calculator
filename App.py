import Calc
import ExceptionHandler as EH


def RunApp():
    ch = 0
    while ch != 1:
        s = input("Введите выражение: ")
        if s != "":
            ch = EH.StartExceptionHandling(s)
        else:
            ch = 1
    ch = 0

    ans1 = Calc.Calculate(0, 0, "")
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
    if ans == ans1:
        ans = "0"
    else:
        while ch != 1:
            s = input(str(ans))
            if s != "":
                ch = EH.ManeExceptionHandling(s)
            else:
                ch = 1

        while s != "":
            ch = 0
            sign = Calc.GetSign(s)
            a = Calc.GetNumber(s)
            ans = Calc.Calculate(ans, a, sign)
            while ch != 1:
                s = input(str(ans))
                if s != "":
                    ch = EH.ManeExceptionHandling(s)
                else:
                    ch = 1

    print("Ответ: " + str(ans))
