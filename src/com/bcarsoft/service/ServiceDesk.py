from src.com.bcarsoft.model.Desk import Desk
from src.com.bcarsoft.desktop.Desktop import Desktop


class ServiceDesk:
    """Desk Service Class"""

    done: bool
    getdesk: Desktop

    def __init__(self):
        self.done = False
        self.getdesk = Desktop()

    # this is the main method

    def set_desktop_launch(self, desk: Desk):
        """MAIN METHOD It create a new  Desktop launcher file"""
        if desk.version < 1:
            return False
        if self.is_none_empty(desk):  # checks there's empty or null strings
            return False
        return self.getdesk.set_desktop_launch(desk)
    
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
        if self.done:
            return self.done
        return self.done
