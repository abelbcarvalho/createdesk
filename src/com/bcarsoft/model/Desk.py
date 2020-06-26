class Desk:
    """Desk Model Class"""
    
    version: float
    name: str
    comment: str
    execute: str
    path: str
    icon: str
    terminal: bool
    typee: str
    categories: list

    def __init__(self):
        self.version = 0.0
        self.name = ""
        self.execute = ""
        self.path = ""
        self.icon = ""
        self.terminal = False
        self.typee = ""
        self.categories = []

