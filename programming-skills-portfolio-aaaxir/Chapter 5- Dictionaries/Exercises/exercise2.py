"""A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

* Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 

their meanings as values.

* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 

the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 

each word-meaning pair in your output."""


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


