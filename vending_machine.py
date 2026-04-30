class VendingMachine:
    def __init__(self):
        self.products={
            "Water": 0.80,
            "Juice": 1.20,
            "Soda": 1.50
        }
        self.balance=0.0
    def insert_money(self, coin):
        self.balance+=coin
        
    def select_product(self, product_name):
        if product_name not in self.products:
            return "Product not available"
        price=self.products[product_name]
        if self.balance < price:
            return f"Not enough balance.You need ${price - self.balance:.2f}  more to buy{product_name}"
       
        change = self.balance - price
        del self.products[product_name]
        self.balance = 0.0
        return f"Dispensing {product_name}. Change: ${change:.2f}"

    
    def show_available_products(self):
        for product_name,price in self.products.items():
            print(product_name, price)
            
vm1=VendingMachine()
vm1.insert_money(1.00)
vm1.insert_money(0.50)
print(vm1.select_product("Juice"))
print(vm1.select_product("Water"))





        