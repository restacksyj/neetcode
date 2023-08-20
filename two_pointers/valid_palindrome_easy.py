# Very naive solution

# input = "aba"
input = ".,"


def isPalindrome():
    output = ""
    for c in input:
        if c.isalnum():
            output += c.lower()
    return input == output[::-1]


# print(isPalindrome())


# Tww pointer solutions
def isPalindromeTwo():
    print("writing two pointer solution to this")
    l, r = 0, len(input) - 1
    while l < r:
        while l < r and not alphaNum(input[l]):
            l += 1
        while r > l and not alphaNum(input[r]):
            r -= 1

        print(l, r)
        if input[l].lower() != input[r].lower():
            return False
        l = l + 1
        r = r - 1

    return True
    # Before this, we need a helper function to determine alphanumeric char


# ord is how you get the unicode point
def alphaNum(c):
    return (
        (ord("A") <= ord(c) <= ord("Z"))
        or (ord("a") <= ord(c) <= ord("z"))
        or (ord("0") <= ord(c) <= ord("9"))
    )


print(isPalindromeTwo())
