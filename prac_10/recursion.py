"""
CP1404/CP5632 Practical
Recursion
"""


#
# def do_it(n):
#     """Do... it."""
#     if n <= 0:
#         return 0
#     return n % 2 + do_it(n - 1)
#
#
# # basically it counts all odd numbers using accumulation of modulus remainders
# print(do_it(5))
#
#
# def do_something(n):
#     """Print the squares of positive numbers from n down to 0."""
#     if n < 0:
#         return
#     else:
#         print(n ** 2)
#         do_something(n - 1)
#
#
# do_something(4)
#
#
# def do_something2(n):
#     """Print the squares of positive numbers from 0 down to n."""
#     if n < 0:
#         return
#     else:
#         do_something2(n - 1)
#         print(n ** 2)
#
#
# do_something2(4)
#

def blocks_in_pyramid(rows=0):
    if rows < 0:
        return 0
    return rows + blocks_in_pyramid(rows - 1)


print(blocks_in_pyramid(5))


