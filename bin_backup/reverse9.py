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
