#Number Spiral Diagonals

# We do this one with maths!
# The top right number in each square is n**2, where n is the side length of the square.
# Going anticlockwise from there, we get n**2 - (n-1), n**2 - 2(n-1), and n**2 - 3(n-1).
# Thus the sum of diagonal corners of a square is 4n**2 - 6(n-1)
# Now we simply have to sum from n=1 to n=1001 (the odd ones, noting that for n=1 there is only one corner)


def print_spiral_diagonals(n):
    corner_sums = [4 * n ** 2 - 6 * (n - 1) for n in range(3, 1002, 2)]

    # Calculate the total sum
    total_sum = 1 + sum(corner_sums)

    # Print the result
    print(total_sum)

if __name__ == '__main__':
    n = 100
    print_spiral_diagonals(n)




