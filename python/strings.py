# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if count < 10:
        print repr("Number of donuts: %d" % count)
    else:
        print repr("Number of donuts: many")


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.
    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    number_of_letters = len(s)
    second_to_last = number_of_letters - 2

    if number_of_letters < 2:
        print repr('')
    else:
        print repr(str(s[0:2] + s[second_to_last:]))


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.
    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    import string

    first_letter = s[0]
    rest_of_word = s[1:]
    replacement = string.maketrans(first_letter, "*")

    print repr(first_letter + rest_of_word.translate(replacement))


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.
    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    a_start = a[0:2]
    b_start = b[0:2]
    a_rest = a[2:]
    b_rest = b[2:]

    print repr(b_start + a_rest + " " + a_start + b_rest)


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.
    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    length = len(s)
    end = length - 3
    end_of_string = s[end:]

    if length >= 3:
        if end_of_string == "ing":
            print repr(s + "ly")
        else:
            print repr(s + "ing")
    else:
        print repr(s)


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    :type s: str
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'
    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    str1 = "not"
    str2 = "bad"
    not_index = s.find(str1)
    bad_index = s.find(str2)

    if not_index < bad_index:
        print repr(s[0:not_index] + "good" + s[bad_index + 3:])
    else:
        print repr(s)


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back
    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    length_a = len(a)
    length_b = len(b)

    if length_a % 2 == 0:
        a_front = a[0:length_a / 2]
        a_back = a[length_a / 2:]
    else:
        a_front = a[0:(length_a / 2) + 1]
        a_back = a[(length_a / 2) + 1:]

    if length_b % 2 == 0:
        b_front = b[0:length_b / 2]
        b_back = b[length_b / 2:]
    else:
        b_front = b[0:(length_b / 2) + 1]
        b_back = b[(length_b / 2) + 1:]

    print repr(a_front + b_front + a_back + b_back)
