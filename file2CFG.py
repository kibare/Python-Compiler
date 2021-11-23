def txtToCFG(filename):
    CFG = {}
    with open(filename, 'r') as f:
        lines = [line.split('->') for line in f.read().split('\n') if len(line.split('->')) == 2]
        for line in lines:
            var = line[0].replace(" ", "")
            rawProds = [rawProd.split() for rawProd in line[1].split('|')]
            prod = []
            for rawProd in rawProds:
                prod.append([" " if itm == "__space__" else "|" if itm == "__or__" else "\n" if itm == "__new_line__" else itm for itm in rawProd])
            CFG.update({var: prod})
    return CFG
