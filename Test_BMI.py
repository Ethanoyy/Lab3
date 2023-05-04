import PHYCHARM.lab2 as bmi
def test_BMI_Overweight():
    result = bmi.CalcuBMI(1.6, 90)
    assert(result==1)

def test_BMI_Underweight():
    result = bmi.CalcuBMI(1.6, 10)
    assert(result==-1)

def test_BMI_Normalweight():
    result = bmi.CalcuBMI(1.8, 65)
    assert(result==0)