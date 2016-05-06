
class FibonacciStrings(object):
    def __init__(self, first='b', second='a'):
        self.first = first
        self.second = second

    def generate(self, count=-float('inf'), length=-float('inf'), **kwargs):
        if kwargs:
            self.__init__(**kwargs)

        if count == 0:
            return self.first
        elif count == 1:
            return self.second
        elif count == 2:
            return self.second + self.first
        else:
            return self.__recursive__(self.first, self.second, count - 1, length)

    def __recursive__(self, prevprev, prev, count, length):

        if count == 0:
            return prev
        else:
            new = prev + prevprev
            if len(new) >= length:
                return new[:length]

            prevprev = prev
            prev = new
            return self.__recursive__(prevprev, prev, count - 1, length)


if __name__ == "__main__":
    print ("hello")


