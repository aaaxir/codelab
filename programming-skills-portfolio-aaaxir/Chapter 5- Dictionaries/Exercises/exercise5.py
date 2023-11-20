"""Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about

each pet"""

animal=[]
pet1={
    'animal type': 'toad',
    'name': 'pepper',
    'owner': 'Nawaf',
    'weight': 1,
    'eats': 'dried insects'}
animal.append(pet1)

pet2={
    'animal type': 'hamster',
    'name': 'billy',
    'owner': 'Amani',
    'weight': 0.5,
    'eats': 'sunflower seeds',}
animal.append(pet2)

pet3={
    'animal type': 'dog',
    'name': 'pepper',
    'owner': 'Aamir',
    'weight': 15,
    'eats': 'dog food',}
animal.append(pet3)


for pet in animal:
    print("\nSome information about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))