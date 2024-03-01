class student:
    def __init__(self,Name,Age,deprt,year):
        self.Name=Name               
        self.Age=Age
        self.deprt=deprt
        self.year=year
    def softwork(self):
        if(self.deprt=='cse'):
            print("software department and works on software")
        else:
            print("hardware department")
s=student('saniya',19,'cse',3)
s.softwork()
print(s.Name)
print(s.Age)
print(s.deprt)
print(s.year)
a=student('sanni',19,'ece',3)
a.softwork()
print(a.Name)
print(a.Age)
print(a.deprt)
print(a.year)