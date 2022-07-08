from datetime import *
class Reward:
    def __init__(self,Reward_ID,Name,Description,Price,Validity):
        self.__Reward_ID=Reward_ID
        self.__Name=Name
        self.__Description=Description
        self.__Price=Price
        self.__Validity=Validity
        self.__Status=0
        self.__Redeemed=0
        self.__Limit=0
        self.__check=0
        self.__expiary = 0
        self.__user_id = 0
        self.__day=0
    def get_Reward_ID(self):
        return self.__Reward_ID
    def get_Name(self):
        return self.__Name
    def get_Description(self):
        return self.__Description
    def get_Price(self):
        return self.__Price
    def get_Validity(self):
        return self.__Validity
    def set_Reward_ID(self,Reward_ID):
        self.__Reward_ID=Reward_ID
    def set_Name(self,Name):
        self.__Name=Name
    def set_Description(self,Description):
        self.__Description=Description
    def set_Price(self,Price):
        self.__Price=Price
    def set_Validity(self,Validity):
        self.__Validity=Validity

    def set_Limit(self,Limit):
        self.__Limit=Limit
    def get_Limit(self):
        return self.__Limit
    def get_Redeemed(self):
        return self.__Redeemed
    def set_Redeemed(self,Redeemed):
        self.__Redeemed=Redeemed
    def get_Status(self):
        self.__Status=int(self.get_Limit())-int(self.get_Redeemed())
        return self.__Status
    def get_check(self):
        return self.__check
    def set_check(self,check):
        self.__check=check
    def get_expiary(self):
        return self.__expiary
    def set_expiary(self,expiary):
        self.__expiary=expiary
    def get_user_id(self):
        return self.__user_id
    def set_user_id(self,user_id):
        self.__user_id=user_id
    def get_day(self):
        self.__day=self.get_expiary()-date.today()
