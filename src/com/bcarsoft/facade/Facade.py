from src.com.bcarsoft.model.Desk import Desk
from src.com.bcarsoft.service.ServiceDesk import ServiceDesk


class Facade:
    """Project Facade Class"""

    service: ServiceDesk

    def __init__(self):
        super().__init__()
        self.service = ServiceDesk()

    def set_desktop_launch(self, desk: Desk):
        """It create a new  Desktop launcher file"""
        return self.service.set_desktop_launch(desk)
