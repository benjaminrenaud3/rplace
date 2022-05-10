class Pixel:

    def __init__(self):
        self.datetime = "2022-01-01 00:00:00.001 UTC"
        self.user = "user"
        self.color = "#000000"
        self.x = 0
        self.y = 0

    def getinfo(self):
        print (self.datetime, self.user, self.color, self.x, self.y)