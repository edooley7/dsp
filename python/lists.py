# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
	count = 0
	
	for i in words:
		if len(i) >= 2:
			if i[0] == i[-1]:
				count += 1
			else:
				count
		else:
			count
	
	print count
	
match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
match_ends(['', 'x', 'xy', 'xyx', 'xx'])				
match_ends(['aaa', 'be', 'abc', 'hello'])			


def front_x(words):
	x_words = []
	not_x_words = []
	
	for i in words:
		if i[0] == "x":
			x_words.append(i)
		else:
			not_x_words.append(i)
	
	new_list = []
	
	for i in sorted(x_words):
		new_list.append(i)
	for i in sorted(not_x_words):
		new_list.append(i)
		
	print new_list 
	
front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])

def middle_of_list(listed):
	if len(listed) > 2:
		return listed[1]
	else: 
		return None


def sort_last(tuples):
	switched_list = []
	listed = map(list, tuples)
	
	for i in range(0,len(listed)):
		first = listed[i][0]
		last = listed[i][-1]
		middle = listed[i][1]
		if len(listed[i]) == 2:
			switched = last, first
			switched_list.append(list(switched))
		else:
			switched = last, middle, first
			switched_list.append(list(switched))
	switched_sorted_list = sorted(switched_list)
	

	final_list = []
	
	for i in range(0, len(switched_sorted_list)):
		first_new = switched_sorted_list[i][0]
		last_new = switched_sorted_list[i][-1]
		middle_new = middle_of_list(switched_sorted_list[i])
		if middle_new != None:
			switched_back = last_new, middle_new, first_new
		else:
			switched_back = last_new, first_new
		final_list.append(list(switched_back))
	
	print final_list

sort_last([(1, 3), (3, 2), (2, 1)])
sort_last([(2, 3), (1, 2), (3, 1)])
sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])


def remove_adjacent(nums):
  new_list = []
  for i in nums:
    if new_list:
      if new_list[-1] != i:
        new_list.append(i)
    else: new_list.append(i)        
  print new_list
  
remove_adjacent([1, 2, 2, 3])
remove_adjacent([2, 2, 3, 3, 3])
remove_adjacent([3, 2, 3, 3, 3])
remove_adjacent([])


def linear_merge(list1, list2):
	list1.extend(list2)
	print sorted(list1)

linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
