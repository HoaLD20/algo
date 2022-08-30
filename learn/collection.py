from collections import Counter, namedtuple


def counter():
    a = "aaaaaaabbbcccc"
    my_counter = Counter(a)
    # print(my_counter.values())
    # print(my_counter.keys())
    # print(my_counter.most_common())
    # print(my_counter.most_common(1))
    # print(my_counter.most_common(1)[0][0])
    print(list(my_counter.elements()))


def name_tuple():
    point = namedtuple('point', 'x,y')
    pt = point(1, -4)
    print(pt.x)

name_tuple()