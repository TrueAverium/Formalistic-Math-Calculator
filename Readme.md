# Formalistic Math Calculator (N edition)

## Overview 
This calculator is a hobby project of mine, intended to build the natural numbers and its operations from first principles. The program starts with the empty set, and defines fundamental operations (equality, successor, addition etc.). This project aims to **formally** defined the natural number system using a logical computational approach. 

## Motivation
This started more as an interest in the question "Can I create mathematical operations in python without using actual mathematical operators? "(+, -, $*$, /). The challenge quickly expanded into starting from as little as possible, and defining the basics of math using no numbers, no equality, and only a single use of the assignment operator. The approach follows a first principles methodology, similar to Peano arithmetic, but is implemented in code to allow the user to explore the structures dynamically. 

## Formal Structure

The only explicit assignment in this code is at the start, declaring U

Over-Formally:

$U=\{M,S,N_{user}\}\owns$
	$M = \{f : A_f \rightarrow B_f\} \owns$
			M = {Successor, predecessor, add, multiply, label}
	$S = \{(L,V)|L\in\Sigma^*, V \in \mathbb{N}\}$
	$N_{user} = \{n_i | n_i \in \mathbb{N} \wedge \exists(L,n_i) \in S\}$

The functions of M follow these mappings:

Successor: $\mathbb{N} \rightarrow \mathbb{N}$, Successor($n$) = $n \cup \{n\}$ 
Predecessor: $\mathbb{N} \setminus \{0\} \rightarrow \mathbb{N}$, Predecessor(Successor($n$)) = $n$
Add: $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$, Add(a, b) = $\begin{cases} a & \text{if } b=0 \\ \text{Add(}\text{Successor}(a), \text{Predecessor}(b) \text{)} & \text{if } b > 0 \end{cases}$
Multiply: $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$, Multiply(a, b) = $\begin{cases} a & \text{if } b=0 \\ \text{Add(}a, \text{Multiply}(a, Predecessor(b)) \text{)} & \text{if } b > 0 \end{cases}$
Label: $V \times L \times S \to S$, Label(V, L, S) = S' $\owns S' = S \cup \{(L,V)\}$

In plain English:

The set U (universe) is defined on program start. U contains 3 different subsets within it. M, S, and $N_{user}$.

M is the group of functions that can be performed within U. These are predefined as: 
	Successor, Predecessor, Add, Multiply, and Label
S is the set of user defined labels. Each element in S is an ordered pair containing L, a label that can consist of any user defined alphabet, and V, a value within the set of naturals. 
$N_{user}$ is the set of values defined by the user. a value is within this set if, the value is a natural number and if there exists a label for this value within S.

More specifics on the functions within M:

Successor: This takes in a natural number defined by the user, Returns "The number that comes after" input. It does this by appending the value to its own set, using Union. The number returned is also defined as a natural.
	NOTE: The successor function works in python by creating and labeling an element in the universe set called "successor". It then stores the value here until its overwritten by the next use. While python's set union COULD have been used, i prefered the look of lists showing the empty set at $[]$ instead of "frozenset()". Plus it allows you to print the set value and convert by hand to the desired number to prove its working

Predecessor: Takes in any natural number, except for the empty set. Is defined with the use of successor and returns the number that came before the number given. The predecessor of (Successor (n)) returns n.

Add: Takes in two natural numbers and returns a natural number. The add function runs a conditional for the second number, b. If b is 0, is simply returns a. However if not, It will recursively call Add again using Successor of a, and predecessor of b as its input. This continues until b is eventually 0 and returns a. 

Example: Given Add (3, 3), 

- b is not 0 so it runs Add (Successor(3), Predecessor(3)) or Add (4, 2)
- b is not 0 so it runs Add (5, 1)
- b is not zero so it runs Add(6, 0)
- Now that be is zero, it returns a, which is our answer 6.

Multiply: Takes in two natural numbers and returns a natural number. Like the add function it checks if b is 0, and returns 0 if true. If not, it runs the add function taking a, and a recursive multiply function of a and predecessor of b as inputs. 

Example: Given Multiply(3, 2),

- b is not 0, so it runs Add(3, Multiply(3, Predecessor(b))), or Add(3, Multiply(3, 1))
	- Zooming into the inner Multiply Function. Multiply (3, 1) = Add (3, Multiply(3, 0)), since b is not 0 yet.
		- Zooming in once more, We now have Multiply (3, 0), which returns 0
	- The add function can now simplify to Add(3, 0), which returns 3
- Finally, zooming back out to the initial function, Add(3, 3) = 6, giving us our answer.

Helper Functions:

Functions that don't return numbers or aren't definined mathematically.

Is_Equal: 
	Takes in two natural numbers, and returns true if they are equal. Otherwise it returns false. It cant do this by simply checking if the sizes are equal since we haven't DEFINED equal yet. Instead, this simply checks if both a and b are the empty set. If only one of them is the empty set, it returns false. If neither of them are the empty set, it runs the function again with predecessor of a and predecessor of b.
Is_Greater:
	Works similarly to Is_Equal, where it continues to recurse downwards until either a or b becomes 0, returning True if b becomes 0 before a, showing that a is greater. 
Is_Less:
	 A clone of Is_Greater, except it returns true of a becomes 0 before b, proving that b is greater.


labelAppend:
	Labels the number but also puts it in a desired list of numbers provided by the user. Used in the countTo function.

CountTo:
	Given a natural number from $N_{user}$ (The set of labeled numbers), the function will label every number from zero to that natural number. This function assumes you want the numbers to be labled as they are in the real world and uses inflect to convert values to their names.

ListNumbers:
	Simply prints all labels within the universe. Not counting the successor label and the numberlist label.

### Why use Numberlist?
The predecessor and successor function get around using assignment variables directly by using the label method to create a placeholder spot for the successor or predecessor function to use. Because of this, a pure printing of the Universe will list all labeled numbers, numberlist, AND these two labels. Numberlist exists as a way to organize all numbers into a desired list. The user is free to define more lists as needed.

Due to this, its recommended to use labelAppend if you' re explicitly defining numbers.

### Assumptions:
In a mathematical sense, we are assuming ZFC axioms to avoid (Things like sets, unions, set equality etc. exist). We are also allowing functions to exist within sets so the structure can be defined more formally. I'm doing this mostly to avoid getting too philosophical on "What is nothing", and "What is a set".

### Disclaimer:
This builds addition and multiplication from basic set building, and is in NO WAY efficient. Please do not use this in leu of normal operators as this is purposefully very inefficient. Ex: It takes 85 function calls to reach the number 16 due to recursion. (4 for succession up to 4. 81 for the multiplying process)

### Future Plans:
The next update to this would include subtraction. The reason I don't include it here is due to the issue of negatives. Building from the empty sets does not include a method for integers, only naturals. So the next major addition would be expanding this system to work for all integers, allowing for subtraction, and negatives.

