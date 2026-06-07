try:
    num1, num2 = eval(input("enter two numbers, separated buy a comma"))
    result = num1/num2
    print("result is", result)

except ZeroDivisionError:
    print("Division by  zero is error ")

except SyntaxError:
    print("comma is missing .Enter number devided by comma 1,2")

except:
    print("wrong input")

else:
    print("no exceptions ")

finally:
    print("this will exceute no matter what")
    
except:
    print("no exceptions ")