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

## Associated Functions

<p>&nbsp;</p>

* Adding to a tree
* Display all values forward in a tree
* Display all values backwards in a tree

## Example Problems
- basic overview of tree functions
- Finding and replacing value (resetting tree if needed)

## First Problem
- Adding to trees
- Removing from tree
- Finding value

## Find/Replace Value
- finding value (what is performance?)
- Replacing value (setting new values and references)
- Resetting tree to fix up size of tree

## Possible Problems
- Talking about recursion
- Problems may be too simple
- Creating code content

Return to [introduction](introduction.md) file.
