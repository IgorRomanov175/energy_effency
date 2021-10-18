class ThermLogic3:
    def __init__(self, area):
        self.area = area

    def therm_calc1(self, arraylist1, arraylist2):
        j1 = []
        for i in arraylist1:
            b = i[1] / i[0]
            j1.append(b)
        count1 = 0
        for i in j1:
            count1 += i
################################################################
        j2 = []
        for i in arraylist2:
            b = i[1] * i[0]
            j2.append(b)
        count2 = 0
        for i in j2:
            count2 += i

        return self.area / (count1 + count2)