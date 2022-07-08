class Supplier:
    # count_id = 0
    def __init__(self, supplierid, name, abbreviation, products_offered, website, email, contactno, availability, logo):
        # Supplier.count_id += 1
        self.__supplier_id = supplierid

        self.__name = name
        self.__abbreviation = abbreviation
        self.__products_offered = products_offered
        self.__website = website
        self.__email = email
        self.__contactno = contactno
        self.__availability = availability
        self.__logo = logo

    def set_supplier_id(self, supplier_id):
        self.__supplier_id = supplier_id
    def set_name(self, name):
        self.__name = name
    def set_abbreviation(self, abbreviation):
        self.__abbreviation = abbreviation
    def set_products_offered(self, products_offered):
        self.__products_offered = products_offered
    def set_website(self, website):
        self.__website = website
    def set_email(self, email):
        self.__email = email
    def set_contactno(self, contactno):
        self.__contactno = contactno
    def set_logo(self, logo):
        self.__logo = logo
    def set_availability(self, availability):
        self.__availability = availability

    def get_supplier_id(self):
        return self.__supplier_id
    def get_name(self):
        return self.__name
    def get_abbreviation(self):
        return self.__abbreviation
    def get_products_offered(self):
        return self.__products_offered
    def get_website(self):
        return self.__website
    def get_email(self):
        return self.__email
    def get_contactno(self):
        return self.__contactno
    def get_logo(self):
        return self.__logo
    def get_availability(self):
        return self.__availability