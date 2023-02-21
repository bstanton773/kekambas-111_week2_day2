# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.  The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 10, the function should return 90.

# Example Inputs: full_price = 100, discount = 10
# Example Output: 90

def solution(price, discount):
    # write your code here
    percentage = discount / 100
    dollars_off = price * percentage
    return price - dollars_off

print(solution(100,10))
