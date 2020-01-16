class car:
    def __init__(self,effiency):
        self.effiency=effiency
        self.fuel=0
		
		#opening file
        
        #open the text file FuelEffic.txt which contain tank capcity efficiency
        infile=open("FuelEffic.txt","r")
        lines=infile.readlines()
        self.millage=int(lines[0].split(':')[-1])
        self.sizeoftank=int(lines[1].split(':')[-1])
        #calculating total miles possible
        self.totaldistance=self.millage*self.sizeoftank
    def drive(self,distance):
        self.fuel=(self.totaldistance-distance)/self.effiency
        

    def getfuelrange(self):
        return self.fuel
  
    def addGas(self,gas):
        self.fuel=self.fuel+gas
        if(self.fuel>self.sizeoftank):
            self.fuel=self.sizeoftank   
if __name__=="__main__":

    myHybrid=car(20)
    myHybrid.drive(100)
    print(myHybrid. getfuelrange())
    myHybrid.addGas(9)
    print(myHybrid.getfuelrange())
	
		
    
    
		
		
	
