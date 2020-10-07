from random import seed
from population import Population
import calculate_fitness_function

class Bisector:
    @staticmethod
    def find_upperbound(l_size, crossover_method, fitness_function, tournament_size = 4, seed_offset = 0, num_runs = 10):
        upper_bound = 2
        success = False
        while not success:
            upper_bound = 2 * upper_bound
            if (upper_bound > 8192):
                return -1
            success = 0
            for i in range(num_runs):
                seed(19520354 + 10 * seed_offset + i)
                population = Population(upper_bound, l_size)
                stable, evolved_population, evaluations = population.evolve_population(crossover_method, fitness_function, tournament_size)
                # print(stable, evaluations, len(evolved_population))
                if stable:
                    success += 1
        return upper_bound
    
    @staticmethod
    def find_minimum_population_size(l_size, crossover_method, fitness_function, tournament_size = 4, seed_offset=0, num_runs=10):
        upper_bound = Bisector.find_upperbound(l_size, crossover_method, fitness_function)
        # print("upper_bound:", upper_bound)
        if upper_bound == -1: return -1
        lower_bound = 1
        res_size = (upper_bound + lower_bound) // 2
        while(lower_bound <= upper_bound):
            res_size = (upper_bound + lower_bound) // 2
            # print(res_size)
            success = 0
            for i in range(num_runs):
                seed(19520354 + 10 * seed_offset + i)
                population = Population(res_size, l_size)
                stable, evolved_population, evaluations = population.evolve_population(crossover_method, fitness_function, tournament_size)
                if stable:
                    success += 1
            if (success):
                upper_bound = res_size - 1
            else:
                lower_bound = res_size + 1
        return res_size, evaluations
            
            

    


