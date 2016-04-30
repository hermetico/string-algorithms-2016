
class FibonacciStrings(object):
    def __init__(self, first='b', second='a', length=float('inf')):
        self.first = first
        self.second = second
        self.length = length

    def generate(self, count=0, **kwargs):
        if kwargs:
            self.__init__(**kwargs)

        if count == 0:
            return self.first
        elif count == 1:
            return self.second
        elif count == 2:
            return self.second + self.first
        else:
            return self.__recursive__(self.first, self.second, count - 1)

    def generate_length(self, length=1, **kwargs):
        if kwargs:
            self.__init__(**kwargs)
        return self.__recursive__(self.first, self.second, float('inf'), length)


    def __recursive__(self, prevprev, prev, count, length=float('inf')):

        if count == 0 or len(prev)>=length:
            if len(prev) > length:
                return prev[:length]
            return prev
        else:
            new = prev + prevprev
            prevprev = prev
            prev = new
            return self.__recursive__(prevprev, prev, count - 1, length)


if __name__ == "__main__":
    fbs = FibonacciStrings()
    print fbs.generate(20)
    print fbs.generate_length(50)


