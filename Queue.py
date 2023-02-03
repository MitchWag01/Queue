# creating a queue

class Queue:
    """
    Queue Object that allows user to implement a queue
    """
    def __init__(self):
        # List object that is the queue itself, This will store the data values for us
        self.__queue = list()
        self.__length = 0

    def is_Empty(self):
        """
        Purpose:
            To determine if the queue is empty
        Return:
            Boolean - True if it is empty false otherwise
        """
        return len(self.__queue) == 0

    def enqueue(self, item):
        """
        Purpose:
            adds a single item onto the end of the queue
        Conditions:
            item - any type - item to be appended to the queue
        PostConditions
            the queue will now have an item added onto the end.
            the length of the queue will be updated
        Return:
            None
        """
        self.__queue.append(item)
        self.__length += 1

    def dequeue(self):
        """
        Purpose:
            Removes the first value in the queue and returns it to the user
        Conditions:
            Queue must not be empty
        PostConditions:
            The queue will have it's first value removed
        Return:
            any type - value that was at the beginning of the queue
        """
        if self.is_Empty():
            raise IndexError("Cannot delete values from an empty Queue")
        self.__length -= 1
        return self.__queue.pop(0)

    def peek(self):
        """
        Purpose:
            To show the user the very first value in a queue
        Conditions:
            Queue must not be empty
        Return:
            None
        """
        if self.is_Empty():
            raise IndexError("Cannot View first value from an empty Queue")
        return self.__queue[0]

    def size(self):
        """
        Purpose:
            Gets the size of the Queue
        Return:
            int - size of the queue
        """
        return self.__length

    def too_string(self):
        """
        Purpose:
            to print a visual of the queue
        """
        print("Start of queue --> ", end="")
        for values in self.__queue:
            print(values, end=" ")
        print("<-- Last value in queue")


# creating a queue and using it

# create an instance of the Queue -- creating a queue and storing it
our_queue = Queue()

# add values to our queue
our_queue.enqueue(1)
our_queue.enqueue(2)
our_queue.enqueue(3)
our_queue.enqueue(4)

# printing state of our queue
print("current state of queue")
our_queue.too_string()

# viewing first value and deleting 2 values
print(our_queue.peek())
stored_value_first = our_queue.dequeue()
stored_value_second = our_queue.dequeue()

# state of queue after removing values
our_queue.too_string()

# using our saved queue values
print(stored_value_first * stored_value_second)




