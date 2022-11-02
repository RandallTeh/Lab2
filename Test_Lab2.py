import Lab2

def test_get_user_input():
    test_values = '2, 8'
    test_ans = [2.0, 8.0]

    result = Lab2.get_user_input(test_values)

    assert( result == test_ans )

def test_calc_average():
    test_values = [2.0, 8.0]
    test_ans = 5

    result = Lab2.calc_average(test_values)

    assert( result == test_ans )