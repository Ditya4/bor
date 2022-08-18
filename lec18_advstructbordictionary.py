'''
Created on Aug 17, 2022
there are a few words in the dictionary. we need to
create a fast way to check
is there a such word in the dictionary or not?
      top
     / | \
    t  d  e
   /|  \  /\
  o i  o n z
    \    \
    d     d
@author: dno
'''


class Vertex:

    def __init__(self, letter):
        self.letter = letter
        self.letters = dict()
        if letter == ".":
            self.letters['None'] = None

    def add_letter(self, letter, vertex):
        '''
        we need to assign a new Vertex to the identifier letter
        '''
        self.letters[letter] = vertex

    def __str__(self):
        result = ""
        for letter in self.letters.keys():
            result += letter
        return self.letter + "<-letter, letters ->" + result


vertex = [Vertex('0')]
words = ["five", "fine"] # , "finally", "poker", "parker"]
vertex_index = len(vertex)
for word in words:
    for i in range(len(word) + 1):  # +1 to create a final word point
        ##if i == 0:
        ##    vertex.append(Vertex(word[i]))
        ##elif i < len(word):
        if i < len(word):
            vertex.append(Vertex(word[i]))
            vertex[vertex_index - 1].add_letter(word[i], vertex[vertex_index])
        elif i == len(word):
            vertex.append(Vertex("."))
            vertex[vertex_index - 1].add_letter(".", vertex[vertex_index])
        vertex_index += 1

print(list(map(str, vertex)))

index = 0
next_element = vertex[index]
for letter in "five":
    next_element = next_element.letters[letter]
    if letter in next_element.letters:
        print(letter, "in letters", next_element.letters.keys)
    else:
        print(letter, next_element.letters.keys())
    print(next_element)






