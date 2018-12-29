# 28*28 Flip-Dot Display with Arduino and RS485 Use Guide

In this instruction, I will show a way to load a series of images into the 28\*28 Flip-Dot Display XY5 by Alfazeta via Arduino. You can prepare all the 28\*28 images in png formats. We first need to use a python script to translate all the images into a 3-layer hex array, then copy the big array into the Arduino code. Ardunio will allow you to decide how the animation be like with all the frames. You can even add sensors and make the display interactive!

### Install Softwares
1. Download and install [Arduino IDE](https://www.arduino.cc/en/Main/Software)
2. Open Terminal and check python version
  ```
  $ python -V
  ```
  In this tutorial we'll use python 2. By default MacOS comes with python 2.7, if you have python 3 by default when typing in `python -V`, try `python2 -V` instead. Download [python 2.7](https://www.python.org/download/releases/2.7.6/) if you are on Windows.
3. Run `pip install Pillow` in terminal to install Pillow in python, a image processing library. If you don't have pip installed
  ```
  $ curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
  $ sudo python get-pip.py
  ```


set up
pip install Pillow
install arduino









frog shanghai studio installation 9/28/2018
-------------------------------------------

I'm working on an interactive installation for frog shanghai studio. There are two pieces of 28*28 flip-dots board made by alphazeta. The first part of this project is to make an eye that follows you on one board.

I did the illustration and animation of the eye by illustrator and photoshop. In this stage I edited the pixels manually by pencil brush in photoshop. There are two versions of eye blinks, one more realistic and one doesn't simulatate human eye blink.

Hardware and software wise, I'm currently using an arduino uno for testing the effects. Flip-dot board uses RS485 signal. I used a ttl to RS485 converter to send signals to the board from arduino. To get the signals in hex code of the format that the board wants, I'm using python to convert a series of pixelated images into a three dimensional array, which is an array of frames of the animation, in which each frame is an array of four panels of the board, that each panel requires an separate array of hex codes. I save that big 3-d array into a single line string text and copy that directly into the arduino code, as a const. One thing to notice here is that I used PROGMEM to store the array into program storage space insdead of dynamic memory.

To make the eyemovement make more realistically, I used polynomials to simulate the movement speed and eye blink speed. I used a predefined array to code the delays between frames.

Next step is to use three ultrasonic sensors for detecting the position of the audience and make the eye follow. Since the board is 42cm wide and humans are mostly over 55cm wide, by placing two sensors in a distance of 20-30 cm allows us to estimate where the eye turns to out of five positions, etc when only the sensor in the left is triggered, the eye turns to the very left; when only the left and middle sensors are both triggered, the eye turns half to the left.
