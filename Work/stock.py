# stock.py

class Stock:
    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self) -> float:
        return self.shares * self.price;

    def sell(self, sstocks) -> None:
        self.shares -= sstocks
        
