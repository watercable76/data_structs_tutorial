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
```python
class Queue:
  def __init__(self):
    self.queue = []
  
  # adding to a queue
  def enqueue(self, value):
    self.queue.append(value)
  
  # removing from a queue
  # remove using del[] to be more professional
  # do I need to return value or just print it out?
  def dequeue(self):
    removal = self.queue[0]
    del self.queue[0]
    return removal
```

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
