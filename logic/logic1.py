class ThermLogic1:
    def __init__(self, z1, z2):
        self.z1 = z1
        self.z2 = z2

    def therm_calc(self, arraylist):
        j = []
        for i in arraylist:
            b = i[0] / i[1]
            j.append(b)
        count = 0
        for i in j:
            count += i
        return 1 / self.z1 + count + 1 / self.z2
