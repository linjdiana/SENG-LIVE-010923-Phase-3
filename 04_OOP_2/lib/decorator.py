# 1. ✅ First Class Functions
# "[We can] assign them to variables, store them in data structures, pass them as arguments
# to other functions, and even return them as values from other functions."
# See more => http://bit.ly/3YQh8KR

    # Create functions to be used as callbacks 

def walk(pet):
    print(f'{pet} has been walked!')

def feed(pet):
    print(f'{pet} has been fed!')

    # Create a higher-order function that will take a callback as an argument
# def execute_task(func):

#     # callback function invoked
#     return func("Rose")

# execute_task(walk)

# 2. ✅ Create a higher-order function that returns a function

# def execute_task():
#     def feed(pet):
#         return f'{pet} has been fed'
    
#     return feed

# execute_task()

# execute_task()("Rose") is the same as feed("Rose")

# 3. ✅ Decorator

# Create a function that:
    # - takes a function as an argument
    # - has an inner function defined 
    # - returns the inner function

# Tools:

    # .format()
    # https://www.geeksforgeeks.org/python-string-format-method/

    # .round()
    # https://www.geeksforgeeks.org/round-function-python/

# Decorator 
def coupon_calculator(func):
    # inner function 
    def report_price():
        print('Initial Price = $35.00')
        final_price = func(35.00)
        print(f'Newly Discounted Price = ${final_price}')

    return report_price

# Callback function to calculate new price
def calculate_price(price):
    # we end up with a floating point number rounded to the nearest hundredth
    return '{:.2f}'.format(round(price / 2, 2))


# Try using a decorator with / without pie syntax '@'

# Without pie syntax 

# report_price = coupon_calculator(calculate_price)
# report_price()

# With pie syntax
@coupon_calculator
def calculate_price(price):
    # we end up with a floating point number rounded to the nearest hundredth
    return '{:.2f}'.format(round(price / 2, 2))


calculate_price()