def chocolate_maker(small, big, x):

#    small = int(input("Please enter small num: "))*1
 #   big = int ( input ( "Please enter big num: " ) )*5
  #  x = int ( input ( "Please enter x size: " ) )

    if small >= x or big >= x:
        return True
    elif small+big >= x:
        return True
    else:
        return False

print(chocolate_maker(3,2,10))