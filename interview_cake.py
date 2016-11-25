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
