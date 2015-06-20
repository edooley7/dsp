# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
	if count < 10:
		print "Number of donuts: %d" % count
	else:
		print "Number of donuts: many"

donuts(4)
donuts(9)
donuts(10)
donuts(99)


def both_ends(s):
	number_of_letters = len(s)
	second_to_last = number_of_letters - 2
	
	if number_of_letters < 2:
		print ' '
	else:
		print s[0:2]+s[second_to_last:]

both_ends('spring')
both_ends('Hello')
both_ends('a')
both_ends('xyz')
    
    
def fix_start(s):
	import string
	first_letter = s[0]
	rest_of_word = s[1:]
	replacement = string.maketrans(first_letter, "*")
	
	print first_letter + rest_of_word.translate(replacement)
	
fix_start('babble')
fix_start('aardvark')
fix_start('google')
fix_start('donut')
    
    
def mix_up(a, b):
	a_start = a[0:2]
	b_start = b[0:2]
	a_rest = a[2:]
	b_rest = b[2:]
	
	print b_start + a_rest, a_start + b_rest

mix_up('mix', 'pod')
mix_up('dog', 'dinner')
mix_up('gnash', 'sport')
mix_up('pezzy', 'firm')

    
def verbing(s):
	length = len(s)
	end = length-3
	start_of_string = s[0:end]
	end_of_string = s[end:]
	
	if length >= 3:
		if end_of_string == "ing":
			print s + "ly"
		else:	
			print s + "ing"
	else:
		print s
		
verbing('hail')
verbing('swiming')
verbing('do')
    

def not_bad(s):
	not_index = s.find("not")
	bad_index = s.find("bad")
	
	if not_index < bad_index:
		print s[0:not_index] + "good" + s[bad_index + 3:]
	else:	
		print s

not_bad('This movie is not so bad')
not_bad('This dinner is not that bad!')
not_bad('This tea is not hot')
not_bad("It's bad yet not")
 
 
def front_back(a, b):
	length_a = len(a)
	length_b = len(b)
	
	if length_a%2 == 0:
		a_front = a[0:length_a/2]
		a_back = a[length_a/2:]
	else:
		a_front = a[0:(length_a/2)+1]
		a_back = a[(length_a/2)+1:]
		
	if length_b%2 == 0:
		b_front = b[0:length_b/2]
		b_back = b[length_b/2:]
	else:
		b_front = b[0:(length_b/2)+1]
		b_back = b[(length_b/2)+1:]
		
	print a_front + b_front + a_back + b_back

front_back('abcd', 'xy')
front_back('abcde', 'xyz')
front_back('Kitten', 'Donut')
