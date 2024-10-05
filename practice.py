class Cookie:
    def __init__(self, color):
        self.color=color
    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color=color

    
cookie_1 = Cookie('green')
cookie_2 = Cookie('red')

print('cookie one is',cookie_1.getColor())
print('cookie 2 is',cookie_2.getColor())

cookie_1.setColor('orange')

print('cookie one is',cookie_1.getColor())
print('cookie 2 is',cookie_2.getColor())
