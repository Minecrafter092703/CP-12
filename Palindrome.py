def palindrome():
    return true
palindrome = input("Enter something:")
##Making the input come together as one
palindrome = ''.join(palindrome.split())
palindrome = palindrome.replace(',', '')
palindrome = palindrome.replace("'", "")
palindrome = palindrome.replace('.', '')
palindrome = palindrome.replace('!', '')
rev_palindrome = palindrome[::-1]

##Making the palindrome lowercase
##If input is palindrome it will say
if palindrome.lower() == rev_palindrome.lower():
    print("This is a palindrome")
else:
    print("This is not a palindrome")
