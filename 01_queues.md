# Queues in Python
Created November 16, 2020
Last Edited: 11/17/2020

## Define 
- a queue
- performance of a queue
- how to implement queues
- FIFO

What is a queue?

A queue looks like the following.  
![Simple Queue](queue_image.jpg)

## Performance of a queue
A queue has a O(n) performance due to the structure of the data structure.  
Since a queue is basically a list, looping through the list would be a O(n) performance  
because to go through every item in the queue, a for loop needs to be used.  

Displaying the queue will require a few things. In these examples, we will use the following  
code to create the new queues. The first class is Queue, and the queue will be held in
the queue class. Each value being added will be added through the Node class.  

The __str__() function is added to make the queue output a lot easier to read  
or understand.

```python
class Queue:
    """
    This class holds the basic outline of a queue []. The main functions will
    be declared here.
    """

    class Node:
        """
        This will hold the data of the queue. For now, there will only be one
        value held in the __init__().
        """

        def __init__(self, value):
            self.value = value

        # need __str__ to print out object's value
        # if this is not added, would return place in memory of object
        def __str__(self):
            return f'{self.value}'

    # define the class as being a []
    def __init__(self):
        self.queue = []
    
    # str function overwrite
    # return str(node) to make everything string
    # (who knows what values could be put in here)
    def __str__(self):
        result = '['
        for node in self.queue:
            result += str(node) + ', '
        result = result[:-2]
        result += ']'
        return result

```


When adding to a queue, this is a simple O(1) performance. A queue works off of FIFO (First in First out)  
which means the first item to be added is the first item to be removed. In the image above, the first number is 1, then 2,  
and so forth. When the number 5 was added, it was added at the end of the queue. 

## Two problems completed and made by me (first one needs to be completely solved and solution displayed)
- how to add to a queue
- removing from a queue

## real life example of queue for registering for classes
- input people who sign up for class
- register their id
- date they sign up for class

```python
class Class_Registration:

  class Student:
    
    def __init__(self, name, id, date):
      self.name = name
      self.id = id
      self.date = date
  
  def __init__():
    self.queue = []
   
  def enqueue(self, name, id, date):
  
    # can I create a dictionary inside a queue?
    if len(self.queue) is None:
      # create dictionary inside the list?


```

Possible problems:
1. creating the classes to store student information
2. what happens if the class is full?

Is there anything else to write about?

Return to [introduction](introduction.md) file.
