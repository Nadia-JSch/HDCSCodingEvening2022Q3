# Approach: find the length of the string
# check if it's even or odd
# print the first and last letter
# if even print the middle letter
# if odd print the middle one
# check if there's a repeat character


#  finds the length of a string
def find_length(text):
    string_length = len(text)
    return string_length

#  finds the first letter of a string
def first_char(text):
    return text[0]

# finds the last letter of a string
def last_char(text):
    return text[-1]


# check if even or odd, prints middle two letters if even or middle letter if odd
def even_odd(text):
    if find_length(text) % 2 == 0:
        print("it's even")
        # print the middle 2 letters
        second_middle_char = (find_length(text) // 2)
        first_middle_char = second_middle_char - 1
        return text[first_middle_char] + text[second_middle_char]
    else:
        print("it's odd")
        # print the middle letter
        middle = text[int(find_length(text)) // 2]
        return middle

#  checks if the second letter is repeated in the rest of the substring
def second_letter_repeats(text):
    # flag if a repeat of the second letter is found
    found = False
    second_letter = text[1]
    # get substring after second char
    third_char_plus = text[2:]
    for char in third_char_plus:
        if char == second_letter:
            found = True
            return "@ index " + str(third_char_plus.index(char) + 2)
    if not found:
        return "not found"

# calls functions and prints results
def print_list_result(text):
    result = [find_length(text), first_char(text), last_char(text),
          second_letter_repeats(text)]
    print(result)

# call the result function
print_list_result("catta")
