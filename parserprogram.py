import sys
import re
from file2CFG import txtToCFG
from CFG2CNF import CFG2CNF

def readFile(filename):
    with open(filename, "r") as f:
        text = f.read()
    return text

def testInput(input):
    key = {"False" : "a", "class" : "b", "is" : "c", "return" : "d", "None" : "e", "Continue" 
           : "f", "for" : "g", "True" : "h", "def" : "i", "from" : "j", "while" 
           : "k", "and" : "l", "not" : "m", "with" : "n", "as" : "o", "elif" 
           : "p", "if" : "q", "or" : "r", "else" : "s", "import" : "t", "pass" : "u", "break" 
           : "v", "in" : "w", "raise" : "A"}
    newInput = ""
    while input:
        x = re.search("[A-Za-z_][A-Za-z0-9_]*", input)
        if x != None:
            newInput += input[:x.span()[0]]
            if x.group() not in key:
                newInput += "x"
            else:
                newInput += key[x.group()]
            input = input[x.span()[1]:]
        else:
            newInput += input
            input = ""

    newInput = re.sub("[0-9]+[A-Za-z_]+", "R", newInput)
    newInput = re.sub("[0-9]+", "y", newInput)
    newInput = re.sub("#.*", "", newInput)
    multiString = re.findall(r'([\'\"])\1\1(.*?)\1{3}', newInput, re.DOTALL)

    for i in range(len(multiString)):
        multi = multiString[i][0]*3 + multiString[i][1] + multiString[i][0]*3
        newInput = newInput.replace(multi, "z\n" * multiString[i][1].count("\n"))

    str = re.findall(r'([\'\"])(.*?)\1{1}', newInput, re.DOTALL)
    
    for i in range(len(str)):
        one = str[i][0] + str[i][1] + str[i][0]
        newInput = newInput.replace(one, "z")

    newInput = newInput.replace(" ", "")
    newInput = re.sub("[xyz]{1}:[xyz]{1},", "", newInput)
    return (newInput + '\n')

def CYK(input, CNF, tst):
    #initialize
    length = len(input)
    nonTerminal = len(CNF)
    lines = tst.split('\n')
    
    line = {}
    pos = []
    count = 0
    for i in range(len(input)):
        if (input[i] == '\n'):
            count += 1
            line[i] = count
            pos.append(i)
    
    parse = [[[0 for i in range(nonTerminal + 1)] for i in range(length + 1)] for i in range(length + 1)]
    terminal = [None] * (nonTerminal+1)
    nt = {}
    
    #Append
    for i, variable in enumerate(CNF):
        nt[variable] = i + 1
        terminal[i+1] = CNF[variable]
        
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
    
    #hasil
    if(parse[length][1][1]):
        print("Accepted")
    else:
        print("Syntax Error\n")
        j = 1
        for i in range(length, 0, -1):
            if (parse[i][1][1]):
                break
            if (input[i - 1] == '\n'):
                j = line[i - 1]
        while (lines[j - 1][0] == ' '):
            lines[j - 1] = lines[j - 1][1:]
        print("Terjadi kesalahan ekspresi pada line", j, ":", lines[j - 1])

# CNF
CNF = CFG2CNF(txtToCFG("cfg.txt"))

# file input
if (len(sys.argv) < 2):
    filename = "inputAcc.py"
else:
    filename = sys.argv[1]

tst = readFile(filename)
input = testInput(readFile(filename))

# Parsing
CYK(input, CNF, tst)
