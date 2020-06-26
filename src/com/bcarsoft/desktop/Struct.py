class Struct:
    """This class has the .desktop structure"""
    
    data: dict

    def __init__(self):
        self.data = {
            0: "[Desktop Entry]",
            1: "Version=",
            2: "Name=",
            3: "Comment=",
            4: "Exec=",
            5: "Path=",
            6: "Icon=",
            7: "Terminal=",
            8: "Type=",
            9: "Categories="
        }

