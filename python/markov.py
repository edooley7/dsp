#!/usr/bin/env python

import sys
from random import choice
from sys import argv

script, filename, max_words = argv


def build_dict(words):
    d = {}
    for i, word in enumerate(words):
        try:
            first, second = words[i], words[i + 1]
        except IndexError:
            break
        key = first
        if key not in d:
            d[key] = []
        d[key].append(second)
    return d


def generate_sentence(d):
    word_count = 0
    s = [key for key in d.keys() if key[0][0].isupper()]
    key = choice(s)
    s = []
    first = key
    s.append(first)
    word_count = word_count + 1
    while True:
        try:
            second = choice(d[key])
        except KeyError:
            break
        s.append(second)
        word_count = word_count + 1
        if word_count >= int(max_words):
            break
        key = second
        first = key

    return ' '.join(s)


def main():
    fname = sys.argv[1]
    with open(fname, "rt") as f:
        text = f.read()

    words = text.split()
    d = build_dict(words)
    sent = generate_sentence(d)
    print(sent)


main()
