from enum import Enum
import sys
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, NeedsCleaningException, OutOfStockException
from BurgerMachineExceptions import InvalidPaymentException

class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity = 10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if (self.quantity < 0):
            raise OutOfStockException
        return self.quantity 

    def in_stock(self):
        return self.quantity > 0
    def __repr__(self) -> str:
        return self.name

class Bun(Usable):
    pass

class Patty(Usable):
    pass

class Topping(Usable):
    pass

class STAGE(Enum):
    Bun = 1
    Patty = 2
    Toppings = 3
    Pay = 4

class BurgerMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 15
    MAX_PATTIES = 3
    MAX_TOPPINGS = 3


    buns = [Bun(name="No Bun", cost=0), Bun(name="White Burger Bun", cost=1), Bun("Wheat Burger Bun", cost=1.25),Bun("Lettuce Wrap", cost=1.5)]
    patties = [Patty(name="Turkey", quantity=10, cost=1), Patty(name="Veggie", quantity=10, cost=1), Patty(name="Beef", quantity=10, cost=1)]
    toppings = [Topping(name="Lettuce", quantity=10, cost=.25), Topping(name="Tomato", quantity=10, cost=.25), Topping(name="Pickles", quantity=10, cost=.25), \
    Topping(name="Cheese", quantity=10, cost=.25), Topping(name="Ketchup", quantity=10, cost=.25),
     Topping(name="Mayo", quantity=10, cost=.25), Topping(name="Mustard", quantity=10, cost=.25),Topping(name="BBQ", quantity=10, cost=.25)] 


    # variables
    remaining_uses = USES_UNTIL_CLEANING
    remaining_patties = MAX_PATTIES
    remaining_toppings = MAX_TOPPINGS
    total_sales = 0
    total_burgers = 0

    inprogress_burger = []
    currently_selecting = STAGE.Bun

    # rules
    # 1 - bun must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - patties can't exceed max
    # 4 - toppings can't exceed max
    # 5 - proper cost must be calculated and shown to the user
    # 6 - cleaning must be done after certain number of uses before any more burgers can be made
    # 7 - total sales should calculate properly based on cost calculation
    # 8 - total_burgers should increment properly after a payment
    

    def pick_bun(self, choice):
        if self.currently_selecting != STAGE.Bun:
            raise InvalidStageException
        for c in self.buns:
            if c.name.lower() == choice.lower():
                c.use()
                self.inprogress_burger.append(c)
                return
        raise InvalidChoiceException

    def pick_patty(self, choice):
        if self.currently_selecting != STAGE.Patty:
            raise InvalidStageException
        if self.remaining_uses <= 0:
            raise NeedsCleaningException
        if self.remaining_patties <= 0:
            raise ExceededRemainingChoicesException
        for f in self.patties:
            if f.name.lower() == choice.lower():
                f.use()
                self.inprogress_burger.append(f)
                self.remaining_patties -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException

    def pick_toppings(self, choice):
        if self.currently_selecting != STAGE.Toppings:
            raise InvalidStageException
        if self.remaining_toppings <= 0:
            raise ExceededRemainingChoicesException
        for t in self.toppings:
            if t.name.lower() == choice.lower():
                t.use()
                self.inprogress_burger.append(t)
                self.remaining_toppings -= 1
                return
        raise InvalidChoiceException

    def reset(self):
        self.remaining_patties = self.MAX_PATTIES
        self.remaining_toppings = self.MAX_TOPPINGS
        self.inprogress_burger = []
        self.currently_selecting = STAGE.Bun

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING
        
    def handle_bun(self, bun):
        self.pick_bun(bun)
        self.currently_selecting = STAGE.Patty

    def handle_patty(self, patty):
        if patty == "next":
            self.currently_selecting = STAGE.Toppings
        else:
            self.pick_patty(patty)

            

    def handle_toppings(self, toppings):
        if toppings == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_toppings(toppings)

    def handle_pay(self, expected, total):
        if self.currently_selecting != STAGE.Pay:
            raise InvalidStageException
        if total == str('{:,.2f}'.format(expected)):
            print("Thank you! Enjoy your burger!")
            self.total_burgers += 1
            self.total_sales += expected # only if successful
            #print(f"Total sales so far {self.total_sales}")
            self.reset()
        else:
            raise InvalidPaymentException
        
    def print_current_burger(self):
        print(f"Current Burger: {','.join([x.name for x in self.inprogress_burger])}")

    def calculate_cost(self):
        # TODO add the calculation expression/logic for the inprogress_burger
        total_cost = sum(item.cost for item in self.inprogress_burger)
        print(f"Total cost of burger: ${total_cost:.2f}")
        return total_cost
#Neil Patel, UCID: np656 Date: 3/27

    def run(self):
        try:
            if self.currently_selecting == STAGE.Bun:
                bun = input(f"What type of bun would you like {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.buns))))}?\n")
                self.handle_bun(bun)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Patty:
                patty = input(f"Would type of patty would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.patties))))}? Or type next.\n")
                self.handle_patty(patty)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Toppings:
                toppings = input(f"What topping would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.toppings))))}? Or type done.\n")
                self.handle_toppings(toppings)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Pay:
                expected = self.calculate_cost()
                # show expected value as currency format
                # require total to be entered as currency format
                expected_str = "${:,.2f}".format(expected)
                total = input(f"Your total is {expected_str}, please enter the exact value.\n")
                #total = input(f"Your total is {expected}, please enter the exact value.\n")
                self.handle_pay(expected, total)
                
                choice = input("What would you like to do? (order or quit)\n")
                if choice == "quit":
                    #exit() in recursive functions creates stackoverflow
                    # use return 1 to exit
                    print("Quitting the burger machine")
                    return 1
        except KeyboardInterrupt:
            # quit
            print("Quitting the burger machine")
            sys.exit()
        except OutOfStockException:
            print(f"item is out of stock in {self.currently_selecting} stage.")
        # handle OutOfStockException
            # show an appropriate message of what stage/category was out of stock
        #Neil Patel, UCID: np656 Date: 3/27
        #This exception raises when the quantity of an ingredient runs out, resulting in being unable to ask for it when ordering.
        except NeedsCleaningException:
            print("The machine needs cleaning. Please type 'clean' to trigger clean_machine().")
            user_input = input().strip().lower()
            if user_input == "clean":
                self.clean_machine()
                print("The machine has been cleaned.")
            else:
                print("Ignoring user input. The machine was not cleaned.")
        # handle NeedsCleaningException
            # prompt user to type "clean" to trigger clean_machine()
            # any other input is ignored
            # print a message whether or not the machine was cleaned
        #Neil Patel, UCID: np656 Date: 3/27
        #This exception is raised when there has been many orders done and the burger machine needs to be clean
        except InvalidChoiceException:
            print(f"Invalid choice in {self.currently_selecting} category.")
        # handle InvalidChoiceException
            # show an appropriate message of what stage/category was the invalid chnoice was in
        #Neil Patel, UCID: np656 Date: 3/27
        #This exception is raised when a user makes an invalid choice or selection when ordering.

        except ExceededRemainingChoicesException:
            print(f"You have already chosen the maximum number of {self.currently_selecting} ingredients.")
            #print({self.currently_selecting.value})
            chag = self.currently_selecting.value + 1
            #print({chag})
            self.currently_selecting = STAGE(chag)

            #if self.currently_selecting != STAGE.Bun:
            #    self.pick_patty()
                
            #if self.currently_selecting != STAGE.Patty:
            #    self.pick_toppings()

            #if self.currently_selecting != STAGE.Toppings:
            #    self.currently_selecting = STAGE.Pay

        # handle ExceededRemainingChoicesException
            # show an appropriate message of which stage/category was exceeded
            # move to the next stage/category
        #Neil Patel, UCID: np656 Date: 3/27
        #This exception is raised when the user exceeds the remaining choices or limit, such as selecting more ingredients than available.

        except InvalidPaymentException:
            print("Input value doesn't match the expected value\n")
        # handle InvalidPaymentException
            # show an appropriate message
        #Neil Patel, UCID: np656 Date: 3/27
        #This exception is raised when a payment method or transaction is invalid or cannot be processed.
        except Exception as e:
            # this is a default catch all, follow the steps above
            print(f"Something went wrong: {e}")
        #Neil Patel, UCID: np656 Date: 3/27

        self.run()

    def start(self):
        self.run()

    
if __name__ == "__main__":
    bm = BurgerMachine()
    bm.start()