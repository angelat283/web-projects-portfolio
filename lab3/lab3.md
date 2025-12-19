# Reflection for Lab 3

## Part A: Analysis

### function 1:
This function checks two base cases (number == 0 or number == 1), both of which are constant-time. Every other case multiplies the value by another recursive call with number-1. That means each call does a small amount of work and then calls itself again until it reaches 0 or 1.
So the recurrence is T(n) = T(n-1) + O(1), which grows linearly.
Big-O = O(n).

```python
def function1(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		return value * function1(value, number-1)
```

### function 2:
Here the function compares two characters at a time, one from the front and one from the back of the string. If they’re the same, it makes another call moving inward. Each call does a few constant operations (about 4), but the string length shrinks by 2 each time.
So the recurrence is T(n) = T(n-2) + O(1), which still works out to linear growth.
Big-O = O(n).

```python

def recursive_function2(mystring,a, b):
	if(a >= b ):
		return True
	else:
		if(mystring[a] != mystring[b]):
			return False
		else:
			return recursive_function2(mystring,a+1,b-1)

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)

```

### function 3 (optional):
This function is smarter because it cuts the problem in half by using number // 2. Each call does only a small amount of work, and then calls itself on half the input. That means the recursion depth is only about log₂(n).
So the recurrence is T(n) = T(n/2) + O(1).
Big-O = O(log n).

```python
def function3(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		half = number // 2
		result = function3(value, half)
		if (number % 2 == 0):
			return result * result
		else:
			return value * result * result

```

## Part C reflection

Answer the following questions

1. Describe the process of analyzing recursive functions.  How does it differ from from analyzing non-recursive functions?  How is it the same?When I analyze recursion, I always look for the base case first, then figure out how much work is happening in each recursive step. After that, I write the recurrence relation and simplify it to Big-O. The difference from a normal (non-recursive) function is that I can’t just add operations in a straight line — I need to think about how many times the function calls itself. But at the end of the day, it’s the same idea: count the work, simplify it, and describe the growth.
2. Described what you learned in the implementation for the linked lists.  What approach did you take?  What bugs did you find most difficult to fix.
For the doubly linked list, I started by writing the Node class and then moved on to building the list methods one at a time. I tested as I went, instead of trying to do everything at once. The hardest part was getting the next and prev pointers updated correctly — if I forgot one, the list would break. Another thing that tripped me up was handling empty lists, since I had to raise IndexError exactly the way the instructions said.

I also noticed that using sentinel nodes made life easier, because I didn’t need to check for None so often. Overall, it was a good exercise in being careful with small details, since one missing pointer update can mess up the whole list.


