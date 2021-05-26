class Str:
    def __init__(self, var):
        self.var = var   
    def __sub__(self, other):
        for i in other.var:
            if i in self.var:
            	b = (self.var).find(i)
            	self.var=self.var[0:b]+self.var[b+1:]
        print(self.var)
 
p = Str(input("Enter the first string: "))
q = Str(input("Enter the second string: "))
r = p-q
print(r)
