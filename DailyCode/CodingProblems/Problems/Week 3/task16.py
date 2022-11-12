class Order():

    def __init__(self):
        self.ids = []
    
    def record(self, id):
        self.ids.append(id)
    
    def get_last(self, i):
        return self.ids[len(self.ids) - 1 - i]

orders = Order()
for i in range(1, 101):
    orders.record(i)

print(orders.get_last(10))
print(orders.get_last(25))
print(orders.get_last(50))