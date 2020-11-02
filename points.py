import random
class Point:
    point_list_x =[]
    point_list_y =[]
    def __init__(self):
        self.x =random.uniform(-1.0,1.0)
        self.y = random.uniform(-1.0,1.0)

        self.liney  = self.func()
        self.bias = 1

        if (self.y>self.liney):
            self.label = 1
        else:
            self.label = -1
    @classmethod        
    def new_point(cls,x,y):
        cls.point_list_x.append(x) 
        cls.point_list_y.append(y)
        




    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def get_label(self):
        return self.label 
    def get_bias(self):
        return self.bias 
    @classmethod    
    def get_list(cls,x):
        if x==1:
            return cls.point_list_x
        else:
            return cls.point_list_y        

    def func(self):
        return 0.3 * self.x + 0.2                              
