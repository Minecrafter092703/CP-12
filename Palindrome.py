def palindrome():
    return true
palindrome = input("Enter something:")
palindrome = ''.join(palindrome.split())
palindrome = palindrome.replace(',', '')
palindrome = palindrome.replace("'", "")
palindrome = palindrome.replace('.', '')
palindrome = palindrome.replace('!', '')
rev_palindrome = palindrome[::-1]

if palindrome.lower() == rev_palindrome.lower():
    print("This is a palindrome")
else:
    print("This is not a palindrome")
