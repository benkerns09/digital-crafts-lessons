class Balloon(object):#object means you can acces the properties of the class #this is global -- every object should inherit from this
    def __init__(self, color, size, shape):#every balloon class is going to run this "dunder init" function. "Self" in this case is tha balloon
        self.color = color
        self.size = size
        self.shape = shape
        self.inflated = False #bydefaultitisnotinflated2start
        self.working = True

    def inflate(self):
        if self.working:
            self.inflated = True
        else:# else is just like saying "otherwise"
            print "You exploded this balloon. Itiot."

    def explode(self):
        self.inflated = False
        self.working = False
        print "Bang!"

    def deflate(self):
        self.inflated = False

class big_balloon(Balloon):
    def __init__(self, color, shape):
        super(Balloon, self).__init__(self.color, 'Big', shape)
        self.color = color
        self.size = size
        self.shape = shape
        self.inflated = False #bydefaultitisnotinflated2start
        self.working = True

big_balloon = Balloon("red", "big", "round") #these two variables are both balloons but they are not the same.
balloon2 = Balloon("blue", "small", "square")
balloon = BigBalloon('green', 'round')
balloon.paint('red')