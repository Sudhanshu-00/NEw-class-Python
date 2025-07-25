class grandfather:
    gname="anuj"
    gage=78
    ghpono=67878997898


    def __init__(self,gcolour):
        self.gcolour=gcolour
      


    def  display(self):
        print("gcolour:",self.gcolour)
        
            



class father(grandfather):
    fname="raj"
    fage=40
    fphono=65767686


    def __init__(self,gcolour,fcolour,fheight):
        self.fcolour=fcolour
        self.fheight=fheight
        super().__init__(gcolour)


    def display1(self):
        super().display()
        print("fcolour:",self.fcolour)
        print("fheight:",self.fheight)
        
ob1=father("Dark", "dark","5.9")
ob1.display1()


