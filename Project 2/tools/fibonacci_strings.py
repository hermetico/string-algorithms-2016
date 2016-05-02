
class FibonacciStrings(object):
    def __init__(self, first='b', second='a'):
        self.first = first
        self.second = second

    def generate(self, length=0, **kwargs):
        if kwargs:
            self.__init__(**kwargs)

        if length == 0:
            return self.first
        elif length == 1:
            return self.second
        elif length == 2:
            return self.second + self.first
        else:
            return self.__recursive__(self.first, self.second, length - 1)

    def __recursive__(self, prevprev, prev, count):

        if count == 0:
            return prev
        else:
            new = prev + prevprev
            prevprev = prev
            prev = new
            return self.__recursive__(prevprev, prev, count - 1 )


if __name__ == "__main__":
    print ("hello")


