"""You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
Print a message to each of the two people still on your list, letting them know they’re still invited.
Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program."""

guest = ['Robert Oppenheimer', 'Alan Turing', 'Jay Z']
name = guest[0].title()
print(name + ", I invite you to have dinner with me.")
name = guest [1].title()
print(name + ", would you like to have dinner with me?.")
name = guest [2].title()
print(name + ", I'd like it if u would accept my invitation to dinner.")
name=guest[0].title()
print("\nunfortunately, " + name + " wont be able to attend.")
del(guest[0])
guest.insert(0, 'Liam Gallagher')
name=guest[0].title()
print("\n" + name + ", I invite you to have dinner with me..")
name=guest[1].title()
print(name + ",I invite you to have dinner with me.")
name=guest [2].title()
print(name + ",I invite you to have dinner with me..")

print("\nWe got a bigger table!")
guest.insert(0, 'Noel Gallagher')
guest.insert(2, 'Abraham Lincoln')
guest.append('Al Pacino')
name=guest[0].title()
print(name + ",I invite you to have dinner with me.")
name=guest[1].title()
print(name + ",I invite you to have dinner with me.")
name=guest[2].title()
print(name + ",I invite you to have dinner with me.")
name=guest[3].title()
print(name + ",I invite you to have dinner with me.")
name=guest[4].title()
print(name + ",I invite you to have dinner with me.")
name=guest[5].title()
print(name + ",I invite you to have dinner with me.")
print("\nUnfortunately the table wont be arriving on time and we only have 2 extra seats.")

name=guest.pop()
print("Sorry," + name.title() + " theres only two chairs left and unfortunately they have been offered to someone else.")
name=guest.pop()
print("Sorry," + name.title() + " theres only two chairs left and unfortunately they have been offered to someone else.")
name=guest.pop()
print("Sorry," + name.title() + " theres only two chairs left and unfortunately they have been offered to someone else.")
name=guest.pop()
print("Sorry," + name.title() + " theres only two chairs left and unfortunately they have been offered to someone else.")

name = guest[0].title()

print(name + ",I invite u to take one of the two empty chair.")
name=guest[1].title()
print(name + ",I invite u to take one of the two empty chair.")
del(guest[0])
del(guest[0])
print(guest)





