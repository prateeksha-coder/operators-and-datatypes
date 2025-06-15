name="Parteeksha"
age=32
num=16.07
value=True
print("Before Typecasting: ")
print(name,type(name))
print(age,type(age))
print(num,type(num))
print(value,type(value))
print("After Typecasting: ")
age1=float(age)
print(age1,type(age1))
num_1=int(num)
print(num_1,type(num_1))
value1=str(value)
print(value1,type(value1))


num1 = 45
num2 = 3

print("Number 1", num1)
print("Number 2", num2)
print("Addition :", num1+num2)
print("Difference :", num1-num2)
print("Product :", num1*num2)
print("Division :", num1/num2)
print("Floor Division :", num1//num2)
print("Modulus Operation :", num1%num2)
print("Square :", num2**2)
print("Square Root :", num1**0.5)

print("Equal ?", num1==num2)
print("Number 1 greater?", num1>num2)
print("Number 2 greater?", num1<num2)
print("Not Equal ?", num1!=num2)

result = num1/2+num2**2+10
print("Result of given equation is:", result)


first_name = "Codingal"
last_name = "Educations"
full_name = first_name+last_name
example = "Haa"*5

print("First Name :", first_name)
print("Last Name :", last_name)
print("Full Name :", full_name)
print("String Multiplied 5 times gives this result :", example)

word = 'Coding'
print("Length of String :", len(word))
print("First Letter of String :", word[0])
print("Last Letter of String :", word[5])
print("String Sliced :", word[0:3])

# Take input values from user
x = input("Enter Value of x:")
y = input("Enter Value of y:")

# Swapping
temp = x
x = y
y = temp

# Displaying results after swapping
print("value of x after swapping", x)
print("value of y after swapping", y)
