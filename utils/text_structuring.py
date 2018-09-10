'''
parse text into structured data

目前是使用的 duckling 库
参考: 
    https://github.com/facebook/duckling
    https://github.com/FraBle/python-duckling
'''

import duckling

class TextStructuring:
    
    def __init__(self):
        self.parser = duckling.Duckling()
        self.parser.load(languages=[duckling.Language.CHINESE])
    
    def parse(self, text):
        return self.parser.parse(text, language=duckling.Language.CHINESE)


if __name__ == "__main__":
    ts = TextStructuring()
    print(ts.parse("明天10点"))
