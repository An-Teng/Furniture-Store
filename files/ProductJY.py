class ProductJY:
    # count_id = 0
    def __init__(self, productid, productname, producttype, availability, suppliers, quantity, cost, ordered):
        # Product.count_id += 1
        self.__productid = productid
        self.__productname = productname
        self.__producttype = producttype
        self.__availability = availability
        self.__suppliers = suppliers
        self.__quantity = quantity
        self.__cost = float(cost)
        self.__ordered = ordered

    def set_productid(self, productid):
        self.__productid = productid
    def set_productname(self, productname):
        self.__productname = productname
    def set_producttype(self, producttype):
        self.__producttype = producttype
    def set_availability(self, availability):
        self.__availability = availability
    def set_suppliers(self, suppliers):
        self.__suppliers = suppliers
    def set_quantity(self, quantity):
        self.__quantity = quantity
    def set_cost(self, cost):
        self.__cost = cost
    def set_ordered(self, ordered):
        self.__ordered = ordered

    def get_productid(self):
        return self.__productid
    def get_productname(self):
        return self.__productname
    def get_producttype(self):
        return self.__producttype
    def get_availability(self):
        return self.__availability
    def get_suppliers(self):
        return self.__suppliers
    def get_quantity(self):
        return self.__quantity
    def get_cost(self):
        return self.__cost
    def get_ordered(self):
        return self.__ordered