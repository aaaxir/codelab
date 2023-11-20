"""Think of at least five places in the world you’d like to visit. • Store the locations in a list. Make sure the list is not in alphabetical order.

• Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.

• Use sorted() to print your list in alphabetical order without modifying the actual list.

• Show that your list is still in its original order by printing it.

• Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

• Show that your list is still in its original order by printing it again.

•"""


place =['Spiti valley', 'Umling La', 'Isle of man', 'Japan', 'Germany']
print("Original order: ")
print (place)
print("\nAlphabetical:")
print(sorted(place))
print("\noriginal order:")
print(place)
print("\nReversed: ")
place.reverse()
print (place)
print("\noriginal order: ")
place.reverse()
print(place)
print("\nAlphabetical")
place.sort()
print (place)
print("\nReverse alphabetical")
place.sort(reverse=True)
print (place)
print("\noriginal order: ")
print (place)




