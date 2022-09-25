def ManeExceptionHandling(s):
    if (s[0] != "+") and (s[0] != "-") and (s[0] != "*") and (s[0] != "/") or ((s[1] < "0") or (s[1] > "9")):
        print("Ошибка")
        return 0
    else:
        return 1


def StartExceptionHandling(s):
    k1 = 0
    k2 = 0
    for i in range(0, len(s)):
        if (s[i] >= "0") and (s[i] <= "9"):
            k1 += 1
        else:
            k2 += 1
    if (len(s) - k1 != 1) or (k2 != 1):
        print("Ошибка")
        return 0
    else:
        return 1
