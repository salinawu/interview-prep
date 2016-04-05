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


# 1.2 Write code to reverse a C-Style String

def reverse_cstring(s):
    r = s[:-1]
    new = []
    for i in reversed(r):
        new.append(i)

    return new

#print(reverse_cstring("salina"))

# 1.3 Design an algorithm and write code to remove the duplicate characters
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

print(dup_char("salina"))
