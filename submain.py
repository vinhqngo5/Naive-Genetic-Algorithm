from bisector import Bisector
from random import seed
from population import Population
from datetime import timedelta
import calculate_fitness_function
import time
import multiprocessing
from multiprocessing import Pool
def print_answer(j, crossover_method, fitness_function, i):
    MRPS, Evaluations = Bisector.find_minimum_population_size(j, crossover_method, fitness_function, seed_offset = i)
    print ("MRPS: ", MRPS, " Evaluation: ", Evaluations)



if __name__ == "__main__":
    print('*********One_Max (one_point_crossover)*********')

    cases = [10, 20, 40, 80, 160]
    for j in cases:
        print("size of binary_string:", j)
        t0 = time.time()
        processes = []
        for i in range(10):
            processes.append(multiprocessing.Process(target=print_answer, args=(j, Population.one_point_crossover, calculate_fitness_function.one_max, i,)))
            processes[i].start()
        for i in range(10):
            processes[i].join()
        t0 = int(round(time.time()-t0))
        print('Running time: {}\n--------------------------'.format(timedelta(seconds=t0)))