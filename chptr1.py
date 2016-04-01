def fib(n):
    repeated =
    if (n==1 or n==2):
        return 1

    return fib(n-1) + fib(n-2)

dictionary = {}
def unique(s):
    for i in s:
        if i in dictionary:
            return False
        else:
            dictionary[i] = 1
    return True

# print(unique('SS'))

def unique2(s):
    letters = []
    for i in range(256):
        letters.append(0)
    for i in s:
        a = ord(i)
        print(a)
        if letters[a]==0:
            letters[a]=1
        else:
            return False
    return True

# print unique2('salina')
# print unique2('salin')

def urlify(s):
    final_url = ""
    for i in s:
        if i==" ":
            final_url+= "%20"
        else:
            final_url+= i
    return final_url

# print(urlify('Salina Wu  '))

def palindrome(s):
    length = len(s)
    dict = {}
    for i in range(length):
        if s[i] in dict:
            dict[s[i]] += 1
        else:
            dict[s[i]] = 1

    odd = 0
    for i in dict:
        if dict[i]%2 == 1:
            if odd==1:
                return False
            else:
                odd = 1
    return True

#print(palindrome('ssaalliii'))
#print(palindrome('salina'))

def one_away(s1, s2):
    longer = s1 if len(s1) > len(s2) else s2
    shorter = s1 if len(s1) < len(s2) else s2
    first = 0
    second = 0
    difference = False
    while first<len(shorter) and second<len(longer):
        if shorter[first] != longer[second]:
            if difference is True:
                return False
            difference = True

            if len(shorter)==len(longer):
                first += 1
        else:
            first += 1
        second += 1
    return True

# print(one_away('pale', 'ple'))

def str_compress(s):
    char = s[0]
    count = 1
    final = ""
    i = 0
    while i+1 < len(s):
        if i+1 < len(s)-1:
            if s[i]!=s[i+1]:
                final += s[i] + str(count)
                count = 1
            else:
                count += 1
        else:
            if s[i]!=s[i+1]:
                final += s[i] + str(count)
                final += s[i+1] + '1'
            else:
                final += s[i] + str(count+1)
        i += 1

    if len(final) < len(s):
        return final
    else:
        return s

# print str_compress('abcdefghij')

def zero_matrix(matrix):
    zero_row = []
    zero_col = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] is 0:
                zero_row.append(i)
                zero_col.append(j)

    print(zero_row)
    print(zero_col)
    col = []
    for j in range(len(matrix[0])):
        col.append(0)
    for i in zero_row:
        matrix[i] = col
    for i in zero_col:
        for j in range(len(matrix)):
            for k in range(len(matrix[0])):
                if k==i:
                    matrix[j][k] = 0

    return matrix

# print zero_matrix([[0, 2, 3], [4, 0, 6], [7, 8, 9], [1, 2, 3]])

def str_rotate(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 += s1
    return s2 in s1

def palindrome_permutation(s):
    hash = {}
    for letter in s:
        if letter in hash:
            hash[letter]+=1
        else:
            hash[letter] = 1
    odd = 0
    for l in hash:
        if hash[l]%2 == 1:
            if odd == 0:
                odd +=1
            else :
                return False
    return True

# print palindrome_permutation('salina')
# print palindrome_permutation('saliinnas')
#'in' is the 'isSubstring' method

def profit(s):
    min_val = s[0]
    max_diff = 0
    for i in s:
        if i<min_val:
            min_val = i
        if i - min_val > max_diff:
            max_diff = i - min_val
    return max_diff

print profit([2, -5, 3, 7])
# print str_rotate('waterbottle', 'erbottlewat')

class Node(object):

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def remove_dups(self):
        dict = {}
        temp = Node(None)
        while self!=None:
            if self.data in dict:
                temp.next_node=self.get_next()
            else:
                dict[self.data] = 1
                temp = self

            self = self.get_next()

    def kth2last(self, k):
        n = 0
        temp = self
        while temp is not None:
            n += 1
            temp = temp.get_next()
        n = n-k
        temp = self
        for i in range(n):
            temp = temp.get_next()
        return temp.get_data()

    def print_self(self):
        temp = self
        while temp is not None:
            print(temp.data)
            temp = temp.get_next()

    def partition(self, x):
    #Fixme
        less = Node(None)
        more = Node(None)
        final = less
        mid = more
        while self is not None:
            if self.get_data() >=x:
                more.data = self.get_data()
                more.set_next(Node(None))
                if mid.get_data() == None:
                    mid = more
                more = more.get_next()
            else:
                less.data = self.get_data()
                less.set_next(Node(None))
                if final.get_data() == None:
                    final = more
                less = less.get_next()
            self = self.get_next()
        final.print_self()
        more.print_self()
        less.set_next(mid)
        return final

    def sum_list(self, summand, carry):

        if self is None and summand is None and carry is 0:
            return Node(None)

        final = Node(None)
        val = carry
        if self is not None:
            val += self.get_data()
        if summand is not None:
            val += summand.get_data()

        final.data = val%10
        val = val/10

        if self.get_next() is not None and summand is not None:
            summand = summand.get_next() if summand.get_next() is not None else None
            final.set_next(self.get_next().sum_list(summand, val))
        return final

def intersecting(a, b):
    a_len = 0
    a_temp = a
    while a_temp is not None:
        a_len += 1
        if a_temp.get_next() is None:
            a_last = a_temp.data
        a_temp = a_temp.get_next()

    b_len = 0
    b_temp = b
    while b_temp is not None:
        b_len += 1
        if b_temp.get_next() is None:
            if b_temp.data != a_last:
                return False
        b_temp = b_temp.get_next()

    long = b if b_len > a_len else a
    short = a if b_len > a_len else b
    diff = abs(b_len-a_len)

    for i in range(diff):
        long = long.get_next()

    while long is not None:
        if long.data == short.data:
            return long.data
        long = long.get_next()
        short = short.get_next()


# n1 = Node(1)
# n2 = Node(4)
# n3 = Node(3)
# n4 = Node(2)
# n1.next_node = n2
# n2.next_node = n4
# n4.next_node = n3
# n1.remove_dups()
# n1.print_self()
# print(n1.kth2last(2))
# n1.print_self()
# print('\n')
# n1.partition(2).print_self()

# n1 = Node(7)
# n2 = Node(1)
# n3 = Node(6)
# n1.set_next(n2)
# n2.set_next(n3)
# m1 = Node(5)
# m2 = Node(9)
# m3 = Node(2)
# m1.set_next(m2)
# m2.set_next(m3)
# sum = n1.sum_list(m1, 0)
# sum.print_self()

# n1 = Node(3)
# n2 = Node(1)
# n3 = Node(5)
# n4 = Node(9)
# n5 = Node(7)
# n6 = Node(2)
# n7 = Node(1)
# m1 = Node(4)
# m2 = Node(6)
# m3 = n5
# m4 = n6
# m5 = n7
#
# n1.set_next(n2)
# n2.set_next(n3)
# n3.set_next(n4)
# n4.set_next(n5)
# n5.set_next(n6)
# n6.set_next(n7)
# m1.set_next(m2)
# m2.set_next(m3)
# m3.set_next(m4)
# m4.set_next(m5)
#
# print(intersecting(n1, m1))

class Tree(object):

    def __init__(self, data, r_node=None, l_node=None):
        self.root = data
        self.l = l_node
        self.r = r_node

    def print_tree(self):
        if self is not None:
            if self.l is not None:
                self.l.print_tree()
            print(self.root)
            if self.r is not None:
                self.r.print_tree()

    def balanced(self):
        if max_diff(self) is False:
            return False
        else:
            return True

    def valid_bst(self, min, max):
        if self is None:
            return True

        if min is not None and self.root < min:
            return False
        if max is not None and self.root > max:
            return False

        print(self.root)
        if self.l is not None and self.r is not None:
            return self.l.valid_bst(min, self.root) and self.r.valid_bst(self.root, max)
        return True

def min_tree(ns, lower, upper):
    if ns is not None and lower<=upper:
        tree = Tree(None)
        l = (upper+lower)/2
        tree.root = ns[l]
        tree.l = min_tree(ns, lower, l-1)
        tree.r = min_tree(ns, l+1, upper)
        return tree
    return None

def list_depths(t, level, list):
    if t is not None:
        if len(list)==level:
            list.append([])
        list[level].append(t.root)
        list_depths(t.l, level+1, list)
        list_depths(t.r, level+1, list)
    return list

def max_diff(self):
    if self is None:
        return 0

    left_height = max_diff(self.l)
    if left_height == -1:
        return False
    right_height = max_diff(self.r)
    if right_height ==-1:
        return False

    if self.l is not None and self.r is not None:
        return max(self.l.root, self.r.root) + 1

    diff = abs(left_height - right_height)
    if diff>1:
        return False
    else:
        return max(left_height, right_height) + 1

def no_recursion_traversal(t):
    stack = []
    stack.append(t[0])
    while stack or t is not None:
        if t.left is not None:
            stack.append(t.left.data())
            t= t.left
        else:
            print(stack[-1])
            stack.pop()
            t = t.right

# tree = min_tree([1,2, 3, 4, 5], 0, 4)
# tree.print_tree()
# list = list_depths(tree, 0, [])
# print(list)
# print(tree.balanced())
# print(tree.valid_bst(None, None))

def paths_w_sums(t, n):
    count = 0

    if t is None:
        return 0

    count += sum_paths(t, t.root, n)
    return count + paths_w_sums(t.l, n) + paths_w_sums(t.r, n)

def sum_paths(t, sum, n):
    print(sum)
    if t is None:
        return 0
    if sum==n:
        return 1
    left = 0
    right = 0
    if t.l is not None:
        left = t.l.root
    if t.r is not None:
        right = t.r.root
    return sum_paths(t.l, sum+left, n) + sum_paths(t.r, sum+right, n)

# tree = min_tree([2, 1, 3, 4, 5], 0, 4)
# tree.print_tree()
# print(paths_w_sums(tree, 5))

def check_subtree(t1, t2):
    if t1 is None:
        return True
    if t2 is None:
        return False

    if t1.root==t2.root:
        match_trees(t1, t2)
    return check_subtree(t1.l, t2) or check_subtree(t1.r, t2)

def match_trees(t1, t2):
    if t2 is None and t1 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t1.root==t2.root:
        return match_trees(t1.l, t2.l) and match_trees(t1.r, t2.r)
    return False

def triple_step(n):
    if n>0:
        return triple_step(n-1) + triple_step(n-2) + triple_step(n-3)
    elif n==0:
        return 1
    else:
        return 0

#print(triple_step(2))

def robot(grid):
    if grid is None:
        return None

    list_ps = []
    return get_path(grid, len(grid)-1, len(grid[0])-1, ps)

def get_path(grid, r, c, ps):
    if grid[r][c]==False or r<0 or c<0:
        return None

    if (r==0 and c==0) or (get_path(grid, r-1, c, ps) is not None) or (get_path(grid, r, c-1, ps) is not None):
        ps.append([r, c])
        return ps

    return None

def magic_array(a, lower, upper):
    if a is not None and upper>=lower:
        mid = (lower + upper)/2
        if a[mid] == mid:
            return mid
        elif a[mid]>mid:
            return magic_array(a, lower, mid-1)
        else:
            return magic_array(a, mid+1, upper)
    return None

# a1 = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
# print(magic_array(a1, 0, len(a1)))

# def perm_no_dups(s):
#     x = [""]
#     for digit in string_n:
#         x = [i + j:
#             for i in s
#             for j in perm_no_dups(s[1:])
#             ]
#     return x

def paint_fill(a, pt, color):
    old_color = a[pt[0]][pt[1]]
    fill_rest(a, pt)

def fill_rest(a, pt, color):
    if a[pt[0]][pt[1]] == old_color:
        a[pt[0]][pt[1]] = color
        fill_rest(a[pt[0]+1][pt[1]])
        fill_rest(a[pt[0]-1][pt[1]])
        fill_rest(a[pt[0]][pt[1]+1])
        fill_rest(a[pt[0]][pt[1]-1])

def coins(n, coin):
    next = 0
    if coin==25:
        next = 10
    elif coin==10:
        next = 5
    elif coin==5:
        next = 1
    elif coin==1:
        return 1
    else:
        print('error')

    final = 0
    i = 0
    while i*coin<=n:
        final+= coins(n-i*coin, next)
        i+=1
    return final

#print(coins(5, 25))

def sorted_merge(a, b):
    a_index = 0
    b_index = 0
    c = [None]*(len(a)+len(b))
    temp = b[b_index]
    ahead = a[a_index]
    i = 0
    while a_index<len(a) and b_index<len(b):
        c[i] = min(temp, ahead)
        temp = max(temp, ahead)
        if temp==b[b_index]:
            a_index+=1
            if a_index<len(a):
                ahead = a[a_index]
        else:
            b_index+=1
            if b_index<len(b):
                ahead = b[b_index]
        i+=1
    if a_index<len(a):
        c[i:] = (a[a_index:])
    if b_index<len(b):
        c[i:] = (b[b_index:])
    return c

# a = [1, 3, 5, 7]
# b = [2, 4, 6, 8, 9, 10, 15, 16]
# print(sorted_merge(a, b))

def group_anagram(ls):
    final = []
    for i in range(len(ls)-1):
        ls[i] = list(ls[i])
        ls[i].sort()
        final.append("".join(ls[i]))
    final.sort()
    return final

a = ["salina", "wu", "is", "funny", "lol", "uw", "anilas", "si"]
print(group_anagram(a))

def search_rotated(array, lower, upper, x):
    if upper<lower:
        return -1
    mid = (lower+upper)/2
    if array[mid]==x:
        return mid

    if array[mid]<array[lower]:
        if x<array[upper] and x>array[mid]:
            search_rotated(array, mid+1, upper, x)
        else:
            search_rotated(array, lower, mid-1, x)
    elif array[mid]>array[lower]:
        if x>array[lower] and x<array[mid]:
            search_rotated(array, lower, mid-1, x)
        else:
            search_rotated(array, mid+1, upper, x)
    else:
        if array[mid]!=array[upper]:
            search_rotated(array, mid+1, upper, x)

# a = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
# r = search_rotated(a, 0, 11, 5)
# print(r)

def bin_search_listy(a, lower, upper, x):
    if upper < lower or a is None:
        return None
    mid = (lower + upper)/2
    if a[mid] == x:
        return mid

    if a[mid]>x or a[mid]==-1:
        return bin_search(a, lower, mid-1, x)

    if a[mid]<x:
        return bin_search(a, mid+1, upper, x)

def listy(a, x):
    i = 1
    len = 0
    while a[i]!= -1:
        len=i
        i*=2
    return bin_search_listy(a, lower, higher, x)

def sparse_search(a, lower, higher, s):
    if a is None or lower>higher:
        return None

    mid = (lower+higher)/2
    if a[mid] == "":
        l = mid-1
        r = mid+1
        while a[mid] == "":
            if l<lower or r>higher:
                return None
            if a[l]!="":
                mid = l
                break
            if a[r]!="":
                mid = r
                break
            l-=1
            r+=1

        if a[mid] == s:
            return mid
        if a[mid]<s:
            return sparse_search(a, mid+1, higher, s)
        if a[mid]>s:
            return sparse_search(a, lower, mid-1, s)

def sorted_matrix(m, x):
    r = 0
    c = len(m[0])-1
    while r<len(m) and c>=0:
        if m[r][c]==x:
            return [r, c]
        elif m[r][c]>x:
            c-=1
        else:
            r+=1
    return -1

def peaks(a):
    s = sorted(a)
    print(s)
    l = len(s)-1
    for i in range(0, l):
        if i%2!=1:
            t = s[i]
            s[i] = s[i+1]
            s[i+1] = t
    return s

def peaks1(a):
    s = sorted(a)
    t = []
    length = len(a)
    upper = length/2+1 if length%2==1 else length/2
    for i in range(0, upper):
        t.append(s[i])
        t.append(s[length-1-i])
    if length%2==1:
        t.pop()
    return t
#
# a = [5, 3, 1, 2]
# print(peaks(a))
# print(peaks1(a))

def power_set(set, acc):
    length = len(set)
    n = pow(2, length)
    acc = []

    for i in range(n):
        index = 0
        subset = []
        while i>0:
            if i&1 == 1:
                subset.append(set[index])
            i>>=1
            index+=1
        acc.append(subset)
    return acc

#print(power_set([1, 2, 3], []))

#hanoi
class Hanoi(object):

    def __init__(self, i):
        self.index = i
        self.disks = []

    def add_disk(self, d):
        if d<self.disks[0]:
            print("invalid")
        else:
            self.disks.append(d)

    def move_top(self, t):
        d = self.disks.pop(0)
        t.disks.append(d)

    def moveDisks(self, n, dest, buff):
        if n>0:
            self.moveDisks(n-1, buff, dest)
            self.move_top(dest)
            buff.moveDisks(n-1, dest, self)

# t1 = Hanoi(0)
# t1.disks = [1, 2, 3]
# t2 = Hanoi(1)
# t3 = Hanoi(2)

# t1.moveDisks(3, t3, t2)
# print(t3.disks)

def perm_no_dups(s):
    result = []
    if len(s) ==1:
        result = [s]
    else:
        for i, c in enumerate(s):
            for p in perm_no_dups(s[i+1:] + s[:i]):
                result += [c+p]
    return result

#print(perm_no_dups('abc'))

class Card(object):
    def __init__(self, suit, card):
        self.suit = suit
        self.card = card

class Cards(object):
    def __init__(self):
        self.cards = []
        suits = ['spade', 'heart', 'clover', 'diamond']
        for i in range(13):
            if i==0:
                card = 'ace'
            elif i==10:
                card = 'jack'
            elif i==11:
                card = 'queen'
            elif i==12:
                card = 'king'
            else:
                card = str(i+1)
            for j in range(4):
                new_card = Card(suits[j], card)
                self.cards.append(new_card)

    def __repr__(self):
        for i in self.cards:
            print(i.card + ": " + i.suit)

# cards = Cards()
# print cards
import random
class Blackjack(object):

    def __init__(self):
        self.deck = Cards()
        r1 = random.randrange(52)
        c1 = self.deck.cards[r1]
        self.deck.cards.pop(r1)
        r2 = random.randrange(51)
        c2 = self.deck.cards[r2]
        self.deck.cards.pop(r2)
        r3 = random.randrange(50)
        c3 = self.deck.cards[r3]
        self.deck.cards.pop(r3)
        r4 = random.randrange(49)
        c4 = self.deck.cards[r4]
        self.deck.cards.pop(r4)
        self.dealer = [[c3.card, c3.suit], [c4.card, c4.suit]]
        self.player = [[c1.card, c1.suit], [c2.card, c2.suit]]

    def dealer_hand(self):
        sum = 0
        for i in self.dealer:
            card = i[0]
            if card=='ace':
                sum+=1
            elif card=='king' or card=='queen' or card=='jack':
                sum+=10
            else:
                sum+= int(card)
        return sum

    def player_hand(self):
        sum = 0
        for i in self.player:
            card = i[0]
            if card=='ace':
                sum+=1
            elif card=='king' or card=='queen' or card=='jack':
                sum+=10
            else:
                sum+= int(card)
        return sum

    def dealer_hit(self):
        d = self.dealer_hand()
        while d<=17:
            length = len(self.deck.cards)
            r = random.randrange(length)
            c = self.deck.cards[r]
            self.deck.cards.pop(r)
            self.dealer.append([c.card, c.suit])
            if c.card=='ace':
                d+=1
            elif c.card=='king' or c.card=='queen' or c.card=='jack':
                d+=10
            else:
                d+= int(c.card)
        return self.dealer

    def player_hit(self):
        b = blackjack.player_hand()
        if b>=17:
            return 'illegal move'
        r = random.randrange(len(self.deck.cards))
        c = self.deck.cards[r]
        self.deck.cards.pop(r)
        self.player.append([c.card, c.suit])

    def game(self):
        blackjack.dealer_hit()
        dealer = self.dealer_hand()
        player = self.player_hand()
        print(player)
        while self.player_hand() <17:
            hit = raw_input('Do you want to hit? Yes or No')
            if hit=="Yes":
                self.player_hit()
                print(self.player_hand())
            else:
                break

        if (player<=21 and dealer<21 and (21-player < 21-dealer)) or (player<=21 and dealer>21):
            print('player wins')
            print(self.player_hand())
            print(self.dealer_hand())
        else:
            print('dealer wins')
            print(self.player_hand())
            print(self.dealer_hand())

    def rep(self):
        print(self.dealer)
        print(self.player)

# blackjack = Blackjack()
# blackjack.game()
import time

class Employee(object):
    def __init__(self):
        self.available = True

class CallCenter(object):
    def __init__(self, respondents, managers, directors):
        self.respondents = [Employee()] * respondents
        self.managers = [Employee()] * managers
        self.directors = [Employee()] * directors

    @staticmethod
    def check_list(list):
        for i in list:
            if i.available == True:
                i.available = False
                return True
        return False

    def dispatchCall(self):
        respondent_availibility = self.check_list(self.respondents)
        if respondent_availibility != False:
            print "now speaking to respondent"
            return respondent_availibility
        manager_availability = self.check_list(self.managers)
        if manager_availability != False:
            print "now speaking to manager"
            return manager_availability
        director_availibility = self.check_list(self.directors)
        if director_availibility != False:
            print "now speaking to director"
            return director_availibility
        print 'nobody available to speak'

    def hang_up(self, emp, i):
        if emp=="respondents":
            self.respondents[i].available = True
            print "respondent is now available"
        elif emp=="managers":
            self.managers[i].available = True
            print "manager is now available"
        elif emp=="directors":
            self.directors[i].available = True
            print "director is now available"
        else:
            print "no employee of the type"

    def clear_all(self):
        for i in self.respondents:
            i.available = True
        for i in self.managers:
            i.available = True
        for i in self.directors:
            i.available = True

    def print_all(self):
        for i in self.respondents:
            print(i.available)
        for i in self.managers:
            print(i.available)
        for i in self.directors:
            print(i.available)
#
# callcenter = CallCenter(1, 1, 1)
# callcenter.clear_all()
# callcenter.dispatchCall()
# callcenter.dispatchCall()
# callcenter.dispatchCall()
# callcenter.hang_up('managers', 0)
# callcenter.print_all()
# callcenter.dispatchCall()
# callcenter.dispatchCall()

class Music_lib(object):
    def __init__(self, artists, songs):
        self.artists = []* artists
        for i in self.artists:
            for j in songs[i]:
                self.artists[i].append(str(j))

class Jukebox(object):

    def __init__(self, artists, songs):
        self.music_lib = Music_lib(artists, songs)
        self.queue = []

    def view_artist(self, artist):
        print(self.music_lib[artist])

    def up_next(self):
        print(self.queue)

    def choose_song(self, artist, song):
        self.queue.append([artist, song])

    def make_request(self, cents, requests):
        n = cents/25
        for i in range(n):
            self.choose_song(requests[0], requests[1])

    def play_song(self):
        self.queue.pop(0)

def num_swapper(a, b):
    a = a-b
    b += a
    a = b-a
    print(a, b)

#num_swapper(5, 3)

def word_freq(book, word):
    b = book.split(' ')
    dict = {}
    for i in b:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    if word in dict:
        return dict[word]
    else:
        return 0

def tic_tac_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return True
        if board[0][i] == board[1][i] == board[2][i]:
            return True
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] == board[1][1] == board[2][0]:
        return True
    return False

def smallest_diff(a, b):
    a.sort()
    b.sort()
    min = b[0]-a[0]
    min_pair = None
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if abs(a[i]-b[j]) < min:
            min = abs(a[i]-b[j])
            min_pair = [a[i], b[j]]
        if a[i]<b[j]:
            i+=1
        elif a[i]>b[j]:
            j+=1
        else:
            return 0

    while i<len(a):
        if abs(a[i]-b[j-1]) < min:
            min = abs(a[i]-b[j-1])
            min_pair = [a[i], b[j-1]]
        i+=1
    while j<len(b):
        if abs(a[i-1]-b[j]) < min:
            min = abs(a[i-1]-b[j])
            min_pair = [a[i-1], b[j]]
        j+=1
    return min_pair

#print(smallest_diff([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]))

def sub_sort(array):
    mini = 0
    maxi = len(array)-1
    length = len(array)-1
    for i in range(length-1):
        if array[i]>array[i+1]:
            mini = i+1
            break
    i = length
    while i>0:
        if array[i]<array[i-1]:
            maxi = array[i]
        i-=1
    sub = array[mini:maxi+1]
    submax = max(sub)
    submin = min(sub)
    for i in range(length):
        if array[mini] <= array[i]:
            mini = i
            break
    i = length
    while i>0:
        if array[maxi]>=array[i-1]:
            maxi = i-1
            break
        i -=1
    return [mini, maxi]

#print(sub_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))

def max_sum(array):
    sum = 0
    max_sum = 0
    for i in array:
        sum += i
        if sum > max_sum:
            max_sum = sum
        elif sum < 0:
            sum = 0
    return max_sum
