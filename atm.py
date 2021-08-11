class car(object):
        def __init__(self,atmcardnumber,pinnumber,CashWithdrawl,BalanceEnquiry):
          self.atmcardnumber=atmcardnumber
          self.pinnumber=pinnumber
          self.CashWithdrawl=CashWithdrawl
          self.BalanceEnquiry=BalanceEnquiry
        def start(self):
                
                print("pinnumber="+self.pinnumber)
                print("atmcardnumber="+self.atmcardnumber) 
                print("BalanceEnquiry="+self.BalanceEnquiry)
                print("CashWithdrawl="+self.CashWithdrawl)     
            
car1=car("20","30","40","50")    
print(car1.start())       
   

          