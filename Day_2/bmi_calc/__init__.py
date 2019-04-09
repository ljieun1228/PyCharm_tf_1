from bmi_calc.bmi import Bmi


def main():
    bmi = Bmi(float(input("키 입력")),float(input("몸무게 입력")),input("이름 입력"))

    print("{}님의 BMI지수 {}입니다.".format(bmi.name,bmi.bmi()))

if __name__ == '__main__':
    main()