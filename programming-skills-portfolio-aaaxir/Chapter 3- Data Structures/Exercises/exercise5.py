"""You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations.

You'll have to think of someone else to invite.

Start with your program from Exercise 3-4. Add a print() call at the end of your program stating

Modify your list, replacing the name of the guest who can't make it with the name of the new pers

Print a second set of invitation messages, one for each person who is still in your list."""

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