### Requirements:       

# # - Implement Euclid's algorithm yourself. Do not call `math.gcd`.      
# # - `gcd(a, 0) == abs(a)` and `gcd(0, 0) == 0`.     
# #- Negative inputs are allowed and the result is never negative.        
# 3- Optional: in a `if __name__ == "__main__":` block, read two numbers with `input()` and print the result.     

# ```python       
# >>> gcd(48, 18)     
# 6       
# >>> gcd(-12, 18)        
# 6       
# >>> gcd(7, 0)       
# 7       
# ```     

# C++ starting point:     

# ```cpp      
# int gcd(int a, int b) {     
#     while (b != 0) {        
#         int t = a % b;      
#         a = b;      
#         b = t;      
#     }       
#     return a;       
# }       
# ```     

user_input = input("Please input 2 integers: ")
integers = [int(x) for x in user_input.split(" ")]
if len(integers) >= 3: 
    print("You should only input 2 integers only!")
    raise ValueError

"""
Difference from C++:
Unlike C++, Python allow for multiple value assignment using the "," signs. 
Moreover, Python does not allow the user the index the nested arguments.
Also, Python does not need the programmer to initialize the type of variables
And also, it does not require you to append a ";" at the end!
"""
    
def gcd(a: int, b: int): 
    while b != 0:
        a, b = b, a%b
    return a

if __name__ == "__main__":
    print("The GCD of", integers[0], "and", integers[1], "is:", gcd(integers[0], integers[1]))