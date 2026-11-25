# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    """
    Return the indices of two numbers in the nums array that sum to the target.

    nums = [1, 2, 3]   target = 5  Should return [1, 2]

    Nest a loop to go through each index twice, checking if they sum to target and that i < j.
    """
    #   ...
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    for i in range(0, len(nums) - 1):
        if i == len(nums) - 1:
            return []
        for j in range(i + 1, len(nums)):
            i_value = nums[i]
            j_value = nums[j]
            if i_value + j_value == target:
                return [i, j]


def max_profit(prices):
    # Outline:
    """
    Compare values in prices to determine the maximum profit from buying on a low day to selling
    on a later high day.

    prices = [1, 2, 3]  Should return 2

    Track a lowest number and a profit count and loop through prices. 
    If there is no profit return 0.
    """
    #   ...
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    lowest = float('inf')
    profit = 0

    for price in prices:
        if price < lowest:
            lowest = price
        if price - lowest > profit:
            profit = price - lowest

    return profit


def max_subarray(nums):
    # Outline:
    """
    Return the largest in a row sum, or sum of numbers in nums that are back to back(contiguous).

    nums = [-2, 1, 2]  Should return 3.

    Track a result and running count. Loop through nums, adding to running count. If running 
    count > result then result = running count. If not, reset running count.
    """
    #   ...
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    current_sum = nums[0]
    best_sum = nums[0]

    for i in range(1, len(nums)):
        current = nums[i]

        current_sum = max(current, current_sum + current)

        best_sum = max(best_sum, current_sum)

    return best_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    """
    Check if bracket types are closed in order, even if they are nested.

    s = "{asdafsaf()}"  Should return True

    Track the brackets with a stack(LIFO) to match corresponding closing bracket. Loop through
    s and if the char is a bracket, add it to the stack. Pop from the stack if a bracket is closed
    and the correct closing bracket.
    Return True if len(stack) is 0.
    """
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    stack = []
    left_bracket = "{(["
    right_bracket = "])}"
    pairs = {
        "{": "}",
        "(": ")",
        "[": "]",
        }

    for char in s:
        if char in left_bracket:
            stack.append(char)

        if char in right_bracket:
            if len(stack) == 0 or pairs[stack[-1]] != char:
                return False
            stack.pop()

    return len(stack) == 0



def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
