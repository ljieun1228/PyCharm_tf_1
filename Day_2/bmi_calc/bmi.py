class Bmi:

    def __init__(self,w, h, name):
        self.w = w
        self.h = h
        self.name = name

    def bmi(self):
        bmi = (self.w/((self.h/100)*(self.h/100)))

        if bmi >= 40:
            res = "고도비만"
        elif bmi >= 35:
            res = "중증도비만"
        elif bmi >= 30:
            res = "경도비만"
        elif bmi >= 25:
            res = "과체중"
        elif bmi >= 18.5:
            res = "정상"
        else: res = "저체중"

        return res
