def input_string(input):
    """
    Returns the number of different substrings
    :param input: string
    :return: number
    """
    string = input
    sublist = list(string)
    sublistrm = list(set(sublist))
    output = []
    if len(sublistrm) == 1:
        return len(string)
    else:
        # [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
        for i in range(len(sublist)):
            for j in range(len(sublist)):
                if j < len(sublist) - 1 and i < j + 1:
                    output.append(sublist[i] + sublist[j + 1])

    return len(output) + len(sublistrm) + 1


print(input_string("abc"))
