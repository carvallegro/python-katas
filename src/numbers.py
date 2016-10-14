def multiples(limit):
    if limit is None or limit == 0:
        return 0

    result = 0;
    for i in range(0, limit):
        if i % 3 == 0:
            result += i
        elif i % 5 == 0:
            result += i
    return result

