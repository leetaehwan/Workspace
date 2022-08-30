test = "you can use this module."

def add(a, b):
    return (lambda a,b: a+b)(a,b)
 
def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b


class all_calc():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
 
    def mul(self):
        return self.a * self.b

    def sub(self):
        return self.a - self.b

    def div(self):
        return self.a / self.b

  