def let_num(letter):
    if letter in "ABC":
        return ("2")
    if letter in "DEF":
        return ("3")
    if letter in "GHI":
        return ("4")
    if letter in "JKL":
        return ("5")
    if letter in "MNO":
        return ("6")
    if letter in "PQRS":
        return ("7")
    if letter in "TUV":
        return ("8")
    if letter in "WXYZ":
        return ("9")

def lets_nums(code):
    res = ""
    for x in range(len(code)):
        res = res + let_num(code[x])
    return (res)

def vanity(codes, numbers):
    result = []
    memo = []
    for x in range(len(codes)):
        nums = lets_nums(codes[x])
        for y in range(len(numbers)):
            if nums in numbers[y]:
                if numbers[y] not in memo:
                    result.append(numbers[y])
                memo.append(numbers[y])
    result = sorted(result)
    return (result)
