def graph_option(choose):
    print("1. ONEMAX_MRPS\n2. ONEMAX_Evaluations\n3. TRAP_MRPS\n4. TRAP_Evaluations")
    path1 = "..\\result\\"
    path2 = "..\\result\\"
    labe1, label2, graph_label = "", "", ""
    if (choose == 1):
        path1 += "MRPS\\onemax_1x.txt"
        path2 += "MRPS\\onemax_ux.txt"
        graph_label = "ONEMAX_MRPS"
        label1 = "one_point_crossover"
        label2 = "uniform_crossover"
    elif (choose == 2):
        path1 += "Evaluations\\onemax_1x.txt"
        path2 += "Evaluations\\onemax_ux.txt"
        graph_label = "ONEMAX_Evaluations"
        label1 = "one_point_crossover"
        label2 = "uniform_crossover"
    elif (choose == 3):
        path1 += "MRPS\\trap_1x.txt"
        path2 += "MRPS\\trap_ux.txt"
        graph_label = "TRAP_MRPS"
        label1 = "one_point_crossover"
        label2 = "uniform_crossover"
    elif (choose == 4):
        path1 += "Evaluations\\trap_1x.txt"
        path2 += "Evaluations\\trap_ux.txt"
        graph_label = "TRAP_Evaluations"
        label1 = "one_point_crossover"
        label2 = "uniform_crossover"
    return path1, path2, label1, label2, graph_label