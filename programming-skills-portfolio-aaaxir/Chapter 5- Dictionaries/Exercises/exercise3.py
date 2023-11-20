"""Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output."""


subjects={
    'Program': 'A computer program is termed as an organized collection of instructions, which when executed perform a specific task or function.',
    'Code': 'Code or source code is a term used to describe a written set of instructions, written using the protocols of a particular language, such as Java, C or Python.',
    'Variable': 'A variable is a location that stores temporary data within a program which can be modified, store and display whenever need',
    'Machine language': "Also known as machine code, machine language is a lowest-level programming language consisting of binary digits or bits that are read by computers.",
    'Low-level language':'A low-level language is a language that is very close to machine language and provides a little abstraction of programming concepts.',}
Program='Program'
print("\n" + Program.title() + ":" + subjects[Program])
Program='Code'
print("\n" + Program.title() + ":" + subjects[Program])
Program= 'Variable'
print("\n" + Program.title() + ":" + subjects[Program])
Program= 'Machine language'
print("\n" + Program.title() + ":" + subjects[Program])
Program= 'Low-level language'
print("\n" + Program.title() + ":" + subjects[Program])
Program={
'value': 'An item associated with a key in a dictionary.',
'float': 'A numerical value with a decimal component.',
'boolean expression': 'An expression that evaluates to True or False.',
'string': 'A series of characters.',
'list': 'A collection of items in a particular order.',}
for word, definition in Program.items():
    print("\n" + word.title() + ": " + definition)