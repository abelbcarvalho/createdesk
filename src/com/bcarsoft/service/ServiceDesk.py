from src.com.bcarsoft.model.Desk import Desk
from src.com.bcarsoft.desktop.Desktop import Desktop
from src.com.bcarsoft.service.AuxService import AuxService


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
        try:
            if desk.version < 1:
                return False
            if self.is_none_empty(desk):  # checks there's empty or null strings
                return False
            if not self.is_category_valid_basic(desk):
                return False
            if not self.is_category_valid_advenced(desk):
                return False
            return self.getdesk.set_desktop_launch(desk)
        except ValueError:
            return False
    
    # this is the main method
    
    def is_none_empty(self, desk: Desk):
        """Checks if all strings is valid is None or Empty"""
        self.done = desk.name.__len__() == 0 or desk.name == None
        if self.done:
            return self.done
        self.done = desk.execute.__len__() == 0 or desk.execute == None
        if self.done:
            return self.done
        self.done = desk.terminal.__len__() == 0 or desk.terminal == None
        if self.done:
            return self.done
        self.done = desk.typee.__len__() == 0 or desk.typee == None
        if self.done:
            return self.done
        return self.done
    
    def is_category_valid_basic(self, desk: Desk):
        """This method checks if category is valid"""
        word = list(desk.categories)
        if not word[0].isalpha():
            return False
        if not word[word.__len__()-1].__eq__(';'):
            return False
        for i in word:
            if not i.isalpha() and not i.__eq__(';'):
                return False
        return True
    
    def is_category_valid_advenced(self, desk: Desk):
        """This method checks if the caregories are really valids"""
        auxs = AuxService()
        lword = auxs.take_sami_common(desk.categories)
        for i in lword:
            b = 1
            key = False
            while b < 14:
                if i.__eq__(auxs.cate[b]):
                    key = True
                b += 1
            if not key:
                return False
        return True
