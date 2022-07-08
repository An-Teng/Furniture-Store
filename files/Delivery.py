class Delivery:
    count_id = 0

    def __init__(self, date_delivery, time_delivery, delivery_address, receiver_name, pricing):
        Delivery.count_id += 1
        self.__delivery_id = Delivery.count_id
        self.__date_delivery = date_delivery
        self.__time_delivery = time_delivery
        self.__delivery_address = delivery_address
        self.__receiver_name = receiver_name
        self.__pricing = pricing

    def get_delivery_id(self):
        return self.__delivery_id
    def get_date_delivery(self):
        return self.__date_delivery
    def get_time_delivery(self):
        return self.__time_delivery
    def get_delivery_address(self):
        return self.__delivery_address
    def get_receiver_name(self):
        return self.__receiver_name
    def get_pricing(self):
        return self.__pricing
    def set_delivery_id(self, delivery_id):
        self.__delivery_id = delivery_id
    def set_date_delivery(self, date_delivery):
        self.__date_delivery = date_delivery
    def set_time_delivery(self, time_delivery):
        self.__time_delivery = time_delivery
    def set_delivery_address(self, delivery_address):
        self.__delivery_address = delivery_address
    def set_receiver_name(self, receiver_name):
        self.__receiver_name = receiver_name
    def set_pricing(self, pricing):
        self.__pricing = pricing
