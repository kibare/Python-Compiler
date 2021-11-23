from copy import deepcopy
import string

def isVar(itm):
    if len(itm) == 1:
        return False
    for char in itm:
        if char not in (string.ascii_uppercase+'_'+string.digits):
            return False
    return True

def CFG2CNF(CFG):
	# Remove unit prod
    for var in CFG:
        prods = CFG[var]
        repeat = True
        while repeat:
            repeat = False
            for prod in prods:
                if len(prod) == 1 and isVar(prod[0]):
                    prods.remove(prod)
                    newprod = deepcopy([prod for prod in CFG[prod[0]]
                                        if prod not in prods])
                    prods.extend(newprod)
                    repeat = True
                    break
    newRule = {}
    for var in CFG:
        terminals = []
        prods = CFG[var]
        # Search terminals
        processprod = [prod for prod in prods if len(prod) > 1]
        for prod in processprod:
            for itm in prod:
                if not(isVar(itm)) and itm not in terminals:
                    terminals.append(itm)
        # Create new rule and update prod
        for i, terminal in enumerate(terminals):
            newRule.update({f"{var}_TERM_{i + 1}": [[terminal]]})
            for idx, j in enumerate(prods):
                if len(j) > 1:
                    for k in range(len(j)):
                        if len(prods[idx][k]) == len(terminal):
                            prods[idx][k] = prods[idx][k].replace(terminal, f"{var}_TERM_{i + 1}")
        # Update prods A -> BC or A -> b
        idx = 1
        for i in range(len(prods)):
            while len(prods[i]) > 2:
                newRule.update({f"{var}_EXT_{idx}": [[prods[i][0], prods[i][1]]]})
                prods[i] = prods[i][1:]
                prods[i][0] = f"{var}_EXT_{idx}"
                idx += 1
    CFG.update(newRule)
    return CFG
