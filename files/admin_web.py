class admin_web():
    count_id = 0


    def __init__(self,first_name,last_name,username,password,confirm_password,gender,email,phone_number,status):
        admin_web.count_id += 1
        self.__admin_id = admin_web.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__password = password
        self.__confirm_password = confirm_password
        self.__gender = gender
        self.__email = email
        self.__phone_number = phone_number
        self.__status = status


    def set_admin_id(self,admin_id):
        self.__admin_id = admin_id

    def set_first_name(self,first_name):
        self.__first_name = first_name

    def set_last_name(self,last_name):
        self.__last_name = last_name

    def set_username(self,username):
        self.__username = username

    def set_password(self,password):
        self.__password = password

    def set_confirm_password(self,confirm_password):
        self.__confirm_password = confirm_password

    def set_gender(self,gender):
        self.__gender = gender

    def set_email(self,email):
        self.__email = email

    def set_phone_number(self,phone_number):
        self.__phone_number = phone_number

    def set_status(self,status):
        self.__status = status

    def get_admin_id(self):
        return self.__admin_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_confirm_password(self):
        return self.__confirm_password

    def get_gender(self):
        return self.__gender

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def get_status(self):
        return self.__status
