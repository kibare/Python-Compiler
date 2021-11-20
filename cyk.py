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

maxLength = 100
terminalMax = 20
p = [[[0 for i in range(terminalMax)] for i in range(maxLength)] for i in range(maxLength)]
terminal = [None]

#urutan nonterminal
nt = {}
nt['S'] = 1
nt['A'] = 2
nt['T'] = 3
nt['B'] = 4
nt['C'] = 5

terminal.append([["a"]])
terminal.append([["b"]])
terminal.append([["A", "B"]])
terminal.append([["a"], ["A", "C"]])
terminal.append([["T", "A"], ["B", "A"], ["A", "B"], ["b"]])

nInput = len(input)
nTerminal = 5

input = "a"*1000
if(len(input) == 0):
    print("LOLOS")
elif(len(input) >= 1000):
    print("Gagal")
    
#pake referensi diatas untuk algoritma cyknya
for s in range(1, nInput+1):
    for v in range(1, nTerminal+1):
        for e in terminal[v]:
            if(e[0] == input[s-1]):
                p[1][s][v] = True
                break

for l in range(2, nInput+1):
    for s in range(1, (nInput-l+2)):
        for p in range(1, l):
            for a in range(1, nTerminal+1):
                for e in terminal[a]:
                    if(len(e) != 1):
                        b = nt[e[0]]
                        c = nt[e[1]]
                        if(p[p][s][b] and p[l-p][s+p][c]):
                            p[l][s][a] = True
                            break
                        
if(p[nInput][1][1]):
    print("ACC")
else:
    print("sintaks error")






