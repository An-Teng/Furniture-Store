import Product

class Electronic(Product.Product):
    count_id = 0

    def __init__(self, name, description, features, colours, category,status, price, assembly):
        super().__init__(name, description, features, colours,category,status, price)
        Electronic.count_id +=1
        self.__electronic_id = Electronic.count_id
        self.__assembly = assembly

    def get_electronic_id(self):
        return self.__electronic_id

    def get_assembly(self):
        return self.__assembly

    def set_electronic_id(self,electronic_id):
        self.__electronic_id = electronic_id

    def set_assembly(self,assembly):
        self.__assembly = assembly
