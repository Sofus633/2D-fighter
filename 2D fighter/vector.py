


class Vector2:
    def __init__(self, x, y):
        
        self.vector = [x, y]

            
    def  __getitem__(self, i : int):
        return self.vector[i]
    
    def __setitem__(self, i, other):
        self.vector[i] = other
    
    def __list__(self):
        return self.vector
    
    def __str__(self):
        return f"x{self.vector[0]},  y{self.vector[1]}"
    
    def __add__(self, other):
        if type(other) == list or type(other) == tuple:
            return Vector2(self.vector[0] + other[0] , self.vector[1] + other[1])
        if type(other) == Vector2:
            return Vector2(self.vector[0] + other[0] , self.vector[1] + other[1])
        return None
    
    
    def __sub__(self, other):
        if type(other) == list  or type(other) == tuple:
            return  Vector2(self.vector[0] -other[0] , self.vector[1] - other[1])
        if type(other) == Vector2:
            return Vector2(self.vector[0] - other[0] , self.vector[1] - other[1])
        return None