# 1. Implement an algorithm to determine if a string has all unique characters
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
