import matplotlib.pyplot as plt
from option import graph_option
import math

def draw_graph(filepath, label_name, type):
    with open(filepath, "r") as f:
        content = f.readlines()
    MRPS = list(map(float, content[0].split()))
    size = list(map(float, content[1].split()))
    yerr = list(map(float, content[2].split()))
    plt.plot()
    plt.yscale('symlog')
    plt.xscale('symlog')
    plt.errorbar(size, MRPS, yerr = yerr, fmt = type, label = label_name)


print("1. ONEMAX_MRPS\n2. ONEMAX_Evaluations\n3. TRAP_MRPS\n4. TRAP_Evaluations")
choose = int(input("Choose one of above: "))
path1, path2, label1, label2, graph_label = graph_option(choose)
draw_graph(path1, label1, '-ro')
draw_graph(path2, label2, '-bo')
plt.ylabel(graph_label)
plt.legend()
plt.show()
