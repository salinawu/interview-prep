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

print denominations([2, 5, 3, 6], 10)
