# def split_digit(num):
#     user_digit=[]
#     user_digit.append(num/100)
#     user_digit.append((num/10)%10)
#     user_digit.append(num%10)
#     return user_digit
def split_digit(num):
    res = [int(x) for x in str(num)]
    print(res)
    return res
def check_digit(a,b):
    if a==b:
        print("You Found The Right Match")
        print("Congratualtion you have Break the Code")
        exit()
    elif ((a[0] in b) or (a[1] in b) or (a[2] in b)):
        print("Almost")
    else:
        print("No Value Match Found")

print("Welcome Code Breaker! Let's See If You Can Guess My 3 Digit Number ! ")
print("code has been generated please guess a 3 digit number")
actual_digit=[2,8,5]
game=True
while game:
    user_input=input("Enter your guess here: ")
    if not 99<user_input<1000:
        print("Value is less than or greater than three digit")
        continue
    after_split=split_digit(user_input)
    check_digit(after_split,actual_digit)
