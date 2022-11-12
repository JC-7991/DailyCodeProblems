class Order():

    def __init__(self):
        self.orderIds = []
    
    def record(self, order_id):
        self.orderIds.append(order_id)
    
    def get_last(self, i):
        return self.orderIds[len(self.orderIds) - 1 - i]

orders = Order()
for i in range(1, 101):
    orders.record(i)
print(orders.get_last(10))
print(orders.get_last(50))