class MyCalc:
    def __init__(self) -> None:
        self.ans = None
    
    def add(self, a,b):
        r = a+b
        self.ans = r
        return r
    
    def sub(self,a,b):
        r = a-b
        self.ans = r
        return r
    def mult(self,a,b):
        r = a*b
        self.ans = r
        return r

    def div(self, a,b):
        if b==0:
            print("Can't divide by 0!")
            return
        r = a/b
        self.ans = r
        return r

if __name__== "__main__":
    calc = MyCalc()
    response = input("Write 2 Numbers: ")
    if "+" in response:
        print("We're adding: ")
        nums = response.split("+")
        r = calc.add(int(nums[0]), int(nums[1]))
        print(f"Answer: {r}")
    if "-" in response:
        print("We're subtracting: ")
        nums = response.split("-")
        r = calc.sub(int(nums[0]), int(nums[1]))
        print(f"Answer: {r}")
    if "*" in response:
        print("We're multyplying: ")
        nums = response.split("*")
        r = calc.mult(int(nums[0]), int(nums[1]))
        print(f"Answer: {r}")
