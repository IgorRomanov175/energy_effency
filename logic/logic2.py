class ThermLogic2:
    def __init__(self, z_zero):
        self.z_zero = z_zero

    def therm_calc(self, arraylist):
        j = []
        for i in arraylist:
            b = i[0] / i[1]
            j.append(b)
        count = 0
        for i in j:
            count += i
        return self.z_zero + count
