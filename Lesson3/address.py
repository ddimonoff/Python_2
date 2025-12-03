class Address:
    postal_code = '000000'
    city = 'unknown'
    street = 'unknown'
    house = 'unknown'
    appartment = 'unknown'

    def __init__(self, postal_code, city, street, house, appartment):
        self.postal_code = postal_code
        self.city = city
        self.street = street
        self.house = house
        self.appartment = appartment

    def __str__(self):
        return f'{self.postal_code}, {self.city}, {self.street}, {self.house}-{self.appartment}'
