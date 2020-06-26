from src.com.bcarsoft.model.Desk import Desk
from src.com.bcarsoft.desktop.Struct import Struct


class Desktop(Struct):
    """This Class Can Create the .desktop File"""

    def __init__(self):
        super().__init__()
    
    def set_desktop_launch(self, desk: Desk):
        """MAIN METHOD It create a new  Desktop launcher file"""
        self.data[1] = self.data[1]+desk.version.__str__()
        self.data[2] = self.data[2]+desk.name
        self.data[3] = self.data[3]+desk.comment
        self.data[4] = self.data[4]+desk.execute
        self.data[5] = self.data[5]+desk.path
        self.data[6] = self.data[6]+desk.icon
        self.data[7] = self.data[7]+desk.terminal.__str__()
        self.data[8] = self.data[8]+desk.typee
        self.data[9] = self.data[9]+desk.categories[0]
        for i in range(1,desk.categories.__len__(),1):
            self.data[9] = self.data[9]+','+desk.categories[i]
        self.create_desktop(desk)
        return self.data

    def create_desktop(self, desk: Desk):
        """Open file and create it"""
        way = './launchers/'
        way += desk.name
        way += '.desktop'
        file = open(way,"w")
        for i in range(10):
            file.write(self.data[i]+'\n')
        file.close()
