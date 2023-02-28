from MyCalc import MyCalc
def test_add():
    calc = MyCalc()
    check = calc.add(2, 2)
    assert check == 4
"""
UCID: np656, Date: 2/272/3. This block is to test the add function in MyCalc 
by calling the function to add 2 numbers, the scenario is 2+2, which should equal 4
"""
def test_ans_add():
    calc = MyCalc()
    ans = calc.add(2, 2)
    check = calc.add(ans, 2)
    assert check == 6
"""
UCID: np656, Date: 2/272/3. This block is to test the add function in MyCalc 
by calling the function to add 2 numbers,in this scenario we are calling the add function from the previous
test, and then setting it to 'ans', and then calling the add function to add ans+2, which should equal 6
"""
def test_sub():
    calc = MyCalc()
    check = calc.sub(10, 2)
    assert check == 8
"""
UCID: np656, Date: 2/272/3. This block is to test the sub function in MyCalc 
by calling the function to subtract 2 numbers, the scenario is 10-2, which should equal 8
"""
def test_ans_sub():
    calc = MyCalc()
    ans = calc.sub(10, 2)
    check = calc.sub(ans, 2)
    assert check == 6
"""
UCID: np656, Date: 2/272/3. This block is to test the sub function in MyCalc 
by calling the function to subtract 2 numbers,in this scenario we are calling the subtract function from the previous
test, and then setting it to 'ans', and then calling the sub function to do ans-2, which should equal 6
"""
def test_mult():
    calc = MyCalc()
    check = calc.mult(2, 5)
    assert check == 10
"""
UCID: np656, Date: 2/272/3. This block is to test the mult function in MyCalc 
by calling the function to multiply 2 numbers, the scenario is 2*5, which should equal 10
"""
def test_ans_mult():
    calc = MyCalc()
    ans = calc.mult(2, 5)
    check = calc.mult(ans, 2)
    assert check == 20
"""
UCID: np656, Date: 2/272/3. This block is to test the mult function in MyCalc 
by calling the function to multiply 2 numbers, the scenario is 2*5, which should equal 10, then setting it 
to ans, and then calling the mult function again to check if it works with ans, ans*2 should equal 20
"""
def test_div():
    calc = MyCalc()
    check = calc.div(50, 5)
    assert check == 10
    """
UCID: np656, Date: 2/272/3. This block is to test the div function in MyCalc 
by calling the function to divide 2 numbers, the scenario is 50/5, which should equal 10
"""
def test_ans_div():
    calc = MyCalc()
    ans = calc.div(50, 5)
    check = calc.div(ans, 5)
    assert check == 2
    """
UCID: np656, Date: 2/272/3. This block is to test the div function in MyCalc 
by calling the function to divide 2 numbers, the scenario is 50/5, which should equal 10, and then setting it 
to ans, and then calling the div function again to check if it works with ans, ans/2 should equal 2
"""
