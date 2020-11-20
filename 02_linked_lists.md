# Linked List

## What to talk about
 - Design of linked list (include image)
 - How does it link to each other
 - How does it save memory (uses space in memory instead of array of data)
 - When to use it
 - performance
 
 ## Possible Practice Problems
 - Blockchain example of confirming payments (one person buys something, and is confirmed by other person/business)
 - something else :)
 
 ## Blockchain Example
 - Maybe scrap this example

 ```python

 class Blockchain:
    """
    Create a blockchain using a linked list. This simple list uses
    other data in the list to confirm transactions between users. 
    """

    class Data:
        def __init__(self, balance):
            # purpose of balance is to confirm balance of user
            # next and prev are to confirm if the transaction is valid
            self.balance = balance
            self.next = None
            self.prev = None

    def __init__(self):
        # what data do I need?
        # make a head and tail (start and stop)
        self.head = None
        self.tail = None

    def create_data(self, value):

        # create Data value
        new_balance = Blockchain.Data(value)

        if self.head is None or self.tail is None:
            self.head = 


 ```
 
 Develop better ideas and think about it a lot. Create new content problems in the week.

Return to [introduction](introduction.md) file.
