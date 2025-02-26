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
    
    return is_equal(predecessor(a), predecessor(b))

#returns true if a > b
def is_greater(a, b):
    #If both are equal
    if not a and not b:
        return False
    #If a is greater
    if a and not b:
        return True
    #if b is greater
    if not a and b:
        return False
    return is_greater(predecessor(a), predecessor(b))

#returns if a < b
def is_less(a, b):
    if not a and not b:
        return False
    if a and not b:
        return False
    if not a and b:
        return True
    return is_less(predecessor(a), predecessor(b))


#Counting w/ successor function where successor(n) = n + 1 in traditional math
def successor(n):
    if "successor" in universe:
        del universe["successor"]
    label(n.copy(), "successor", universe)
    universe["successor"].append(n) 
    return universe["successor"]


#Assignment replacements
#Labels the value and does nothing else
def label(value, label, group):
    group.update({label: value}) 

#Labels the value and adds to specified sub-list within universe
#Value will exist both in the universe group AND the list, used for countTo
def labelAppend(value, name, group, List):
    label(value, name, group)
    group[List].append(group[name])

#Adding function, add if a & b != 0, then add(a, S(b)) = S(add(a, b)) where S is successor
def add(a, b):
    # Base case: If b is zero (i.e., the empty set), return a (no change)
    if not b:
        return a
    # Recursive case: Apply successor to a and decrement b
    return add(successor(a), predecessor(b))

#Multiply function where if A & B != 0, multiply(a, add(a,b)) = add(multiply(a, b))
def multiply(a, b):
    # Base case: If b is zero, return zero
    if not b:
        return zero()
    
    # Recursive case: Add a to the result of multiply(a, b - 1)
    return add(a, multiply(a, b[1:]))
    
    #Defines and labels all numbers up to the given parameter, assuming the parameter IS a labled number in numberlist
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

#prints all elements in universe that isnt successor label or numberlist label
def listNumbers():
    for element in universe:
        if element in {"successor"} or element in {"numberlist"}:
            continue
        print(element)

#Predecessor (P) of n is as follows, P(S(x)) = x, where n = S(x) or P(n) = n -1
def predecessor(n):
    if "predecessor" in universe:
        del universe["predecessor"]
    label(n.copy(), "predecessor", universe)
    universe["predecessor"].pop() 
    return universe["predecessor"]

label(zero(), "numberlist", universe)
#For reference, numberlist contains all VALUES, the universe dictionary contains the VALUES AND LABELS

labelAppend(successor(zero()), "one", universe, "numberlist")
labelAppend(successor(universe["one"]), "two", universe, "numberlist")

listNumbers()


