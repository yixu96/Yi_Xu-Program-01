#Lab assignment 01
#CSC-201  Yi Xu

#Project 1 Half Pyramid

level = int(input('How many levels should the pyramid have?: '))
bb = input('What kind of building block (character) do you want to use for the pyramid: ')
#We make sure our level of pyramid and the character we want to use for the pyramid
print('The right half of the pyramid:')
for i in range(level):
    print(bb + (i * bb))
#Print the character multiply the level


#Project 2 The Full Pyramid

level = int(input('How many levels should the pyramid have?: '))
bb = input('What kind of building block (character) do you want to use for the pyramid: ')
#We make sure our level of pyramid and the character we want to use for the pyramid
print('The complete, symmetric pyramid:')
for i in range(level):
    print(((level - i) * ' ') + (2 * i + 1) * bb)
##This step can draw the symmetric pyramid


#Project 3 Fix the problem

level = int(input('How many levels should the pyramid have?: '))
bb = input('What kind of building block (character) do you want to use for the pyramid: ')
#Enter the level of pyramid and character
n = len(bb)
#Double character for the pyramid
print('The complete, symmetric pyramid:')
for i in range(level):
    print(((level - i) * n * ' ') + (2 * i + 1) * bb)
#Math formula for this symmetric pyramid



#Project 4 The Parabola, Right Side Up

minx = int(input('Enter the minimum value of x: '))
maxx = int(input('Enter the maximum value of x: '))
scaling_fac = float(input('Enter the scaling factor for the parabola: '))
i = minx
#Maximum, minimum value and the sacling factor of the parabola
while i <= maxx:
    y = scaling_fac * (i ** 2)
    print((int(y - 1) * ' ') + ('*'))
    i += 1
#If i is bigger than max, it won't run successfully
#For i <= maximum, use int(y-1)*'' + '*' and it will stop until it becomes maximum number


#Project 5 Drawing A Circle

r = int(input('Enter the radius of the circle: '))
#Radius of the circle

for i in range(r):
    y = ((r ** 2) - ((r - i) ** 2)) ** 0.5
    print((int(r - y) * ' ') + ('*') + (int(y * 2) * ' ') + ('*'))
#This is the formula of half circle

for j in range(r):
    y = ((r ** 2) - ((j) ** 2)) ** 0.5
    print((int(r - y) * ' ') + ('*') + (int(y * 2) * ' ') + ('*'))
#This is the last of the circle so that it can constitute the whole circle
