class Individual:
    def __init__ (self, binary_string):
        # Construct an individual with binary_string
        self.binary_string = binary_string
    # Passing a delegate to calculate fitness of individuals

    def fitness(self, fitness_function):
        return fitness_function(self.binary_string)

    @property
    def clone(self):
        return Individual(self.binary_string)
    def length(self):
        return len(self.binary_string)
    