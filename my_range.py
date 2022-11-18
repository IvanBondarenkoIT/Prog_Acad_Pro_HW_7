class MyRange:
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.step = 1

    def range(self, *args):
        match len(args):
            case 3:
                self.begin = args[0]
                self.end = args[1]
                self.step = args[2]
            case 2:
                self.begin = args[0]
                self.end = args[1]
            case 1:
                self.end = args[0]
            case 0:
                raise AttributeError

        if not (isinstance(self.begin, int) and
                isinstance(self.end, int) and
                isinstance(self.step, int)):
            raise TypeError

        __val = self.begin
        while __val < self.end:
            yield __val
            __val += self.step


