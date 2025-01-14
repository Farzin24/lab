def reverse_num():
   num=input("enter 4 digit:")
   if len(num)>=4 and num.isdigit():
       rev=""
       for digit in num:
           rev=digit+rev
       print(f"original{num}, reversed{rev}")
   else:
       print("invalid")
reverse_num()


def read_num():
    while True:
        num=int(input("enter numbers:"))
        if 1000<=num<=9999:
            return num
        else:
            print("invalid")
def reverse(num):
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev
number=read_num()
reversed=reverse(number)
print(number)
print(reversed)