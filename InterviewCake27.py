"""This module contains solutions to Problem 27 of Interview Cake."""

def reverse_string(s):
    """Reverses a string in the form of a list in place."""
    length = len(s)
    for i in range(length):
        if i >= length - 1 - i:
            return ''.join(s)

        tmp = s[i]
        s[i] = s[length-1-i]
        s[length-1-i] = tmp

def reverse_word(lst, index, length):
    """Reverses a word in a list in place"""
    left_pointer = index
    right_pointer = index + length - 1

    while left_pointer < right_pointer:
        #print(left_pointer, right_pointer)
        tmp = lst[left_pointer]
        lst[left_pointer] = lst[right_pointer]
        lst[right_pointer] = tmp

        left_pointer += 1
        right_pointer -= 1

def reverse_words(message):
    """Reverses the words of a message in place."""
    msg = list(message)
    word_length = 0
    i = 0

    while i < len(msg):
        if msg[i] != ' ':
            word_length += 1
            if i == len(msg)-1:
                reverse_word(msg, i-word_length+1, word_length)
        else:
            reverse_word(msg, i-word_length, word_length)
            word_length = 0

        i += 1

    reverse_string(msg)
    return ''.join(msg)

l = list("abcdefg")
reverse_string(l)
assert l == list("gfedcba")

l = list('alan really forgot')
reverse_word(l, 5, 6)
assert ''.join(l) == 'alan yllaer forgot'

assert reverse_words("hell a here") == "here a hell"
assert reverse_words("i am a legendary pokemon") == "pokemon legendary a am i"
