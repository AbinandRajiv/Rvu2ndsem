
def is_palindrome(string):
    left, right = 0, len(string) - 1
    while right >= left:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

st=input("Enter a string: ")
st = st.lower()
print(is_palindrome(st))  
