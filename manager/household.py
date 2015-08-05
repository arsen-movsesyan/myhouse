
class Household(object):

    def __init__(self):
	self.address=None
	self.vehicles=dir()
	self.property_name=None
	self.people=dir()

    def __str__(self):
	return self.name


class Address(object):

    def __init__(self):
	self.addr_dict=dict()
	self.street_1=''
	self.street_2=''
	self.city=''
	self.state=''
	self.zip_code=''

    def set_address(self,in_address):
	self.addr_dict=in_address
	self.street_1=in_address['street_1']
	self.street_2=in_address['street_2']
	self.city=in_address['city']
	self.state=in_address['state']
	self.zip_code=in_address['zip_code']




class Person(HHObject):

    def __init__(self):
	self.f_name=None
	self.l_name=None
	self.dob=None
	self.role=None

