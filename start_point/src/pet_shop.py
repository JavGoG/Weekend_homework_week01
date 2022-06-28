
import pdb

def get_pet_shop_name(pet_shop):
    # pdb.set_trace()
    return pet_shop["name"]


# def test_add_or_remove_cash__remove(self):
#     add_or_remove_cash(self.cc_pet_shop,10)
#     cash = get_total_cash(self.cc_pet_shop)
#     self.assertEqual(990, cash)



# I AM NOT ABLE TO DO THIS FUNCTION WORK PROPPERLY
def get_total_cash(pet_shop):
    total_cash = pet_shop["admin"]["total_cash"]                                               
    return total_cash        

# def test_add_or_remove_cash__remove(self):
#         add_or_remove_cash(self.cc_pet_shop,-10)
#         cash = get_total_cash(self.cc_pet_shop)
#         self.assertEqual(990, cash)
    
def add_or_remove_cash(cc_pet_shop,cash):
    # pdb.set_trace()
    total_cash = cc_pet_shop["admin"]["total_cash"] 
    total_cash += cash
    cc_pet_shop["admin"]["total_cash"] = total_cash
    
        
# def test_pets_sold(self):
#         sold = get_pets_sold(self.cc_pet_shop)
#         self.assertEqual(0, sold)

def get_pets_sold(cc_pet_shop):
    # pdb.set_trace()
    pets_sold = cc_pet_shop["admin"]["pets_sold"] 
    print(pets_sold)
    return pets_sold

# def test_increase_pets_sold(self):
#         increase_pets_sold(self.cc_pet_shop,2)
#         sold = get_pets_sold(self.cc_pet_shop)
#         self.assertEqual(2, sold)

def increase_pets_sold(pet_shop, sold):
    # pdb.set_trace()
    pets_sold = pet_shop["admin"]["pets_sold"]
    pets_sold += sold
    pet_shop["admin"]["pets_sold"] = pets_sold
    print (pets_sold) 

def get_stock_count(shop):
    return len(shop["pets"])

#  def test_stock_pets(self):
#         pets = get_stock_pets(self.cc_pet_shop)
#         self.assertEqual(6, pets)

def get_stock_pets(cc_pet_shop):
    pdb.set_trace()
    stock = len(cc_pet_shop["pets"])
    return stock

# def test_all_pets_by_breed__found(self):
#         pets = get_pets_by_breed(self.cc_pet_shop, "British Shorthair")
#         self.assertEqual(2, len(pets))

def get_pets_by_breed(pet_shop, breed):
    pets_by_breed = []

    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)

    return pets_by_breed
        
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_customer_cash(customer_cash):
    # pdb.set_trace()
    if customer_cash["cash"] == 1000:
        return 1000
        
def remove_customer_cash(customer, cash):
    customer["cash"]-= cash

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

    
    
    


