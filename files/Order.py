class Order:
    # count_id = 0
    def __init__(self, orderid, productid, product, orderamt, supplier, cost, remarks, delivered):
        # Order.count_id += 1
        self.__orderno = orderid
        self.__productid = productid
        self.__product = product
        self.__orderamt = orderamt
        self.__cost = float(cost)
        self.__supplier = supplier
        self.__remarks = remarks
        self.__delivered = delivered

    def set_orderno(self, orderno):
        self.__orderno = orderno
    def set_productid(self, productid):
        self.__productid = productid
    def set_product(self, product):
        self.__product = product
    def set_orderamt(self, orderamt):
        self.__orderamt = orderamt
    def set_cost(self, cost):
        self.__cost = cost
    def set_supplier(self, supplier):
        self.__supplier = supplier
    def set_remarks(self, remarks):
        self.__remarks = remarks
    def set_delivered(self, delivered):
        self.__delivered = delivered

    def get_orderno(self):
        return self.__orderno
    def get_productid(self):
        return self.__productid
    def get_product(self):
        return self.__product
    def get_orderamt(self):
        return self.__orderamt
    def get_totalcost(self,cost,orderamt):
        totalcost = cost * orderamt
        return float(totalcost)
    def get_cost(self):
        return self.__cost
    def get_supplier(self):
        return self.__supplier
    def get_remarks(self):
        return self.__remarks
    def get_delivered(self):
        return self.__delivered