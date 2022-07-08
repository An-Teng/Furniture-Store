from Reward import *
class Special(Reward):
    def __init__(self,Reward_ID, Name, Description, Price, Validity,Usability):
        super().__init__(Reward_ID, Name, Description, Price, Validity)
        self.__Special_ID=Reward_ID
        self.__Usability=Usability
        self.__Status=0
        self.__Redeemed=0
        self.__Limit=0
        self.__check=0
        self.__expiary =0
        self.__user_id=0
        self.__day=0
    def get_Special_ID(self):
        return self.__Special_ID
    def get_Usability(self):
        return self.__Usability
    def get_Redeemed(self):
        return self.__Redeemed
    def set_Redeemed(self,Redeemed):
        self.__Redeemed=Redeemed
    def set_Usability(self,Usability):
        self.__Usability=Usability
    def set_Special_ID(self,Special_ID):
        self.__Special_ID=Special_ID
    def set_Limit(self,Limit):
        self.__Limit=Limit
    def get_Limit(self):
        return self.__Limit
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
    def get_day(self):
        return  self.__day
    def set_day(self,day):
        self.__day=day
