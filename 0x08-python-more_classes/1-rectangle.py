#!/usr/bin/python3
"""This defines a class """

class Rectangle():
    def __init__(self, width=0, height=0):
        """The initializer of the class triangle that runs 
        immediately the class is created

        Args:
        width (int) description of the width of the rectangle
        height (int): the height of the triangle
        
        """
        self.__width = width
        self.__height = height

    def width(self):
        """retrieves the value of instance width"""
        return self.__width
    def height(self):
        """retrieves tbe value of instance height"""
        return self.__height

    def width(self, value):
        """sets the value of width
        
        Args:
        value (int): the value of instance width
        """
        self.__value = (value)
        if not isinstance(width, int):
            raise TypeError("width must be an integer") 
        if self.__value < 0:
            raise ValueError("width must be >= 0")
    
    def height(self, value):
        """Sets the value of height
        Args:
            value (int): the value off instance height """
        self.__value = value
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if self.__value < 0:
                raise ValueError("height must be >= 0") 


