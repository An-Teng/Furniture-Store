class History:
    def __init__(self,Type,Name,Date):
        self.__Type=Type
        self.__Name=Name
        self.__Date=Date
    def get_Type(self):
        return self.__Type
    def get_Name(self):
        return self.__Name
    def get_Date(self):
        return self.__Date
    def set_Type(self,type):
        self.__Type=type
    def set_Name(self,Name):
        self.__Name=Name
    def set_Date(self,Date):
        self.__Date=Date
