import csv

class Item:


    pay_rate =0.8 
    all=[]
    def __init__(self,name:str,price:float,quantity=0):
        
        assert price>=0,f"Price{price}is not greater than zero!"
        assert quantity>=0, f"Quantity{quantity}is not greater than zero!"
        
        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)
    @property
    def __name(self):
        return self.__name
        
    def calculate_total_price(self):
        return self.__price*self.quantity
    
    def apply_discount(self):
        self.__price= self.__price * self.pay_rate
    @__name.setter
    def __name(self,value):
        self.__name=value
    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv","r")as infile:
            reader=csv.DictReader(infile)
            items=list(reader)
        for item in items:
            Item(
                name= item.get('name'),
                price= float(item.get('price')),
                quantity= float(item.get('quantity'))
            )
    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
   

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.__price}, {self.quantity})"