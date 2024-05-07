# Example 1)  develop a class that will provide methods to convert some amount

class currency_rate_exchange:
    def __init__(self):
        self.__exchange_rate = 0.0
    def set_exchange_rate(self,rate):
        self.__exchange_rate = rate
    def exchange_currency(self, ammount):
        res = self.__exchange_rate * ammount
        return res
    
def main():
    obj = currency_rate_exchange()
    obj.set_exchange_rate(104)
    pr = obj.exchange_currency(35)
    print("After the exchange rate of currency is =",pr)
    
main()