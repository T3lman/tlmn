#tell if a number is divisible by 1 to 20
def isDivisable(number):
    for i in range(1,21):
        if number %i!=0:
            return False
    return True
number=20
while True:
    if isDivisable(number):
        break
    number +=20 #incrent number
print(number)