import Lab2.ex1_bmi as bmi 

def test_bmi_under_weight():
    expected_result = -1 
    result = bmi.calculate_bmi(1.73,40)
    assert (result == expected_result)

def test_bmi_over_weight():
    expected_result = 1
    result = bmi.calculate_bmi(1.73,90)
    assert(result == expected_result)

def test_bmi_normal_weight():
    expected_result = 0
    result = bmi.calculate_bmi(2.0,100)
    assert(result == expected_result)