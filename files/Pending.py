import Delivery

class Pending(Delivery.Delivery):
    count_id = 0

    def __init__(self, delivery_address, receiver_name, email, confirmation, remarks, date_delivery, time_delivery, pricing):
        super().__init__(delivery_address, receiver_name, date_delivery, time_delivery, pricing)
        Pending.count_id += 1
        self.__pending_id = Pending.count_id
        self.__email = email
        self.__confirmation = confirmation
        self.__remarks = remarks

    def get_pending_id(self):
        return self.__pending_id
    def get_email(self):
        return self.__email
    def get_confirmation(self):
        return self.__confirmation
    def get_remarks(self):
        return self.__remarks
    def set_pending_id(self, pending_id):
        self.__pending_id = pending_id
    def set_email(self, email):
        self.__email = email
    def set_confirmation(self, confirmation):
        self.__confirmation = confirmation
    def set_remarks(self, remarks):
        self.__remarks = remarks
