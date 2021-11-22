'''
Referensi (Wikipedia):
let the input be a string I consisting of n characters: a1 ... an.
let the grammar contain r nonterminal symbols R1 ... Rr, with start symbol R1.
let P[n,n,r] be an array of booleans. Initialize all elements of P to false.

for each s = 1 to n
    for each unit production Rv → as
        set P[1,s,v] = true

for each l = 2 to n -- Length of span
    for each s = 1 to n-l+1 -- Start of span
        for each p = 1 to l-1 -- Partition of span
            for each production Ra    → Rb Rc
                if P[p,s,b] and P[l-p,s+p,c] then set P[l,s,a] = true

if P[n,1,1] is true then
    I is member of language
else
    I is not member of language
'''

def CYK(input, CNF):
    #initialize
    length = len(input)
    nonTerminal = len(CNF)
    
    parse = [[[0 for i in range(nonTerminal + 1)] for i in range(length + 1)] for i in range(length + 1)]
    terminal1 = [None] * (nonTerminal+1)
    nt = {}
    
    #Append
    for i, variable in enumerate(CNF):
        nt[variable] = i + 1
        terminal1[i+1] = CNF[variable]
        
    #proses parsing
    #pake algorithm diatas (wikipedia)
    for s in range(1, length+1):
        for v in range(1, nonTerminal+1):
            for e in terminal1[v]:
                if(e[0] == input[s-1]):
                    parse[1][s][v] = True
                    break

    for l in range(2, length+1):
        for s in range(1, (length-l+2)):
            for p in range(1, l):
                for a in range(1, nonTerminal+1):
                    for e in terminal1[a]:
                        if(len(e) != 1):
                            b = nt[e[0]]
                            c = nt[e[1]]
                            if(parse[p][s][b] and parse[l-p][s+p][c]):
                                parse[l][s][a] = True
                                break
    
    #hasil (sementara)
    if(parse[length][1][1]):
        print("ACC")
    else:
        print("eRrOr")
    







