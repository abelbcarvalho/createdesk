from src.com.bcarsoft.model.Desk import Desk


class ServiceDesk:
    """Desk Service Class"""

    done: bool

    def __init__(self):
        self.done = False

    # this is the main method

    def set_desktop_launch(self, desk: Desk):
        """MAIN METHOD It create a new  Desktop launcher file"""
        if desk.version < 1:
            return False
        if self.is_none_empty(desk):  # checks there's empty or null strings
            return False
    
    # this is the main method
    
    def is_none_empty(self, desk: Desk):
        """Checks if all strings is valid is None or Empty"""
        self.done = desk.name.__len__() == 0 or desk.name == None
        if self.done:
            return self.done
        self.done = desk.comment.__len__() == 0 or desk.categories == None
        if self.done:
            return self.done
        self.done = desk.execute.__len__() == 0 or desk.execute == None
        if self.done:
            return self.done
        self.done = desk.path.__len__() == 0 or desk.path == None
        if self.done:
            return self.done
        self.done = desk.icon.__len__() == 0 or desk.icon == None
        if self.done:
            return self.done
        self.done = desk.typee.__len__() == 0 or desk.typee == None
        return not self.done
