# Trees File

# What are trees
- Outline of how trees look
- BST and associated functions
- Recap on recursion
- Performance of trees

## Trees (What Are They?)
Trees are another way to store data. There is the root (top of tree) and then there are branches.  
The start of each branch is called the 'parent.' The next set of data is called the 'child.' When  
data is insert into the tree, they are insert into a node that is part of the tree. Data is  
automatically sorted and placed into the tree based on the value of the parent.  

In this image below, the tree starts out at 10. This is the base number of all the values being  
input. Then, 5 is added, and since it is less than 10, it goes to the left. Then, 30 is insert,  
and since it is bigger than 30, it goes to the right. When 4 is added, it is less than 10, so it  
goes left. 4 is less than 5, so it goes to the left of 5.  

When 8 is added, the same thing happens. 8 is less than 10, so it goes left. 8 is greater than 5,  
so it goes to the right of 5. 

A simple way to explain would be this: a new value that is entered into the BST starts at the root,  
or the first number in the tree. It evaluates if the new value is bigger than or less than the root  
value, and if it is bigger than the value, then the new value goes to the right. If the new value  
is smaller, then it goes to the left. When the new value arrives at a new level of the tree, it  
evaluates the value at that point, and moves either left or right just like when evaluating the root  
of the BST.  

<p>&nbsp;</p>

![BST](bst_image.jpg)

<p>&nbsp;</p>

## Recursion

When working with BST, one of the key factors is using *recursion*, which is a function calling itself  
to solve a problem. For example, when working with factorials (#!), this means multiply all of the  
values from 1 to # by each other. If I wanted to do 10!, it would be something like this:

```python
# DISCLAIMER! This is not how to actually code a factorial, but is a good visual instead.
var x = 10!

x = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
```

<p>&nbsp;</p>

This means 10! would be equal to 3,628,800! That is a really big number. 

If we wanted to code this using recursion, it would look like this:

<p>&nbsp;</p>

```python

# create a function to find a factorial
def factorial(number):
    if number == 1:
        return number
    else:
        result = number * factorial(number-1)
    return result

factorial(10)
```

<p>&nbsp;</p>

Recursion is dependent on two things. One is the base case, or the ending case, and then the function  
call. The base case is what determines when the function should stop running. The function call holds  
what data is going to be returned, as well as calling the function. When calling the function, the  
value being used needs to be decremented. If the value is not decremented, then that would create a  
never ending condition, which is not good.  

<p>&nbsp;</p>

## Associated Functions

<p>&nbsp;</p>

For a BST, we are going to use classes to implement the tree. We will use the following code.  

<p>&nbsp;</p>

```python

class BST:

    class Node:

        def __init__(self, data):
            # set the data to be the root. Links are None 
            # because they are unkown.
            self.data = data
            self.left = None
            self.right = None
    
    def __init__(self):
        # Set the root to be None because it is empty

        self.root = None
    
    def insert(self, data):

        if self.root is None:



```

When adding to a tree, the root value must be evaluated by the value to be insert. 




* Adding to a tree
* Display all values forward in a tree
* Display all values backwards in a tree



## Possible Problems
- Talking about recursion
- Problems may be too simple
- Creating code content

Return to [introduction](introduction.md) file.
