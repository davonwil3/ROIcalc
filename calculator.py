class roiCalc :
    def __init__(self, rentalIncome, expenses, totalInvestment) :
        self.rentalIncome = rentalIncome
        self.expenses = expenses
        self.totalInvestment = totalInvestment
        self.cashflow = 0

    def expensesSum (self):
       self.expenses = sum(self.expenses)
       return self.expenses
       
    
    def calculateCashFlow (self):
        self.cashflow = self.rentalIncome - self.expensesSum()
        return self.cashflow
    
    def roi (self):
        returnonInv = self.calculateCashFlow() * 12 / self.totalInvestment
        returnonInv = returnonInv * 100
        return returnonInv
    

newCalc = roiCalc(2000, [300, 200, 10, 90], 200000)
newCalc2 = roiCalc(2000, [700, 100, 50, 60], 300000)

print(newCalc.roi())
print(newCalc2.roi())




        