class Robot:
    def __init__(self):
        self.position=(0, 0)
       

    def move(self, directions):
        for direction in directions:
            if direction == "U":
                self.position = (self.position[0], self.position[1] + 1)
            elif direction == "D":
                self.position = (self.position[0], self.position[1] - 1)
            elif direction == "L":
                self.position = (self.position[0]- 1, self.position[1])
            elif direction == "R":
                self.position = (self.position[0]+ 1, self.position[1])
            else:
                 print("Invalid direction")    

        return self.position
            
robot=Robot()
print(robot.move("UURDDL"))
        



       
    