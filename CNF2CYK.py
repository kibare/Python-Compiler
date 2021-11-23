def CYK(input, CNF):
    #initialize
    length = len(input)
    nonTerminal = len(CNF)
    
    parse = [[[0 for i in range(nonTerminal + 1)] for i in range(length + 1)] for i in range(length + 1)]
    terminal = [None] * (nonTerminal+1)
    nt = {}
    
    #Append
    for i, variable in enumerate(CNF):
        nt[variable] = i + 1
        terminal[i+1] = CNF[variable]
        
    #proses parsing
    #pake algorithm diatas (wikipedia)
    for s in range(1, length+1):
        for v in range(1, nonTerminal+1):
            for e in terminal[v]:
                if(e[0] == input[s-1]):
                    parse[1][s][v] = True
                    break

    for l in range(2, length+1):
        for s in range(1, (length-l+2)):
            for p in range(1, l):
                for a in range(1, nonTerminal+1):
                    for e in terminal[a]:
                        if(len(e) != 1):
                            b = nt[e[0]]
                            c = nt[e[1]]
                            if(parse[p][s][b] and parse[l-p][s+p][c]):
                                parse[l][s][a] = True
                                break
    
    #hasil (sementara)
    if(parse[length][1][1]):
        print("=====================")
        print("===Syntax Accepted===")
        print("=====================")
    else:
        print("=======================")
        print("=====Syntax Error=====")
        print("=======================")
    







