class AuxService:
    cate: dict
    lword: list
    
    def __init__(self):
        self.cate = {
            1: 'AudioVideo',
            2: 'Audio',
            3: 'Video',
            4: 'Development',
            5: 'Education',
            6: 'Game',
            7: 'Graphics',
            8: 'Network',
            9: 'Office',
            10: 'Science',
            11: 'Settings',
            12: 'System',
            13: 'Utility'
        }
        self.lword = []
    
    def take_sami_common(self, word: str):
        """This method returns a list of words without semicommon"""
        aux = ''
        for i in word:
            if i.isalpha():
                aux += i
            elif i.__eq__(';'):
                self.lword.append(aux)
                aux = ''
        return self.lword
