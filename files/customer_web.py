import admin_web

class customer_web(admin_web.admin_web):
    count_id = 0

    def __init__(self, first_name, last_name, gender, email, phone_number, date_of_birth, region, street, unit_number, block, username, password, confirm_password, status):
        super().__init__(first_name, last_name, username, password, confirm_password, gender, email, phone_number, status)
        customer_web.count_id += 1
        self.__customer_id = customer_web.count_id
        self.__date_of_birth = date_of_birth
        self.__region = region
        self.__street = street
        self.__unit_number = unit_number
        self.__block = block

    def get_customer_id(self):
        return self.__customer_id

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_region(self):
        return self.__region

    def get_street(self):
        return self.__street

    def get_unit_number(self):
        return self.__unit_number

    def get_block(self):
        return self.__block

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def set_region(self, region):
        self.__region = region

    def set_street(self, street):
        self.__street = street

    def set_unit_number(self, unit_number):
        self.__unit_number = unit_number

    def set_block(self, block):
        self.__block = block
