from player import Player
p = Player()
#Commands = p.Commands()

p.name = input("What is your character's name? ")
print("(type help to get a list of actions)\n")
print("%s enters a dark cave, searching for adventure." % p.name)

while (p.health > 0):
    line = input("> ")
    args = line.split()
    if len(args) > 0:
        commandFound = False
        for c in p.Commands.keys():
            if args[0] == c[:len(args[0])]:
                p.Commands[c](p)
                commandFound = True
                break
        if not commandFound:
            print("%s doesn't understand the suggestion." % p.name)

"""Copyright <2018> <RITUSHREE SAHU>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""
