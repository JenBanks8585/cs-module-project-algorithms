import random
import time
from itertools import combinations
"""
class Items:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.efficiency = 0

    def __str__(self):
        return f'{self.name}, {self.weight} lbs, ${self.value}'


def naive_fill_knapsack(sack, items):
    '''
    Put highest value items in knapsack until full
    (other basic, naive approaches exist)
    '''
    # sort items
    items.sort(key = lambda x: x.value, reverse = True)

    # put most value items until full
    weight = 0
    for item in items:
        weight += item.weight
        if weight > 50:
            return sack
        else:
            sack.append(item)
    return sack


def brute_force_fill_knapsack(sack, items):
    '''
    Try every combination to find the best combination
    '''
    # generate all possible combinations of items
    combos = []
    #calculate the value of all combinations
    #combos = list(combinations(items))
    
    for i in range(1, len(items)+ 1):
        list_of_combos = list(combinations(items, i))
        for combo in list_of_combos:
            combos.append(list(combo))

    best_value = -1
    # for each combo add up all the weight and value if the items and save the best one
    for combo in combos:
        value = 0
        weight = 0
        for item in combo:
            value +=item.value
            weight +=item.weight
        
        if weight <=50 and value > best_value:
            best_value = value
            sack = combo

    return sack


def greedy_fill_knapsack(sack, items):
    #Calculate efficiency
    for item in items:
        item.efficiency = item.value/item.weight
    # Sort items
    items.sort(key = lambda x: x.efficiency, reverse = True)
    # put items in knapsack till full
    weight = 0
    for item in items:
        weight +=item.weight
        if weight > 50:
            return sack
        else:
            sack.append(item)
    return sack





small_cave = []
medium_cave = []
large_cave = []

def fill_cave_with_items():
    '''
    Randomly generate Item objects and creates
    caves of different sizes for testing
    '''

    names = ["painting", "jewel", "coin", "statue", "Treasue chest", 
                "gold", "silver", "sword", 'goblet', 'hat']
    
    for _ in range(5):
        n = names[random.randint(0,4)]
        w = random.randint(1,25)
        v = random.randint(1,100)
        small_cave.append(Items(n, w, v))

    for _ in range(15):
        n = names[random.randint(0,4)]
        w = random.randint(1,25)
        v = random.randint(1,100)
        medium_cave.append(Items(n, w, v))

    for _ in range(25):
        n = names[random.randint(0,4)]
        w = random.randint(1,25)
        v = random.randint(1,100)
        large_cave.append(Items(n, w, v))

def print_results(items, knapsack):
    '''
    Print out contents of what the algorithm
    calculated should be added to the knapsack
    '''

    print("n\Best items to put in the knapsack: ")
    for item in knapsack:
        print(f'-{item}')

    print(f'n\Result calculated in {time.time() - start:.5f} second \n')

    print('n\_______________________________________________')


fill_cave_with_items()
knapsack = []

# Test1 - Naive
print('Starting test 1, naive approach...')

items = small_cave
start= time.time() 
knapsack = naive_fill_knapsack(knapsack, items)
print_results(items, knapsack)

# Test2 - Brute Force
print('Starting test 2,  brute force....')

items = small_cave
start = time.time()
knapsack = brute_force_fill_knapsack(knapsack, items)
print_results(items, knapsack)


# Test3 - Greedy
print('Starting test 3,  greedy force....')

items = medium_cave
start = time.time()
knapsack = greedy_fill_knapsack(knapsack, items)
print_results(items, knapsack)
"""
# fibonacci

def fibonacci(n):
    #base case
    if (n == 0):
        return n
    if (n == 1):
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

start = time.time()
print(f'{fibonacci(315)}')
print(f'\nResult calculated in {time.time() - start:.5f} seconds')
print(f'\n_______________________________')


# with cache
#cache = {}
#def mem_fibonacci(n):
#    if (n==0):
#        cache[0]=0
#        return 0
#    if (n==1):
#        cache[1]=1
#        return 1
#
#    if n in cache:
#        return cache[n]
#
#    res_n_1 = mem_fibonacci(n-1)
#    res_n_2= mem_fibonacci(n-2)
#    res_at_n = res_n_1 + res_n_2
#
#    cache[n] = res_at_n
#
#    return res_at_n
#
#start = time.time()
#print(f'{mem_fibonacci(315)}')
#print(f'\nResult calculated in {time.time() - start:.5f} seconds')
#print(f'\n_______________________________')
