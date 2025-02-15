#Assumption 1: Pure nothingness cant exist because talking about nothing implies something: nothing
#Assumption 2: Functions exist 
#Def of functions: Take input(s) and produce an output, existing by declaration since i need SOMETHING
#Only 1 assingment is allowed, for declaration of the number dictionary (For my own sanity of labeling)
import inflect

universe = {}

#Defining zero as the empty set
def zero():
    return []




#Defining simple equality, A = B iff |A| = |B|
def is_equal(a, b):
    if not a and not b:
        return True
    
    if not a or not b:
        return False
    
    return is_equal(a[1:], b[1:])

#Counting
def successor(n):
    if "successor" in universe:
        del universe["successor"]
    label(n.copy(), "successor", universe)
    universe["successor"].append(n) 
    return universe["successor"]

#Assignment replacement
def label(value, label, group):
    group.update({label: value}) 

def add(a, b):
    # Base case: If b is zero (i.e., the empty set), return a (no change)
    if not b:
        return a
    # Recursive case: Apply successor to a and decrement b
    return add(successor(a), b[1:])

def multiply(a, b):
    # Base case: If b is zero, return zero
    if not b:
        return zero()
    
    # Recursive case: Add a to the result of multiply(a, b - 1)
    return add(a, multiply(a, b[1:]))
    
def countTo(number):
    for element in universe["numberlist"]:
        if is_equal(element, number):
            continue
        #Skip if the successor exists in the number list
        if inflect.engine().number_to_words(len(successor(element))) in universe:
            continue
        #else, make the new number
        label(successor(element), inflect.engine().number_to_words(len(successor(element))), universe)
        #add new number to list
        universe['numberlist'].append(successor(element))
        #print(is_equal(universe,))


def listNumbers():
    for element in universe:
        if element in {"successor"} or element in {"numberlist"}:
            continue
        print(element)

def predecessor(n):
    if "predecessor" in universe:
        del universe["predecessor"]
    label(n.copy(), "predecessor", universe)
    universe["predecessor"].pop() 
    return universe["predecessor"]

#Use predecessor to subtract. ONLY WORKS FOR NATURALSz
def subtract(a, b):
    print(str(len(a)) + " " + str(len(b)))
    # Base case: If b is zero (i.e., the empty set), return a (no change)
    if not b:
        return a
    
    # Recursive case: Apply predecessor to a and decrement b
    return subtract(predecessor(a), predecessor(b))

label(zero(), "numberlist", universe)
#For reference, numberlist contains all VALUES, the universe dictionary contains the VALUES AND LABELS



label(successor(zero()), "one", universe) 
universe["numberlist"].append(universe["one"])

label(successor(universe["one"]), "two", universe)
universe["numberlist"].append(universe["two"])

label(successor(universe["two"]), "three", universe)
universe["numberlist"].append(universe["three"])

label(successor(universe["three"]), "four", universe)
universe["numberlist"].append(universe["four"])

label(multiply(universe["four"], universe["four"]), "sixteen", universe)
universe["numberlist"].append(universe["sixteen"])

label(multiply(universe["sixteen"], universe["sixteen"]), "two hundred and fifty-six", universe)
universe["numberlist"].append(universe["two hundred and fifty-six"])

countTo(universe["two hundred and fifty-six"])
