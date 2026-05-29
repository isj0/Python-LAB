#!/usr/bin/env python3

class Robot:
    def __init__(self):
        print("Started Robot")
    def move_forward(self, distance):
        print(f"Robot moving forward: {str(distance)}")
    def move_backward(self, distance):
        print(f"Robot moving backward: {str(distance)}")
    def move_left(self, distance):
        print(f"Robot moving left: {str(distance)}")
    def move_right(self, distance):
        print(f"Robot moving right: {str(distance)}")
    def __dl__(self):
        print("Robot Stopped")

def main():
    obj = Robot()
    obj.move_forward(5)
    obj.move_backward(2)
    obj.move_left(1)
    obj.move_right(3)

if __name__ == "__main__":
    main()