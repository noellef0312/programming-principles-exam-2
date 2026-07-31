# Program Name: Exam2.py
# Course: IT1114
# Student Name: Noelle Finney
# Assignment Number: Exam 2
# Due Date: March 29, 2026
# Purpose: This program calculates the total volume of a water tower.
# Resources: Notes from class & general understanding of python

import math  # gives access to pi

# calculate the volume of a full sphere
def calc_sphere(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

# calculate the volume of a cylinder
def calc_cylinder(radius, height):
    volume = math.pi * radius**2 * height
    return volume


# then the program will ask user for measurements
sphere_radius = float(input("What is the radius for the sphere portion: "))
cylinder_radius = float(input("What is the radius for the cylinder portion: "))
cylinder_height = float(input("What is the height for the cylinder portion: "))

# only of the half the sphere is used in the tower)
top_part = calc_sphere(sphere_radius) / 2

# full cylinder part
bottom_part = calc_cylinder(cylinder_radius, cylinder_height)

# total volume of the tower
tower_volume = top_part + bottom_part

# the final result
print("Volume:", tower_volume)
