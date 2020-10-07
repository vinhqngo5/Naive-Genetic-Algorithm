def one_max(binary_string):
    fitness = binary_string.count('1')
    return fitness

def trap(binary_string, k = 5):
    fitness = 0
    for i in range(len(binary_string) // k):
        count = 0
        for j in range(k):
            if (binary_string[i * k + j] == '1'):
                count = count + 1
        if (count == k):
            fitness += k
        else: 
            fitness += (k - count - 1)
    return fitness