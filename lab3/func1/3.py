def solve(numheads, numlegs):
    for y in range(numheads + 1): # y is a number ofchickens 
        x = numheads - y # x is a number of rabbits
        if 2 * x + 4 * y == numlegs:
            print(x, y)
            return (x, y)
    return None

solve(35, 94)