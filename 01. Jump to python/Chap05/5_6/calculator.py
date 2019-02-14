class Calculator :
    def __init__(self, list):
        self.parameter = list

    total = 0;
    def sum (self) :
        for i in self.parameter :
            self.total += int(i)
        print(str(self.total))

    avg = 0
    def avg(self):
        self.avg = self.total / self.parameter.__len__()
        print(str(self.avg))

if __name__ == "__main__" :
    cal1 = Calculator([1,2,3,4,5])
    cal1.sum()
    cal1.avg()

    cal2 = Calculator([6,7,8,9,10])
    cal2.sum()
    cal2.avg()