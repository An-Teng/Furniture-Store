class Product:
    count_id = 0

    def __init__(self, name, description, features, colours, category, status, price):
        Product.count_id +=1
        self.__product_id= Product.count_id
        self.__name = name
        self.__description = description
        self.__features = features
        self.__colours = colours
        self.__category = category
        self.__status = status
        self.__price = price

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_features(self):
        return self.__features

    def get_colours(self):
        return self.__colours

    def get_category(self):
        return self.__category

    def get_status(self):
        return self.__status

    def get_price(self):
        return self.__price

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_name(self,name):
        self.__name = name

    def set_description(self,description):
        self.__description = description

    def set_features(self,features):
        self.__features = features

    def set_colours(self,colours):
        self.__colours = colours

    def set_category(self,category):
        self.__category = category

    def set_status(self,status):
        self.__status = status

    def set_price(self,price):
        self.__price = price



