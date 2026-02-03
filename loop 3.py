s = input("Enter string:")
alphabets = 0
digits = 0


for ch in s:
    if('A'<= ch <= 'Z') or ('a' <= ch <= 'z'):
        alphabets += 1
    elif'0'<= ch <='9':
        digits+=1
            
print("Alphabets:",alphabets)
print("Digits:",digits)
