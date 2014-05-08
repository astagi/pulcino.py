#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pulcino.py: generate a "Pulcino Pio" style (??) song!
# Author: Andrea Stagi on vacation <stagi.andrea@gmail.com>

import argparse

#Our type Animal
class Animal:

    def __init__(self, name, sound, art_d, art_i):
        self.name = name
        self.sound = sound
        self.art_d = art_d
        self.art_i = art_i

def animal_file_parser(file):
    f = open(file, 'r')
    animals = []
    for line in f:
        animal_attrs = line.rstrip().split(' ')
        articles = animal_attrs[0].split('/')
        animals.append(Animal(animal_attrs[1], animal_attrs[2], articles[0], articles[1]))
    return animals

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='animal file')
attrs = parser.parse_args()

#Set all the animals you want with our hero on the first position!
animals = animal_file_parser(attrs.file)

#Let's start singing
current = 1
anche = ""
n_animals = len( animals )

#The title
print "\n%s %s %s\n" % ( animals[0].art_d.capitalize(), animals[0].name, animals[0].sound )

for i in range( n_animals ):

    print ""

    #Who is new on the radio?? Let's see..
    for j in range( 2 ):
        if current != 1:
            anche = " anche"
        print "In radio c'é%s %s %s" % ( anche, animals[i].art_i, animals[i].name )

    #Uhm I don't remember who's actually on the radio, damn!
    for k in reversed(range( current )):
        print "e %s %s %s" % (animals[k].art_d, animals[k].name, animals[k].sound )

    #Pulcino Pio, it's your moment!!
    pulcino_sound_range = (3 - (( current + 1 ) % 2))

    for j in range( pulcino_sound_range ):
        if i == (n_animals - 1) and j == pulcino_sound_range - 1:
            animals[0].sound = "oh oh!"
        print "e %s %s %s" % (animals[0].art_d, animals[0].name, animals[0].sound )

    current += 1

    print ""