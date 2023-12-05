def shortest_palindrome(s):
    n = len(s)

    i = n
    while i > 0:
        if s[:i] == s[:i][::-1]:
            break
        i -= 1

    return s[i:][::-1] + s

s = "aacecaaa"
output = shortest_palindrome(s)
print(output)