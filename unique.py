#Return True if all the characters in the string are unique. Otherwise, return False.
def unique_chars_in_string(s):
    char_list = [];
    for x in s:
        if brute_force_search(char_list, x):
            return False
        else:
            char_list.append(x)
    return True


#Search array for a character using brute force
def brute_force_search(s, c):
    for x in s:
        if x == c:
            return True
    return False


#Insert character into a binary tree represented by an array
def binary_insert(s, c):
    int_c = ord(c)
    raise Exception('Not implemented yet')


#Search a binary tree represented by an array for a character
def binary_search(s, c):
    int_c = ord(c)
    raise Exception('Not implemented yet')


print(unique_chars_in_string("Hello, World!"))
print(unique_chars_in_string("Thequickbrownfxjmpdvlazy g"))