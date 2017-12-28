#TODO : Check Whether the given angle is acture ,obtuse or right angle
n = int(input("Enter the angle"))
if n<=60:
    print('Angle is acute')
elif n == 90:
    print('Angle is Normal')
else:
    print("Angle is obtuse")