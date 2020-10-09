from bisector import Bisector
from random import seed
from population import Population
from datetime import timedelta
import calculate_fitness_function
import time

f = open("result\\test.txt", "a")
print('*********OneMax (one_point_crossover)*********')
f.write('*********OneMax (one_point_crossover)*********\n')

sum_MRPS, sum_Evaluations = 0, 0
cases = [10, 20, 40, 80, 160]

for j in cases:
    sum_MRPS, sum_Evaluations = 0, 0
    print("size of binary_string:", j)
    f.write("size of binary_string: " + str(j) +"\n")

    t0 = time.time()
    for i in range(10):
        MRPS, Evaluations = Bisector.find_minimum_population_size(j, Population.one_point_crossover, calculate_fitness_function.one_max, seed_offset = i)
        sum_MRPS += MRPS
        sum_Evaluations += Evaluations

        print ("MRPS: ", MRPS, "Evaluation: ", Evaluations)
        f.write ("MRPS: " + str(MRPS) + " Evaluation: " + str(Evaluations) + "\n")


    print ("mean_MRPS:", sum_MRPS / 10, "\nmean_Evaluations:", sum_Evaluations / 10)
    f.write ("mean_MRPS:" + str(sum_MRPS / 10) + "\nmean_Evaluations:" + str(sum_Evaluations / 10) + "\n")


    t0 = int(round(time.time()-t0))

    
    print('Running time: {}\n'.format(timedelta(seconds=t0)))
    print("--------------------------")
    f.write('Running time: {}\n'.format(timedelta(seconds=t0)))
    f.write("--------------------------\n")

f.close()