class Patient:
    first_name : str
    last_name : str
    age : int
    b_group : str

    def show_patient(self):
        print(f"{self.first_name} {self.last_name}")
    def show_patient_age(self):
        print(f"The age of {self.first_name} {self.last_name} is {self.age}")
    def get_bgroup(self, group):
        if self.b_group == group:
            print("Blood is available")
        else:
            print("Blood is not available")

p = Patient()
p.first_name = "Bhushan"
p.last_name = "Chaudhari"
p.age = 25
p.b_group = "B+"
# p.show_patient()
# p.show_patient_age()
p.get_bgroup("B+")