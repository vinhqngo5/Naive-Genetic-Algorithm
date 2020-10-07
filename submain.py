from bisector import Bisector
from random import seed
from population import Population
from datetime import timedelta
import calculate_fitness_function
import time
import threading
from threading import Lock
data_lock = Lock()
def print_answer(j, crossover_method, fitness_function, i, sum_MRPS, sum_Evaluations):
    MRPS, Evaluations = Bisector.find_minimum_population_size(j, Population.one_point_crossover, calculate_fitness_function.one_max, seed_offset = i)
    with data_lock:
        sum_MRPS += MRPS
        sum_Evaluations += Evaluations
    print(i)
    print ("MRPS: ", MRPS, "Evaluation: ", Evaluations)
    f.write ("MRPS: " + str(MRPS) + "Evaluation: " + str(Evaluations) + "\n")

f = open("output_multithread.txt", "a")
print('*********One_Max (one_point_crossover)*********')
f.write('*********One_Max (one_point_crossover)*********\n')

sum_MRPS, sum_Evaluations = 0, 0
# cases = [10, 20, 40, 80, 160]
cases = [10, 20, 40]
for j in cases:

    print("size of binary_string:", j)
    f.write("size of binary_string: " + str(j) +"\n")

    t0 = time.time()
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=print_answer, args=(j, Population.one_point_crossover, calculate_fitness_function.one_max, i, sum_MRPS, sum_Evaluations,)))
        threads[i].start()
    threads[0].join()
    threads[1].join()
    threads[2].join()
    threads[3].join()
    threads[4].join()
    threads[5].join()
    threads[6].join()
    threads[7].join()
    threads[8].join()
    threads[9].join()


    print ("mean_MRPS:", sum_MRPS / 10, "\nmean_Evaluations:", sum_Evaluations / 10)
    f.write ("mean_MRPS:" + str(sum_MRPS / 10) + "\nmean_Evaluations:" + str(sum_Evaluations / 10) + "\n")


    t0 = int(round(time.time()-t0))

    
    print('Running time: {}\n'.format(timedelta(seconds=t0)))
    print("--------------------------")
    f.write('Running time: {}\n'.format(timedelta(seconds=t0)))
    f.write("--------------------------\n")

f.close()