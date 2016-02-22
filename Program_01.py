#Lab assignment 01
#CSC-201  Yi Xu

#Project 1 Half Pyramid
＃test

level = int(input('How many levels should the pyramid have?: '))
bb = input('What kind of building block (character) do you want to use for the pyramid: ')

print('The right half of the pyramid:')
for i in range(level):
    print(bb + (i * bb))



#Project 2 The Full Pyramid

level = int(input('How many levels should the pyramid have?: '))
bb = input('What kind of building block (character) do you want to use for the pyramid: ')

print('The complete, symmetric pyramid:')
for i in range(level):
    print(((level - i) * ' ') + (2 * i + 1) * bb)


#Project 3 Fix the problem

level = int(input('How many levels should the pyramid have?: '))
bb = input('What kind of building block (character) do you want to use for the pyramid: ')
n = len(bb)

print('The complete, symmetric pyramid:')
for i in range(level):
    print(((level - i) * n * ' ') + (2 * i + 1) * bb)



#Project 4 The Parabola, Right Side Up

minx = int(input('Enter the minimum value of x: '))
maxx = int(input('Enter the maximum value of x: '))
scaling_fac = float(input('Enter the scaling factor for the parabola: '))
i = minx

while i <= maxx:
    y = scaling_fac * (i ** 2)
    print((int(y - 1) * ' ') + ('*'))
    i += 1


#Project 5 Drawing A Circle

r = int(input('Enter the radius of the circle: '))


for i in range(r):
    y = ((r ** 2) - ((r - i) ** 2)) ** 0.5
    print((int(r - y) * ' ') + ('*') + (int(y * 2) * ' ') + ('*'))


for j in range(r):
    y = ((r ** 2) - ((j) ** 2)) ** 0.5
    print((int(r - y) * ' ') + ('*') + (int(y * 2) * ' ') + ('*'))
