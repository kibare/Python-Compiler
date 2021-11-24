def readDFA(file):
    with open(file, "r") as f:
        content = f.read()
        content = content.split("\n")
        state = content[0]
        input = content[1]
        start = content[2]
        final = content[3]
        for i in range(4, len(content)):
            transisi[i]
        '''
        tidak selesai :(
        '''
        
        

def validated(var):
    state, input, start, final, transisi = readDFA("dfa.txt")
    stateNow = start
    i = 0
    while(i < len(var) and stateNow != 'x'):
        if var[i] in (['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
                       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']):
            tipe = "huruf"
        elif var[i] in (["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]):
            tipe = "angka"
        elif var[i] == "_":
            tipe = "underscore"
        else:
            tipe = "tidak diketahui"
            
        if tipe in input:
            stateNow = transisi[f"{stateNow},{tipe}"]
        else:
            return False
        
        i += 1
        
    if stateNow == final:
        return True
    else:
        return False