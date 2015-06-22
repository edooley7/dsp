# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

[![Think Python](img/think_python.png)](http://www.greenteapress.com/thinkpython/)

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

Complete the following exercises to check your ability with Python.

These exercises are implemented with doctests, which are runnable tests inside docstrings. Fill in the function definitions. Correct solutions will make it possible to run (for example) `python -m doctest strings.py` with no messages about failures.

 * [Strings](python/strings.py)
 * [Lists](python/lists.py)


---

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>Lists can be changed, tuples cannot (although you could create a new tuple using parts of the old tuple.) Tuples can be keys in dictionaries, lists cannot.  Dictionary keys must be immutable, and lists are mutable.

---


---

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>Lists maintain order, while sets do not.  Items in a set must be immutable, items in a list do not have to be.  Sets cannot have duplicate values, lists can. I would use a list if I had something that had to be kept in order or had duplicate values, otherwise I would use a set.  

For example:
```
list1 = [1, 1, 2, 5, 4]
set1 = set(list1)
```
Results in:
```
[1, 1, 2, 5, 4]
set([1, 2, 4, 5])
```

>Sets are faster for finding an element because there aren't any duplicates.
---


---

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>Lambda is a way to create a quick throwaway function.  

---


---

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>List comprehensions are a quick way to create a new list.  You could use a list comprehension to create a list where each element is the result of an operation on a range. 

```
list1 = [1, 2, 3, 4, 5]

#Regular (squares all items in list)
def regular(s):
	squared_list = []
	for x in s:
		squared_list.append(x**2)
	return squared_list
		
#List Comprehension (squares all items in list)
def list_comprehension(s):
	squared_list = [x**2 for x in s]
	return squared_list
	
#Map (squares all items in list)
def map_test(s):
	squared_list = map(lambda x: x**2, s)
	return squared_list
	
#Filter (finds items in s that are even)
def filter_test(s):
	even_list = filter(lambda x: x%2 == 0, s)
	return even_list

print regular(list1)
print list_comprehension(list1)
print map_test(list1)
print filter_test(list1)
```

```
#Set Comprehension
set1 = set(list1)

def set_comprehension(s):
	squared_set = {x**2 for x in s}
	return squared_set
	
print set_comprehension(set1)

#Dictionary Comprehension
def dict_comprehension(s):
	squared_dict = {x: x**2 for x in set1}
	return squared_dict
	
print dict_comprehension(set1)
```
---


Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

```bash
./markov.py chains.txt 40
```

A possible output would be:

> show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.
