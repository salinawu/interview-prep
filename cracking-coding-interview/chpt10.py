def sorted_merge(a, b):
    b_len = len(b) - 1
    full_length = len(a) - 1
    a_len = full_length - len(b)

    while b_len > 0:
        if b[b_len] >= a[a_len]:
            a[full_length] = b[b_len]
            b_len -= 1
        else:
            a[full_length] = a[a_len]
            a_len -= 1
        full_length -= 1
    return a

def group_anagrams(ss):
    table = {}
    for index, i in enumerate(ss):
        sorted_string = ''.join(sorted(i))
        if sorted_string in table:
            table[sorted_string].append(index)
        else:
            table[sorted_string] = [index]
    final = []
    for i in table.values():
        final += [ss[x] for x in i]
    return final

def rotated_array(arr, i):
    if len(arr) == 0:
        return False
    mid = len(arr) / 2
    mid_el = arr[mid]
    if mid_el == i:
        return mid
    elif mid_el>arr[0]:
        return rotated_array(arr[:mid], i)
    elif mid_el<arr[-1]:
        return rotated_array(arr[mid+1:], i)
    elif mid_el==arr[0] and mid_el!=arr[-1]:
        return rotated_array(arr[mid+1:], i)
    else:
        return rotated_array(arr[:mid], i) or rotated_array(arr[mid+1:], i)

def listy(listy, x):
    i = 1
    lower = 0
    while listy[i]:
        if listy[i] == x:
            return i
        elif listy[i] > x:
            return fake_bin_search(listy[lower:i], x)
        lower = i
        i << 1

    i = lower
    while listy[i]:
        if listy[i] == x:
            return i
        i + = 1
    return False

def fake_bin_search(array, i):
    return array.index(i)

def sparse_search(ss, x):
    if len(ss)
    mid = len/2
    mid_el = ss[mid]
    if mid_el == i:
        return mid
    elif mid_el == "":
        left = right = mid
        while left > -1 and right < len(ss):
            left -= 1
            right += 1
            if ss[left] != "":
                mid = left
                break
            elif ss[right] != "":
                mid = right
                break
        if ss[mid] == "":
            return False
    return ss[mid] > x ? sparse_search(ss[:mid], x) : sparse_search(ss[mid+1:], x)

def peaks_valleys(array):
    for i in range(1, len(array), 2):
        lower = i-1
        upper = i+1
        neg_inf = float('-inf')
        max_i = max(array[lower] or neg_inf, array[i], array[upper] or neg_inf)
        print(i)
        if max_i == array[lower]:
            array[lower], array[i] = array[i], array[lower]
        elif max_i == array[upper]:
            array[upper], array[i] = array[i], array[upper]
    return array

def find_in_matrix(matrix, i):
    row = 0
    col = len(matrix[0])
    while row < len(matrix) and col >= 0:
        curr_spot = matrix[row][col]
        if curr_spot == i:
            return True
        elif curr_spot > i:
            col -=1
        else:
            row += 1
    return False

class RankedStream(object):
    def __init__(self, data=None, left=None, right=None, rank=0):
        self.data = data
        self.left = left
        self.right = right
        self.rank = rank

    def insert(self, n):
        if n > self.data:
            self.right.insert(n) if self.right else self.right=RankedStream(n)
        else:
            self.left.insert(n) if self.left else self.left=RankedStream(n)
            self.rank += 1

    def get_rank(self, n):
        if self.data==i:
            return self.rank
        elif self.data >= n:
            return False if not self.data else return self.left.get_rank(n)
        else:
            if not self.right:
                return False
            else:
                right_side = self.right.get_rank(n)
            return False if not right_side else return self.rank + 1 + right_side
