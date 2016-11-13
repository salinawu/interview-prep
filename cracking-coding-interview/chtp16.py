def swap_nums(a, b):
    a -= b
    b += a
    a = b-a

def swap_nums_bits(a, b):
    a ^= b
    b ^= a
    a ^= b

def intersection(l1, l2):
    slope_1 = (l1.start.y - l1.end.y)/(l1.start.x - l1.end.x)
    slope_2 = (l2.start.y - l2.end.y)/(l2.start.x - l2.end.x)
    return False if slope_1 == slope_2

    y_int_1 = l1.start.y - slope_1*l1.start.x
    y_int_2 = l2.start.y - slope_2*l2.start.x

    x = (y_int_2 - y_int_1)/(slope_1 + slope_2)
    y = slope_1 * x + y_int_1
    intersection = Point(x, y)
    return is_between(l1.start, intersection, l1.end) && is_between(l2.start, intersection, l2.end)

def is_between(start, middle, end):
    return (start.x < middle.x < end.x) && (start.y < middle.y < end.y)
