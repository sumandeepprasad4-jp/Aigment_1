# class vechicle:
#     company="xyz motors"
#     def __init__(self,n_wheel,n_seets,milage):
#         self.n_wheel= n_wheel
#         self.n_seets=n_seets
#         self.milage=milage
#     def get_details(self):
#         return f"this vichel has {self.n_wheel} wheel,and {self.n_seets} seats and provide a milage of {self.milage}"
# class car(vechicle):
#     modle="deep"
#     def __init__(self,car_type,drive_type):   #def __init__(self,car_type,drive_type,n_wheel,n_seets,milage):
#         self.car_type=car_type
#         self.drive_type=drive_type
#         super().__init__(4,5,20) # or vechicle.__init__(self,4,5,30) or super().__init__(n_wheel,n_seets,milage)
#     def greet(self):
#         return f"type of car is: {self.car_type} and drive  is: {self.drive_type}"
# c1=car("4 wheeler","nice") #or c1=car("4 wheeler","nice",4,5,6)
# print(c1.company)
# print(c1.milage)
# print(c1.modle)
# print(c1.get_details())
# print(c1.greet())
