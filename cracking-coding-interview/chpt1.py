# 1.1 Implement an algorithm to determine if a string has all unique characters
# What if you can not use additional data structures?


# with hash:

def unique_string(s):
    dict = {}
    for c in s:
        if c in dict:
            return False
        else:
            dict[c] = 1

    return True

#print(unique_string('salina'))
#print(unique_string('salin'))

# without hash: we can use an array

def unique_string1(s):
    array = []
    for i in s:
        if array[i-'a'] > 0:
            return False
        else:
            array[i-'a'] = 1
    return True

# print(unique_string('salina'))
# print(unique_string('salin'))
#
# print(unique_string('sss'))
# print(unique_string('abcd1029'))


# extra: Write code to reverse a C-Style String

def reverse_cstring(s):
    r = s[:-1]
    new = []
    for i in reversed(r):
        new.append(i)

    return new

#print(reverse_cstring("salina"))

# extra: Design an algorithm and write code to remove the duplicate characters
# in a string without using any additional buffer

def dup_char(s):
    print(s)
    s = sorted(s)
    print(s)
    new = []
    a = s[0]
    print(s[1:])
    for i in s[1:]:

        if a == i:
            s.remove(a)
        else:
            # print("i:" + i)
            # print(a)
            new.append(a)

            a = i
    return new

# print(dup_char("salina"))

#1.2: check if strings are permutations

def permutation(a, b):
    dict = {}
    for i in a:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1

    for i in b:
        if i in dict and dict[i]>0:
            dict[i]-=1
        else:
            return False

    for i in dict:
        if dict[i]>0:
            return False

    return True

# print(permutation("salina", "anilas"))
# print(permutation("yes", "no"))

#1.3: replace all spaces with "%20"

def urlify(s):
    string = ""
    for i in s:
        if i==" ":
            string += "%20"
        else:
            string += i

    return string

# print(urlify("salina is cool"))

#1.4: see if string is permutation of a palindrome

def palindrome_permutation(s):
    dict = {}
    perm = 0
    for i in s:
        if i in dict:
            dict[i]+=1
            if dict[i]%2 == 1:
                perm +=1
            else:
                perm -=1
        else:
            dict[i]=1
            perm +=1
    return perm <=1

# print(palindrome_permutation("salina"))
# print(palindrome_permutation("saliasil"))
# print(palindrome_permutation("saliasilb"))

#1.5: check if two strings are one letter off

#salina
#saina
#saiina
#sailna

#FIXME lol dun work
def one_away(a, b):
    a_len = len(a)
    b_len = len(b)

    longer = a if a_len > b_len else b
    shorter = a if a_len < b_len else b
    i_long = i_short = 0
    diff = False
    while i_long<len(longer) and i_short<len(shorter):
        if longer[i_long]!=shorter[i_short]:
            if diff==True:
                return False
            else:
                diff = True

            if len(longer)==len(shorter):
                i_short+=1
        else:
            i_short+=1
        i_long +=1
    return True

# print(one_away("salina", "saina"))
# print(one_away("salina", "sallina"))
# print(one_away("salina", "saxina"))
# print(one_away("salina", "sallinaa"))
# print(one_away("salina", "saxia"))


def string_compression(s):
    final = ""
    curr = s[0]
    count = 1
    if len(s) == 1:
        return curr + "1"
    for i in s[1:]:
        if i!=curr:
            final += curr+str(count)
            count = 1
            curr = i
        else:
            count += 1
    return final + curr + str(count)

# print(string_compression("aa"))
# print(string_compression("abc"))
# print(string_compression("aabbcs"))

def print_matrix(matrix):
    for i in matrix:
        print(i)

test_matrix = [["o", "x", "o", "o", "o"], ["o", "o", "o", "x", "o"],["x", "o", 0, "o", "o"], ["o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o"]]
#print_matrix(test_matrix)
#print("\n\n\n")

def rotate_matrix(matrix):
    n = len(matrix)
    floor = (n/2)
    ceil = (n+1)/2
    print(n)
    for x in range(floor):
        print(x)
        for y in range(ceil):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][n-1-x]
            matrix[y][n-1-x] = matrix[n-1-x][n-1-y]
            matrix[n-1-x][n-1-y] = matrix[n-1-y][x]
            matrix[n-1-y][x] = temp
    return matrix

#print_matrix(rotate_matrix(test_matrix))

def zero_matrix(matrix):
    columns = []
    rows = []
    n = len(matrix)
    for r in range(n):
        for c in range(n):
            if matrix[r][c]==0:
                rows.append(r)
                columns.append(c)

    rows = list(set(rows))
    columns = list(set(columns))
    for i in rows:
        matrix[i] = [0]*n
    for i in columns:
        for x in range(n):
            matrix[x][i]=0
    return(matrix)

# print_matrix(test_matrix)
# print("\n\n\n")
# print_matrix(zero_matrix(test_matrix))

def string_rotation(s, sub):
    full = s+s
    x = sub in full
    return sub in full

# print(string_rotation("salina", "inasal"))
# print(string_rotation("bye", "hih"))
