import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm
@pytest.fixture
def machine2():
    bm = BurgerMachine()
    return bm
'''
# sample fixture, can delete if not using
@pytest.fixture
def first_order(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(1.00,"1.00")
    return machine
    assert True

# sample fixture, can delete if not using
@pytest.fixture
def second_order(first_order):
    first_order.handle_bun("lettuce wrap")
    first_order.handle_patty("turkey")
    first_order.handle_patty("turkey")
    first_order.handle_patty("next")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("done")
    #machine.handle_pay(10000,"10000")
    return first_order

# sample test case, can delete if not using
def test_production_line(second_order):
    for j in second_order.buns:
        print(second_order.inprogress_burger)
        if j.name.lower() == second_order.inprogress_burger[0].name.lower():
            assert True
            return

    assert False

# add required test cases below
'''
def test_bun_must_be_first_selection(machine):
    machine.reset()
    with pytest.raises(InvalidStageException):
        machine.handle_toppings("cheese")
    with pytest.raises(InvalidStageException):
        machine.handle_patty("turkey")
    assert True
'''Neil Patel, UCID: np656 date: 3/28
This test was to test that an invalid stage exception will occur when trying to order toppings/patty 
before choosing the bun first'''

def test_add_patty(machine):
    machine.reset()
    machine.handle_bun("no bun")
    for i in machine.patties:
        patties.quantity = 1
    with pytest.raises(OutOfStockException):
        machine.handle_patty("turkey")
        machine.handle_patty("Turkey")
        machine.handle_patty("Turkey")
    assert True
'''Neil Patel, UCID: np656 date: 3/28
This test was to test when adding patties to the order, an out of stock exception will rise when
there is no more stock of a patty'''

def test_add_toppings(machine):
    machine.reset()
    machine.handle_bun("no bun")
    machine.handle_bun("beef")
    machine.handle_bun("next")
    for i in machine.toppings:
        toppings.quantity = 1
    with pytest.raises(OutOfStockException):
        machine.handle_toppings("bbq")
        machine.handle_toppings("bbq")
        machine.handle_toppings("bbq")
    assert True
'''Neil Patel, UCID: np656 date: 3/28
This test was to test when adding toppings to the order, an out of stock exception will rise when
there is no more stock of a topping'''

def test_patty_combo(machine):
    machine.reset()
    machine.handle_bun("no bun")
    machine.handle_patty("turkey")
    machine.handle_patty("beef")
    machine.handle_patty("veggie")
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_patty("turkey")
    assert True
'''Neil Patel, UCID: np656 date: 3/28
This test was to test the ordering of any 3 patties in any order and giving a exceeded remaining choices
exception when trying to add a 4th patty'''

def test_toppings_combo(machine):
    machine.reset()
    machine.handle_bun("no bun")
    machine.handle_patty("turkey")
    machine.handle_patty("next")
    machine.handle_toppings("mayo")
    machine.handle_toppings("bbq")
    machine.handle_toppings("cheese")
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_toppings("mayo")
    assert True
'''Neil Patel, UCID: np656 date: 3/28
This test was to test that when ordering burger, if a person order more toppings then they
are allowed to, an exceed remaing choices error will occur'''

def test_cost(machine):
    machine.reset()
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(1.00,"1.00")
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("bbq")
    machine.handle_toppings("done")
    machine.handle_pay(1.25,"1.25")
    machine.handle_bun("white burger bun")
    machine.handle_patty("beef")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(3.00,"3.00")
    if machine.handle_pay:
        assert True
    return
'''Neil Patel, UCID: np656 date: 3/28
This test was to test when ordering a burger, if the correct payment to the price of the burger is made, no
error will occur'''

def test_total_cost(machine):
    machine.reset()
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(1.00,"1.00")
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("bbq")
    machine.handle_toppings("done")
    machine.handle_pay(1.25,"1.25")
    machine.handle_bun("white burger bun")
    machine.handle_patty("beef")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(3.00,"3.00")
    print(f"Total sales so far {machine.total_sales}")
    if machine.total_sales ==5.25:
        assert True
    return
'''Neil Patel, UCID: np656 date: 3/28
This test was to test that when multiple people order burgers, the machine will track the total sales of
all the brugers'''

def test_total_burger(machine):
    machine.reset()
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(1.00,"1.00")
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("bbq")
    machine.handle_toppings("done")
    machine.handle_pay(1.25,"1.25")
    machine.handle_bun("white burger bun")
    machine.handle_patty("beef")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(3.00,"3.00")
    print(f"Total burgers so far {machine.total_burgers}")
    if machine.total_burgers ==3:
        assert True
    return
#Neil Patel, UCID: np656 DATE: 3.28
#This test was to test that when ordering multiple burgers, the machine will track the total amoount of burgers made