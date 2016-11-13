def triple_step(n):
    return triple_step_helper(n, [])
def triple_step_helper(n, memo):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        memo[n] = triple_step_helper(n-1, memo) + triple_step_helper(n-2, memo) + triple_step_helper(n-3, memo)
    return memo[n]

def robot_in_grid(grid):
    memo = {}
    return robot_grid_helper(grid, len(grid)-1, len(grid[0])-1, memo, [])

def robot_grid_helper(grid, r, c, memo, path):

    if r<0 or c<0 or not grid[r][c]:
        return False

    if memo[(r, c)]:
        return memo[(r, c)]

    if (r==0 and c==0) or robot_grid_helper(grid, r-1, c, path) or robot_grid_helper(grid, r, c-1, path):
        memo[(r, c)] = True
        path.append([r, c])
        return True
    else:
        memo[(r, c)] = False
        return False

def magic_index(A):
    length = len(A)
    halfway = length/2
    index = A[halfway]
    if index==halfway:
        return index
    elif length==1 or length==0:
        return False
    elif index>halway:
        return magic_index(A[:halfway])
    else:
        return magic_index(A[halfway:])

def magic_index_dups(A):
    length = len(A)
    halfway = length/2
    index = A[halfway]
    if index==halfway:
        return index
    elif length==1 or length==0:
        return False
    elif index>halway:
        return magic_index_dups(A[:halfway]) or magic_index_dups(A[index:])
    else:
        return magic_index_dups(A[halfway:]) or magic_index_dups(A[:index])

def build_subsets_generator(s):
    if len(s)<=1:
        yield s
        yield []
    else:
        for val in build_subsets(s[1:]):
            yield [s[0]]+val
            yield val

def build_subsets_bits(s):
    final = []
    for i in range(1<<len(s)):
        subset = []
        x = 0
        while i!=0:
            if i&1==1:
                subset.append(s[x])
            x+=1
            i>>=1
        final.append(subset)
    return final

def recursive_multiply(a, b):
    smaller = (a<b ? a : b)
    bigger = (a<b ? b : a)
    if smaller==0:
        return 0
    elif smaller==1:
        return bigger
    else:
        half_prod = recursive_multiply(smaller>>1 , bigger)
        return half_prod%2==0 ? half_prod<<1 : half_prod<<1+bigger

def towers_of_hanoi(first, thru, final, N):
    if N>0:
        towers_of_hanoi(first, final, thru, N-1)
        final.append(first.pop())
        towers_of_hanoi(thru, first, final, N-1)
    return final

def permutations(s, first=0, all_perms = {}):
    if first==len(s):
        string = "".join(s)
        if string not in all_perms:
            all_perms[string]=1
    for i in range(first, len(s)):
        original = [x for x in s]
        original[first], original[i] = original[i], original[first]
        permutations(original, first+1, all_perms)
    return all_perms.keys()

def parens(i):
    list = []
    parens_helper(i, i, list, "")
    return list

def parens_helper(r, l, list, string):
    if l<0 || r<l:
        return False

    if r==0 && l==0:
        list.append(string)
    else:
        if l>0:
            parens_helper(r, l-1, list, string+"(")
        if r>l:
            parens_helper(r-1, l, list, string+")")

def paint_fill(grid, r, c, color):
    if grid[r][c]==color:
        return False

    paint_fill_helper(grid, r, c, color, grid[r][c])
    return grid

def paint_fill_helper(grid, r, c, color, old):
    if r<len(grid) || r<0 || c<0 || c>len(grid[0]):
        return False

    if grid[r][c]==old:
        grid[r][c]=color
        paint_fill_helper(grid, r+1, c, color, old)
        paint_fill_helper(grid, r-1, c, color, old)
        paint_fill_helper(grid, r, c+1, color, old)
        paint_fill_helper(grid, r, c-1, color, old)

def make_change(n):
    denoms = [25, 10, 5, 1]
    dict = [[0 for i in range(n)] for i in range(len(denoms))]

def make_change_helper(n, i, dict, denoms):
    if i < len(denoms):
        return 1
    elif dict[n][i]>0:
        return dict[n][i]

    mult = 0
    amt = denoms[i]
    while mult*amt < n:
        ways = make_change_helper(n-(mult*amt), i+1, dict, denoms)
        mult+=1

    dict[n][i] = ways
    return dict[n][i]

def n_queens(N):
    results = []
    n_queens_helper(0, 8, [], results)
    return results

def n_queens_helper(row, N, column, results):
    if row==N:
        results.append(column)
    else:
        for col in range(N):
            if can_place(row, col, column):
                column[row] = col
                n_queens(row+1, column, results)

def can_place(row, col, column):
    for i in range(row):
        if column[i]==col or (abs(column[i]-col)==row1-i):
            return False
    return True

def order_boxes(b):
    sorted_boxes = sorted(b, key=lambda x: x.h, reverse=True)
    max_height = 0
    curr_stack = [0] * len(b)
    for i in sorted_boxes:
        max_height = max(max_height, order_boxes_helper(b, i, curr_stack))
    return max_height

def order_boxes_helper(b, bottom, curr_stack):
    if curr_stack[bottom]>0:
        return curr_stack[bottom]
    else:
        max_height = 0
        while bottom+1<len(b):
            if can_be_below(b[bottom], b[bottom+1]):
                max_height = max(max_height, order_boxes_helper(b, bottom+1, curr_stack))
    curr_stack[bottom] = max_height + b[bottom].h
    reutn curr_stack[bottom]

def can_be_below(b1, b2):
    return b1.w > b2.w and b1.d > b2.d

def bool_eval(s, bool):
    return bool_eval_helper(s, bool, {})

def bool_eval_helper(s, bool, hashmap):
    hash_value = s + bool ? '1' : '0'
    if len(s)==0:
        return 0
    elif len(s)==1:
        string_bool = s=='1' ? True : False
        return string_bool==bool ? 1 : 0
    elif hashmap[hash_value]:
        return hashmap[hash_value]
    else:
        ways = 0
        for i in range(1, len(s), 2):
            left = bool_eval_helper(s[:i], bool, hashmap)
            right = bool_eval_helper(s[i+1:], bool, hashmap)
            left_true = bool_eval_helper(left, true, hashmap)
            left_false = bool_eval_helper(left, false, hashmap)
            right_true = bool_eval_helper(right, true, hashmap)
            right_false = bool_eval_helper(right, false, hashmap)
            all_ways = (left_false + left_true) * (right_false + right_true)

            val = s[i]
            if val=='&':
                total = left_true * right_true
            elif val=='^':
                total = (left_false * right_true) + (left_true * right_false)
            elif val=='|':
                total = all_ways - (left_false * right_false)
            else:
                print('unknown sign')

            ways += bool ? total : all_ways-total
        hashmap[hash_value] = ways
        return ways
