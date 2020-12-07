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

The \_\_str\_\_() function is added to make the queue output a lot easier to read  
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

### Adding To a Queue
When adding to a queue, this is a simple O(1) performance. A queue works off of FIFO (First in First out)  
which means the first item to be added is the first item to be removed. In the image above, the first number is 1, then 2,  
and so forth. When the number 5 was added, it was added at the end of the queue. 

To add to a queue, the code would have to do the following:
  * create a new node to hold the value
  * add the new value to the end of the queue
```python
    # create a function to add values to a queue
    def enqueue(self, value):
        new_node = Queue.Node(value)
        self.queue.append(new_node)
```

### Removing From a Queue
Removing from a queue is similar, but has an O(n) performance. Removing the first item in a queue  
causes the rest of the queue to shift over to the left, filling in that first item that was removed.  
If there are a million and one values and the first one is removed, then one million  
values have to be moved over. That is a lot of data, and that is a lot of data to be moved.  

Removing from a queue is not very hard. As mentioned earlier, it can be very performance heavy  
since it has to remove a value and shift over all of the other values. Try to do the following:
  * Set a value as the value to be removed
  * Delete the value from the queue
  * Print out the value dequeued (This is not required, but makes it more user friendly to see what is removed)
```python
    # write a dequeue function
    def dequeue(self):

        # set a var as the value to be removed
        removal = self.queue[0]
        del self.queue[0]
        print(f'The value being removed is {removal}.\n')
```

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

## When to Use a Queue
* When working with lines of people
* Orders in Fast Food
* Anything with order where the first person should leave first

Possible problems:
1. creating the classes to store student information
2. what happens if the class is full?

Is there anything else to write about?

Return to [introduction](introduction.md) file.
