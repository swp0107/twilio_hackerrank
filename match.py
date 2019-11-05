def match(prefixes, numbers):
    result = []
    for x in range(len(numbers)):
        max_len = 0
        max_index = -1
        for y in range(len(prefixes)):
            if prefixes[y] in numbers[x]:
                tmp_len = len(prefixes[y])
                if tmp_len > max_len:
                    max_len = tmp_len
                    max_index = y
        if max_index >= 0:
            result.append(prefixes[max_index])
        else :
            result.append("")
    return result
