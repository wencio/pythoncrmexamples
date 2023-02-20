class Property:
    def __init__(self, address, city, state, zip_code, price, num_bedrooms, num_bathrooms, num_garages):
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.price = price
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.num_garages = num_garages
        
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        
class CRM:
    def __init__(self):
        self.properties = []
        self.contacts = []
        
    def add_property(self, property):
        self.properties.append(property)
        
    def add_contact(self, contact):
        self.contacts.append(contact)
        
    def search_properties(self, city, state, num_bedrooms, max_price):
        results = []
        for property in self.properties:
            if property.city == city and property.state == state and property.num_bedrooms >= num_bedrooms and property.price <= max_price:
                results.append(property)
        return results
        
    def search_contacts(self, name):
        results = []
        for contact in self.contacts:
            if name in contact.name:
                results.append(contact)
        return results
