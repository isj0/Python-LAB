#!/usr/bin/env python3

print ("Hello, Robot")
print("---------------\n")

def forward():
    print("Robot is moving forward")

def back():
    print("Robot is moving backwards")

def left():
    print("Robot is moving left")

def right():
    print("Robot is moving right")

def main():

    robot_command = input("Enter the command:> ")

    if (robot_command == "left"):
        left()
    elif (robot_command == "right"):
        right()
    elif (robot_command == "forward"):
        forward()
    elif (robot_command == "back"):
        back()
    else:
        print("Invalid Command")

    robot_x = 0.1
    robot_y = 0.1

    # while (robot_x < 2 and robot_y < 2):
    #     robot_x += 0.5
    #     robot_y += 0.5

    #     print(f"Current position ({robot_x:.2f}, {robot_y:.2f})")

    # print("Robot has Reached Destination")

    # for _ in range(100):

    #     robot_x += 0.1
    #     robot_y += 0.1

    #     print(f"Current position ({robot_x:.2f}, {robot_y:.2f})")

    #     if (robot_x > 2 and robot_y > 2):
    #         print("Robot has Reached Destination")
    #         break

if __name__ == "__main__":
    main()