class Person:
    def hello(self,fname,lname):
        self.fname=fname
        self.lname=lname
        return fname+lname

    def sum(self,v1,v2):
        self.v1=v1
        self.v2=v2
        return v1+v2


spoorthi = Person()
print(spoorthi.hello('spurti','raj'))
print(spoorthi.sum(45,78))

