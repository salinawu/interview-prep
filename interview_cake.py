# stock_prices_yesterday: max profits from one buy and one sell
def get_max_profit(prices):
    if len(prices) < 2:
        return 0
    curr_min = prices[0]
    max_profit = float('-inf')
    for i in prices[1:]:
        max_profit = max(max_profit, i-curr_min)
        curr_min = min(curr_min, i)
    return max_profit

#print get_max_profit([10, 7, 5, 8, 11, 9])

# Write a function get_products_of_all_ints_except_at_index() that takes
# a list of integers and returns a list of the products.
def product_except_index(ids):
    forward = []
    backward = []
    for i in range(len(ids)):
        forward.append([ids[s] for s in range(len(ids)) if s < i])
        backward.append([ids[s] for s in range(len(ids)) if s > i])
    forward[0].append(1)
    backward[-1].append(1)

    answer = []
    for index in range(len(ids)):
        first = reduce(lambda x, y: x * y, forward[index], 1)
        second = reduce(lambda x, y: x * y, backward[index], 1)
        answer.append(first * second)
    return answer

# print product_except_index([1, 7, 3, 4])

def insert(ints, n, dir):
    ints.append(n)
    ints.sort()
    #print ints
    ints.pop() if dir=='D' else ints.pop(0)
    return ints

#find the highest_product you can get from three of the integers
def highest_product(ints):
    # 2 lowest, 3 highest
    if len(ints) <3:
        return None

    lowest = []
    highest = []

    for i in ints:
        if len(lowest) < 2:
            lowest.append(i)
            lowest.sort()
        else:
            if i< lowest[-1]:
                lowest = insert(lowest, i, 'D')
        if len(highest) < 3:
            highest.append(i)
            highest.sort()
        else:
            if i>highest[0]:
                highest = insert(highest, i, 'U')
    return max(lowest[0]*lowest[1]*highest[2], highest[0]*highest[1]*highest[2])

#print highest_product([3, 2, 5, 6, 2, 1])
#print insert([3, 2, 5], 4, 'D')

def merge_meeting_times(intervals):
    final_list = []
    intervals.sort(key=lambda x: x[0])
    for i in intervals:
        if not final_list:
            final_list.append(i)
        else:
            if final_list[-1][1] > i[0]:
                final_list[-1][1] = max(i[1], final_list[-1][1])
            else:
                final_list.append(i)
    return final_list

#print merge_meeting_times([[1, 3], [4, 6], [5, 9], [10, 11]])

def denominations(denoms, n):
    index = len(denoms)
    table = [[0 for i in denoms] for j in range(n+1)]
    for i in range(n+1):
        for j in range(index):
            if i==0:
                table[i][j] = 1
            else:
                with_m = table[i - denoms[j]][j] if i-denoms[j]>=0 else 0
                without_m = table[i][j-1] if j>=1 else 0
                table[i][j] = with_m + without_m
    return table[n][index-1]

#print denominations([2, 5, 3, 6], 10)

class Rectangle(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def right_x(self):
        return self.x + self.w

    def up_y(self):
        return self.y + self.h

    def intersection(self, other):
        min_x = self if self.x < other.x else other
        other_x = self if min_x!= self else other
        if min_x.right_x() < other_x.x:
            return False

        min_y = self if self.y < other.y else other
        other_y = self if min_y!= self else other
        if min_y.up_y() < other.y:
            return False

        x = min(self.right_x(), other.right_x())
        y = min(self.up_y(), other.up_y())
        return Rectangle(other_x.x, other_y.y, x-other_x.x, y-other_y.y)

    def print_rectangle(self):
        print [self.x, self.y, self.w, self.h]

r1 = Rectangle(1, 1, 5, 2)
r2 = Rectangle(4, 2, 3, 5)
#r2.intersection(r1).print_rectangle()

def check_validity(root, min, max):
    if not root:
        return True
    elif root.val >= min and root.val <= max:
        return check_validity(root.l, min, root.val) and check_validity(root.r, root.val, max)
    else:
        return False

class Tree(object):
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None

    def isBalanced(self):
        return self.balance() > 0

    def balance(self):
        if not self:
            return 0
        left_balanced = left.balance()
        right_balanced = right.balance()
        if left_balanced < 0 or right_balanced < 0 or abs(left_balanced - right_balanced)>1:
            return -1
        return 1 + max(left_balanced, right_balanced)

    def validBST(self):
        return check_validity(self, float('-inf'), float('inf'))


def exist(board, word):
    visited = [[0 for i in board[0]] for j in board]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not visited[i][j]:
                if board[i][j] in word:
                    letters = []
                    add_letters(board, i, j, letters, word, visited)
                    if word in letters:
                        return True
    return False

    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """

def add_letters(board, s, e, letters, word, visited):
    if 0 > s or s >= len(board) or 0 > e or e >= len(board[0]) or visited[s][e]:
        return
    #print [s, e]
    l = board[s][e]
    visited[s][e] = 1
    if l in word:
        letters.append(l)
        x = s+1
        y = e+1
        print [s-1, e]
        add_letters(board, s-1, e, letters, word, visited)
        add_letters(board, s+1, e, letters, word, visited)
        add_letters(board, s, e-1, letters, word, visited)
        add_letters(board, s, e+1, letters, word, visited)
    else:
        return

print exist(["AB","SF","AD"], "ABS")
