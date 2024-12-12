class UNO():
    a=5
    def __init__(self):
        self.b=3
    def f(self,i):
        self.c = i
        return self.a*self.b
obj = UNO()
x = obj.a
y = obj.f(5)
z = obj.c / obj.f(1)
print(f'{x},{y},{z}')