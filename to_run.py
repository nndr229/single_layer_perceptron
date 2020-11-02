
from points import Point
from perceptron import Perceptron
import matplotlib.pyplot as plt
import numpy as np
import random

points =[]
brain = Perceptron(3)
training_index = 0
def run():
    global brain
    global points,training_index
    inputs = [-1,0.5,1,1]

    out = brain.guess(inputs)
    list_iter_p1 = []
    list_iter_p2 = []
    check=[]
    for i in range(1000):
        point = Point()
        points.append(point)
        Point.new_point(point.getx(),point.gety())

    x = [point.getx() for  point in points ]
    y = [0.3*x_value + 0.2 for x_value in x  ]


    x_s = [map(x_value, -1, 1, 0, 1) for x_value in x]
    y_s = [map(y_value, -1, 1, 1, 0) for y_value in y]


    plt.ion()
    fig, ax = plt.subplots()
    listx, listy = [],[]

    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.plot(x_s,y_s, color='blue')
    plt.show()


    plt.draw()

    count=0
    for point in points:
        x = point.getx()
        y = point.gety()
        target = point.get_label()


        weights = Perceptron.weights;
        try:
            x1 = -1;
            y1 = brain.guessY(x1)#(-weights[2] - weights[0] * x1) / weights[1];
            x2 = 1;
            y2 =  brain.guessY(x2)#(-weights[2] - weights[0] * x2) / weights[1];

            x1_ = map(x1, -1, 1, 0, 1);
            y1_ = map(y1, -1, 1, 1, 0);
            x2_ = map(x2, -1, 1, 0, 1);
            y2_ = map(y2, -1, 1, 1, 0);
            sc = ax.plot([x1_,x2_], [y1_,y2_], c="red")
            fig.canvas.draw_idle()
            plt.pause(0.0001)
            sc.pop(0).remove()

        except ZeroDivisionError:
            pass

        training_point = points[training_index]
        inputs = [training_point.getx(),training_point.gety(),training_point.get_bias()]
        target = training_point.get_label()

        brain.train(inputs,target)

        count_i = 0
        training_index+=1
        if(training_index ==len(points)):
            training_index =0
        count_i+=1


        guess_value  = brain.guess(inputs)
        if(guess_value==target):
            x_to_append = map(training_point.getx(), -1, 1, 0, 1);
            y_to_append = map(training_point.gety(), -1, 1, 1, 0);
            listx.append(x_to_append)
            listy.append(y_to_append)
            sc =ax.scatter(listx[count],listy[count],c="green")
            fig.canvas.draw_idle()

        elif guess_value != target:
            x_to_append = map(training_point.getx(), -1, 1, 0, 1);
            y_to_append = map(training_point.gety(), -1, 1, 1, 0);

            listx.append(x_to_append)
            listy.append(y_to_append)
            sc =ax.scatter(listx[count],listy[count],c="red")
            fig.canvas.draw_idle()
        count+=1

    plt.show()
    plt.waitforbuttonpress()

def f(x):
    return x*0.3 +0.2
def map(n, start1, stop1, start2, stop2):
     return ((n-start1)/(stop1-start1))*(stop2-start2)+start2

run()
