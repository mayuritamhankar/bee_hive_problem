import random
from random import uniform
import numpy as np
import matplotlib.pylab as plt

class swarm(object):
    def __init__(self):
        # self.size = random.randint(10, 5000)
        # self.center_x = round(random.uniform(-100, 100), 2)
        # self.center_y = round(random.uniform(-100, 100), 2)
        # self.radius = random.randint(0, 100)
        self.size = 500
        self.center_x = 2
        self.center_y = 2
        self.radius = 10
        print(self.size)
        print(self.center_x)
        print(self.center_y)
        print(self.radius)
        # self.swarm_of_bees = [bee() for i in range(self.size)]
        # print(self.swarm_of_bees)
        # bee1=bee()


class bee(swarm):
    # print(swarm.size)
    # print(swarm.center_x)
    # print(swarm.center_y)
    # print(swarm.radius)
    # center_x =swarm.center_x
    # center_y = swarm.center_y
    # radius = swarm.radius
    def __init__(self):
        swarm.__init__( self )
        self.x_coordinate, self.y_coordinate = self.position(swarm)
        self.life = round(random.uniform(2.5,365.5), 2)

    def queen_bee(self):
        self.queen = True

    def position(self,swarm):
        circle = False
        while circle == False:
            r = np.array(
                [uniform(self.center_x - self.radius, self.center_x + self.radius),
                 uniform(self.center_y - self.radius, self.center_y + self.radius)])
            # we will regenerate random numbers untill the coordinates
            # are within the ring x^2+y^2 < 3,5^2 and x^2+y^2 > 2^2
            if ((r[0] - self.center_x) ** 2 + (r[1] - self.center_y) ** 2 <= self.radius ** 2):
                circle = True
            else:
                circle = False
        return r[0], r[1]



# x = np.zeros(500)
# y = np.zeros(500)
# for i in range(500):
#     x[i],y[i] = position()
b = [bee() for i in range(3)]
for be in b:
    plt.scatter(be.x_coordinate,be.y_coordinate)
# hive = [swarm() for i in range(3)]
# for hive in hive:
#     for bee in hive.swarm_of_bees:
#         plt.scatter(bee.x_coordinate,bee.y_coordinate)
plt.scatter(b[0].center_x,b[0].center_y)
plt.show()
# b = bee()
# print(b.x_coordinate)