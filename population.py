from individual import Individual
from random import randint
from math import log2
import extension
import calculate_fitness_function
class Population:
    def __init__(self, population_size, l_size):
        self.individuals = []
        self.Evaluation_times = 0
        self.l_size = l_size
        self.population_size = population_size
        # using method in extention to create a random binary string with size l
        for _ in range(population_size):
            binary_string = extension.create_random_binary_string(l_size)
            self.individuals.append(Individual(binary_string))

    # one-point crossover 
    @staticmethod
    def one_point_crossover(parent1, parent2):
        sub_child1, sub_child2 = [], []
        # Create a random crossover_point
        crossover_point = randint(0, parent1.length())
        for i in range(crossover_point):
            sub_child1.append(parent1.binary_string[i])
            sub_child2.append(parent2.binary_string[i])
        for i in range(crossover_point, parent1.length()):
            sub_child1.append(parent2.binary_string[i])
            sub_child2.append(parent1.binary_string[i])
        child1 = Individual(''.join(sub_child1))
        child2 = Individual(''.join(sub_child2))
        return child1, child2

    # uniform crossover
    @staticmethod
    def uniform_crossover(parent1, parent2):
        sub_child1, sub_child2 = [], []
        for i in range(parent1.length()):
            if (randint(0, 1)):
                sub_child1.append(parent1.binary_string[i])
                sub_child2.append(parent2.binary_string[i])
            else:
                sub_child1.append(parent2.binary_string[i])
                sub_child2.append(parent1.binary_string[i])
        child1 = Individual(''.join(sub_child1))
        child2 = Individual(''.join(sub_child2))
        return child1, child2

    # breeding best_individuals with delegate is crossover_method
    @staticmethod
    def breeding_best_individuals(best_individuals, crossover_method):
        new_offspring = []
        extension.shuffle_list_randomly(best_individuals)
        for i in range(0, len(best_individuals) // 2):
            parent1, parent2 = best_individuals[2 * i], best_individuals[2 * i + 1]
            child1, child2 = crossover_method(parent1, parent2)
            new_offspring.append(child1)
            new_offspring.append(child2)
        while (len(new_offspring) < len(best_individuals)):
            new_offspring.append(best_individuals[-1])
        
        new_population = best_individuals + new_offspring
        return new_population

    # check if population has best individual
    def check_popuation(self, fitness_function):
    	for i in range(len(self.individuals)):
            if (self.individuals[i].fitness(fitness_function) == self.l_size):
                self.Evaluation_times += 1
                return 1
            if (i == len(self.individuals) - 1):
                return 0
        

    # tournament_selection to select N / 4 best individuals
    def tournament_selection(self, fitness_function = calculate_fitness_function.one_max, tournament_selection_size = 4):
        best_individuals = []
        while (len(best_individuals) < self.population_size):
            extension.shuffle_list_randomly(self.individuals)
            for i in range(len(self.individuals) // tournament_selection_size):
                max_fitness_pos, max_fitness_score = i * tournament_selection_size, self.individuals[i * tournament_selection_size].fitness(fitness_function)
                self.Evaluation_times += 1
                for j in range(1, tournament_selection_size):
                    fitness_score = self.individuals[i * tournament_selection_size + j].fitness(fitness_function)
                    self.Evaluation_times += 1
                    if (fitness_score > max_fitness_score):
                        max_fitness_pos = i * tournament_selection_size + j
                        max_fitness_score = fitness_score
                best_individuals.append(self.individuals[max_fitness_pos])
                if (len(best_individuals) >= self.population_size):
                    break
        return best_individuals

    # create new population for only one time
    def onetime_evolve_population(self, crossover_method, fitness_function = calculate_fitness_function.one_max, tournament_selection_size = 4):
        off_spring = Population.breeding_best_individuals(self.individuals, crossover_method)
        self.individuals = off_spring
        best_individuals1 = self.tournament_selection(fitness_function, tournament_selection_size)
        best_individuals2 = self.tournament_selection(fitness_function, tournament_selection_size)
        self.individuals = best_individuals1 + best_individuals2
        return self.individuals

    # evolve the population until it is stable
    def evolve_population(self, crossover_method, fitness_function = calculate_fitness_function.one_max, tournament_selection_size = 4):
        count_stable_times = 0
        count_generations = 0
        average_fitness = self.calculate_average_fitness(fitness_function)
        while count_stable_times < log2(self.population_size):
            # print(average_fitness)
            self.onetime_evolve_population(crossover_method, fitness_function, tournament_selection_size)
            new_average_fitness = self.calculate_average_fitness(fitness_function)
            if (new_average_fitness <= average_fitness):
                count_stable_times += 1
            else: 
                count_stable_times = 0
            average_fitness = new_average_fitness
            count_generations += 1 
            # count generation là đếm số thế hệ, Evaluation_times là số lần gọi hàm fitness
        return self.check_popuation(fitness_function) ,self.individuals, self.Evaluation_times

    # calculate average fitness of the population
    def calculate_average_fitness(self, fitness_function):
        fitness_sum = 0
        for i in range(len(self.individuals)):
            fitness_sum += self.individuals[i].fitness(fitness_function)
        fitness_sum /= len(self.individuals)
        return fitness_sum
    

    
