"""A module designed to manage personalized exceptions for the library."""

class EmptyListError(Exception):
    """ A case where a list is expected to have at least one element but found none. """
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
     
    def __str__(self):
        if self.message:
            return 'EmptyListError: {0}'.format(self.message)
        else:
            return "EmptyListError: List size can't be 0."
        
