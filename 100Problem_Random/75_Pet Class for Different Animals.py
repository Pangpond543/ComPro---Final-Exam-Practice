class Pet:
    def __init__(self, species: str, breed: str, color: str, name: str, height: float, weight: float):
        self.species = species
        self.breed = breed
        self.color = color
        self.name = name
        self.height = height
        self.weight = weight
    
    def display_info(self):
        return (f"species: {self.species}\nbree: {self.breed}\ncolor: {self.color}\nname: {self.name}\nheight {self.height}\nweight: {self.weight}")
        
def pet_menu():
    while True:
        spe = int(input("เลือกชนิดสัตว์ 1-3 : 1. Dog | 2. Cat | 3. Bird"))
        if spe == 1:
            species = "Dog"
            break
        elif spe == 2:
            species = "Cat"
            break          
        elif spe == 3:
            species = "Bird"
            break
        else:
            print("เล์อกไม่ถูกต้อง")
            
    name = input("กรอกชื่อ: ") 
    breed = input("กรอกสายพันธุ์: ") 
    color = input("กรอกสี: ") 
    height = float(input("กรอกความสูง (cm): ")) 
    weight = float(input("กรอกน้ำหนัก (kg): "))
  
    pet = Pet(species,  breed, color, name, height, weight)
    
    print(pet.display_info())
    
pet_menu()