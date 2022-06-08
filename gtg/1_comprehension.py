#As a concrete example, a list of the squares of the numbers from 1 to n, that is
#[1,4,9,16,25,... ,n2], can be created by traditional means as follows:
n = input('n?: ' )
squares = [ ]
for k in range(1, n+1):
    squares.append(k*k)
#With list comprehension, this logic is expressed as follows:
squares = [k*k for k in range(1, n+1)]