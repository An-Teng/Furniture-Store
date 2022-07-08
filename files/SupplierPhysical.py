import Supplier

class SupplierPhysical(Supplier.Supplier):
    # count_id = 0
    def __init__(self, supplierid, supplierPid, name, abbreviation, products_offered, website, email, contactno, availability, logo, address):
        super().__init__(supplierid, name, abbreviation, products_offered, website, email, contactno, availability, logo)
        # SupplierPhysical.count_id += 1
        self.__supplierphysical_id = supplierPid
        self.__address = address

    def set_supplierphysical_id(self, supplierphysical_id):
        self.__supplier_id = supplierphysical_id
    def set_address(self, address):
        self.__address = address

    def get_supplierphysical_id(self):
        return self.__supplierphysical_id
    def get_address(self):
        return self.__address