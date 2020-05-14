class Student(object):
    def __init__(self, id, name, address, phone):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def get_status(self):
        return self.status