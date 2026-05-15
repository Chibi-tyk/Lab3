import employee_info as info

def test_calc_avg():
    expected_result = 60166.67
    result =info.calculate_average_salary()
    assert (round(result,2) == expected_result)

def test_get_employee_by_dept():
    expected_result = [info.employee_data[1], info.employee_data[2]]
    result = info.get_employees_by_dept("Marketing")
    assert (result == expected_result)

def test_get_by_range():
    expected_result = [info.employee_data[0], info.employee_data[3], info.employee_data[4]]
    result = info.get_employees_by_age_range(25, 30)
    assert (result == expected_result)