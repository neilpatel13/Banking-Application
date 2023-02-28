from MyCalc import MyCalc
def test_add():
    calc = MyCalc()
    check = calc.add(2, 2)
    assert check == 4
def test_ans_add():
    calc = MyCalc()
    ans = calc.add(2, 2)
    check = calc.add(ans, 2)
    assert check == 6

def test_sub():
    calc = MyCalc()
    check = calc.sub(10, 2)
    assert check == 8
def test_ans_sub():
    calc = MyCalc()
    ans = calc.sub(10, 2)
    check = calc.sub(ans, 2)
    assert check == 6

def test_mult():
    calc = MyCalc()
    check = calc.mult(2, 5)
    assert check == 10
def test_ans_mult():
    calc = MyCalc()
    ans = calc.mult(2, 5)
    check = calc.mult(ans, 2)
    assert check == 20

def test_div():
    calc = MyCalc()
    check = calc.div(50, 5)
    assert check == 10
def test_ans_div():
    calc = MyCalc()
    ans = calc.div(50, 5)
    check = calc.div(ans, 5)
    assert check == 2
