speed = int(input("Enter speed: "))
average_speed = int(input("Average speed: "))

points = (speed - average_speed)/5

if speed < 60:
    print("Ok")
elif speed == 60:
    print("Ok")

if points > 12:
    print("Demerit: " + str(points))
else:
    print("Time to go to jail!")
