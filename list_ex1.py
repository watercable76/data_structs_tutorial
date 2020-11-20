"""
Date Created: 11/20/2020
Author: Nicholas Cable, el cablecito
Purpose: Create a fully functional linked list in order to further
        personal knowledge and prepare to teach peers about data
        structures in Python.

"""


class Linked_list:
    """
    Create a linked list that holds the values of the head and the tail. Any other data
    to be held here will be within the inner class Data.
    """

    class Data:
        """
        Here will be the values held in the list. There will also be references to
        the next itmes in the linked list.
        """

        # define the values held and the references to the next item in the list
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

    # define the head and tail of the linked list
    def __init__(self):
        self.head = None
        self.tail = None

    # function to insert into list
    # user will specify if the item is to be placed in head or tail (one function for two purposes)
    def insert(self, value, place):
        # create a var to store the new data
        # change the var name later
        stuff = Linked_list.Data(value)

        # if there is no data, set the head and tail as the new data
        if self.head is None and self.tail is None:
            self.head = stuff
            self.tail = stuff

        else:
            # if place is 'head'
            if place.lower() == 'head':
                stuff.next = self.head    # connnect the old head to the new data
                self.head.prev = stuff    # connect the previous head to the new data
                self.head = stuff         # set the head to the new data

            elif place.lower() == 'tail':
                stuff.prev = self.tail    # connect the old tail to the new data
                self.tail.next = stuff    # connect the previous tail to the new data
                self.tail = stuff         # set the tail to the new data

    # create a function to sum all values in the list
    # not currently returning anything, so need more work on this later
    # was returning a value when I should be printing it out
    def sumation(self):
        now = self.head
        total = 0
        while now is not None:
            # yield now.value - do not use yield at all
            total += now.value
            now = now.next

        # return the total
        print('The total is: ' + str(total))

    # create an iter function to run through code
    def __iter__(self):

        curr = self.head
        while curr is not None:
            yield curr.value
            curr = curr.next

    # create a str function to make ouputting the linked list understandable
    def __str__(self):
        # modify the string output so it is understandable
        output = "linkedlist["
        first = True

        # run through the list
        for value in self:
            # if is the first value, set first as false and then continue with loop
            if first:
                first = False
            else:
                output += ", "
            # add the value of the list value to output
            output += str(value)
        # close brackets when outputting the list
        output += "]"
        return output


# Test cases!

# Different ways of formatting the label for test cases
# case1 = ' TEST CASE 1 '
# print("{:=^40}\n".format(' TEST CASE 1 '))
# print(f"{case1:=^40}\n")
print(f"{' TEST CASE 1 ':=^40}\n")
cool = Linked_list()
cool.insert(10, "head")
cool.insert(5, "head")
print(cool)

cool.sumation()
