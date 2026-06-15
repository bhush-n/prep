def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
s = "NITIN"
p = palindrome(s)
print(p)