class Pet:
    kind = "mammal"
    n_pets = 0 # количество питомцев
    pet_names = [] # список имен всех питомцев
    def __init__(self, spec, name):
        self.spec = spec
        self.name = name
        self.legs = 4

tom = Pet("cat", "Tom")
avocado = Pet("dog", "Avocado")
ben = Pet("goldfish", "Benjamin")

Pet.n_pets += 3
print(Pet.n_pets, tom.n_pets, avocado.n_pets, ben.n_pets)

ben.kind = "fish"
print(Pet.kind, tom.kind, avocado.kind, ben.kind)

tom.pet_names = ["Tom"]
avocado.pet_names = ["Avocado"]
ben.pet_names = ["Benjamin"]
print(Pet.pet_names, tom.pet_names, avocado.pet_names, ben.pet_names)

Pet.all_specs = [tom.spec, avocado.spec, ben.spec]
print(tom.all_specs, avocado.all_specs, ben.all_specs)

avocado.breed = "corgi"
print(avocado.breed)