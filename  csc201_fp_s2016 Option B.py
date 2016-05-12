import csv
import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.legend_handler import HandlerLine2D

def extract_election_vote_counts(filename, column_names):
    open_file = open(filename)
    data = csv.DictReader(open_file)
    nvote = []
    for row in data:
        for i in column_names:
            if row[i] != '':
                nvote.append(int(row[i].replace(',', '')))
            else:
                nvote.append(0)
    open_file.close()
    return nvote


def ones_and_tens_digit_histogram(numbers):
    result = []
    num1 = []
    num2 = []
    for n in numbers:
        num1.append(int(str(n)[-1]))
        if n < 10:
            num2.append(0)
        else:
            num2.append(int(str(n)[-2]))
    for i in range(10):
        ni = 0
        for n1 in num1:
            if n1 == i:
                ni += 1
        for n2 in num2:
            if n2 == i:
                ni += 1
        result.append(ni)

    sumre = sum(result)
    for i in range(10):
        result[i] = result[i] / sumre

    return result


def plot_iranian_least_digits_histogram(histogram):
    x = np.arange(0, 10, 1)
    y = histogram
    y0 = [0.1] * 10
    line, = plt.plot(x, y0, label='Ideal', color='blue')
    line1, = plt.plot(x, y, label='Iran', color='green')
    plt.legend(handler_map={line: HandlerLine2D(numpoints=4)})

    plt.xlabel('Digit')
    plt.ylabel('Frequency')
    plt.savefig('iran-digits.png')
    plt.show()


def plot_distribution_by_sample_size():
    sizes = [10, 50, 100, 1000, 10000]
    for i in sizes:
        x = np.arange(0, 10, 1)
        y0 = [0.1] * 10
        nums = np.random.randint(100, size=i)
        y1 = ones_and_tens_digit_histogram(nums)
        line, = plt.plot(x, y0, label='Ideal', color='blue')
        line1, = plt.plot(x, y1, label=(str(i) + ' random numbers'), color='green')
        plt.legend(handler_map={line: HandlerLine2D(numpoints=4)})
        plt.show()
        # plt.clf()


def mean_squared_error(numbers1, numbers2):
    l = len(numbers1)
    ds = []
    for i in range(l):
        ds.append((numbers1[i] - numbers2[i]) ** 2)
    MSE = sum(ds) / l
    return MSE


def calculate_mse_with_uniform(histogram):
    uniforms = [0.1] * 10
    return mean_squared_error(histogram, uniforms)


def compare_iranian_mse_to_samples(iranian_mse, number_of_iranian_samples):
    le = 0
    sm = 0
    for i in range(10000):
        ran_nums = np.random.randint(100, size=number_of_iranian_samples)
        y = ones_and_tens_digit_histogram(ran_nums)
        MSEs = calculate_mse_with_uniform(y)
        if MSEs >= iranian_mse:
            le += 1
        else:
            sm += 1

    print('Quantity of MSEs larger than or equal to the 2009 Iranian election MSE: ', le)
    print('Quantity of MSEs smaller than 2009 Iranian election MSE: ', sm)
    print('2009 Iranian election null hypothesis rejection level p: ', le/10000)


def compare_us_mse_to_samples(us_mse, number_of_us_samples):    #怎么可能跟iranian的没有重复
    le = 0
    sm = 0
    for i in range(10000):
        ran_nums = np.random.randint(100, size=number_of_us_samples)
        y = ones_and_tens_digit_histogram(ran_nums)
        MSEs = calculate_mse_with_uniform(y)
        if MSEs >= us_mse:
            le += 1
        else:
            sm += 1

    print('Quantity of MSEs larger than or equal to the 2008 United States election MSE: ', le)
    print('Quantity of MSEs smaller than 2008 United States election MSE: ', sm)
    print('2008 United States election null hypothesis rejection level p: ', le / 10000)



def main():


lis00 = extract_election_vote_counts('C:/election-iran-2009.csv', ['Ahmadinejad', 'Rezai', 'Karrubi', 'Mousavi'])
print(lis00)

lis0 = [127, 426, 28, 9, 90]
ones_and_tens_digit_histogram(lis0)

lis1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
ones_and_tens_digit_histogram(lis1)

histogram00 = ones_and_tens_digit_histogram(lis00)
print(histogram00)

plt.figure(1)
plot_iranian_least_digits_histogram(histogram)

plt.figure(2)
plot_distribution_by_sample_size()

mse = mean_squared_error([1, 4, 9], [6, 5, 4])
print(mse)

mse_uni00 = calculate_mse_with_uniform(histogram00)
print(mse_uni00)

compare_iranian_mse_to_samples(mse_uni00, len(lis00))

with open('answers.txt', 'w') as af:      ###interpretation不造写啥
  p = input('Enter the p level according to the results: ')
  q = 1 - float(p)
  af.write('p = ' + p + ' level\n')
  af.write('The Iranian election results were ' + str(q) + ' confident fraudulent.\n')

  threshhold_stat_sign = 0.05
  if float(p) <= threshhold_stat_sign:
    af.write('The Iranian election results were fraudulent.')

with open('answers.txt', 'r') as f:
  print(f.read())

lis11 = extract_election_vote_counts('C:/election-us-2008.csv', ['Obama', 'McCain', 'Nader', 'Barr', 'Baldwin', 'McKinney'])
print(lis11)

histogram11 = ones_and_tens_digit_histogram(lis11)
print(histogram11)


mse_uni11 = calculate_mse_with_uniform(histogram11)
print(mse_uni11)

compare_us_mse_to_samples(mse_uni11, len(lis11))

with open('answers.txt', 'w') as af:      ###interpretation不造写啥
    p = input('Enter the p level according to the results: ')
    q = 1 - float(p)
    af.write('p = ' + p + ' level\n')
    af.write('The US election results were ' + str(q) + ' confident fraudulent.\n')

    threshhold_stat_sign = 0.05
    if float(p) <= threshhold_stat_sign:
        af.write('The US election results were fraudulent.')

with open('answers.txt', 'r') as f:
    print(f.read())




#     if _name_ == '_main_':
#         main()
#
#
