
# class
class Car:
  # constructor
  def __init__(self , brand , model , made , lunch_year , fuel):
    self.brand = brand
    self.model = model
    self.made = made
    self.lunch_year = lunch_year
    self.fuel = fuel

  def car_info(self):
    print(self.brand , self.model , self.made , self.lunch_year )

# polymorphism (same method in electric_car class)
  def fuel_info(self):
    print(f"It uses fuel: {self.fuel}")


# object of car class
car_Object = Car("Tata" , "safari" , "Made in India" , "2025" , "Petrol")
# print(car_Object.model)
# print(car_Object.brand)
# print(car_Object.made)
# print(car_Object.lunch_year)


#  inherite parent class through child class electric_car
class Electric_car(Car):
  def __init__(self , brand , model , made , lunch_year, battery_charge , fuel):
   super().__init__(brand , model , made , lunch_year , fuel)
   self.battey_charge = battery_charge
   self.fuel = fuel

  def battery_charge_info(self):
    print(f"Battery charge: {self.battey_charge}")

  def fuel_info(self):
    print(f"It uses fuel: { self.fuel}")

 # object of electric_car
electric_car = Electric_car("Tata" , "safari" , "Made in India" , "2025" , "85%" , "electric")

car_Object.car_info()  # call parent class info
car_Object.fuel_info() # in parent class

electric_car.battery_charge_info()  # call child class info
electric_car.fuel_info()  # in child class