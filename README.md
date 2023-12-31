# Reverse Vending Machine (ReviveMate)

This repository contains the scripts and code for the Reverse Vending Machine project. This is a Data Science project where we used a RaspberryPI , and a Deep Learning model to create a reverse vending machine targeted for the tunisian market, specializing in the classification of plastic bottles and aluminum/metal cans. The users have the chance to receive points/vouchers for the type of object they insert into the vending machine.

####
For more information on how our reverse vending machine works this is a demo video for our prototype :
* https://drive.google.com/file/d/1iYF6ZegnNlID7g1da0yCUDRWzoDHxynM/view?usp=sharing

The "ReviveMate Reverse Vending Machine" does not rely on expensive sensors to detect the type of the object inserted, it uses AI : Deep Learning to classify the object that is detected by a cheap Module2 cameraPi 8mpx .


####
The types of the objects which the deep learning model has been trained on :

* Plastic bottles, ranging from 25cl to 2 liters.
* Aluminum/Metal cans.
* And also the brand of each item 

####


## RasperryPI Setup :
A Raspberry PI 4  running on Rasipan OS has been used for this project. The main code that has been used for taking the picture can be found in the topLevelRecyclingWindow.py__ file.

Here's how we setup the card and the components :
![Pi Connections](https://i.imgur.com/8yZzEPn.jpg)
