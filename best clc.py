# the libraries
# the inputs
important = "in symople please "
name = input("please sur enter your name : ")
print("welcome " + name)
num1 = float(input("please "+ name +" enter the frist nunber you want "))
the_process = input("please enter the process you want " + important )
num2 = float(input(" please enter the secound number you want "))

#the process
sum = "+"
sub = "-"
mul = "*"
div = "/"

if the_process == sum :
    
    print(num1 + num2)

elif the_process == sub:
    
    print(num1 - num2)

elif the_process == mul :
    
    print(num1 * num2)

elif the_process == div :
    
    print(num1 / num2)

# the end
else :
    
    print("sorry "+ name + " plase try again")