#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand

        if type(size) != int:
              print("size must be an integer")
        else:
             self.size = size

    def get_size(self):
        return self._size
    
    def set_size(self, new_size):
        if type(new_size) == int:
            self._size = new_size
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")


    size = property(get_size, set_size)