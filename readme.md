Weather on the Raspberry Pi
===================

This LED Matrix that can render just about anything.  Messages from your friends, or in this example the weather. 

Step 1: Buy some IoT Stuff
-------------

Support adafruit.com as they provide a very nice library with some included demos for drawing on the LED Matrix.
```
Rasberry Pi 2 - Model B
RGB Matrix + Real Time Clock HAT
LED Matrix 16x32 (or bigger if you prefer)
Hub75 Cable
5V Power Supply
Micro SD (Blank)
Micro USB Cable
Balsa Wood (Optional)

```

Step 2: Assembly
--------------

Download the OS: [here](https://www.raspberrypi.org/downloads/)


Burn it to the SD card (Wait 45 minutes):
```
dd bs=1m if=2015-05-05-raspbian-wheezy.img of=/dev/diskn
```
Solder the HAT board as per the instructions [here](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/assembly)

Start the Pi, and get the matrix library:
```
sudo apt-get update
sudo apt-get install python-dev python-imaging
wget https://github.com/adafruit/rpi-rgb-led-matrix/archive/master.zip
unzip master.zip
cd rpi-rgb-led-matrix-master/
make
```
Optionally add a welcome script that displays the IP address if you want to skip the screen/keyboard in future.




Step 3: Test
-------------
One of the included demos that scrolls text along the LED.
```
 sudo ./led-matrix -r 16 -D 1 runtext16.ppm
```



Another included demo, which displays time.  Note the while loop is needed to constantly refresh.
```
(while :; do date +%T ; sleep 0.2 ; done) | sudo ./text-example -f fonts/8x13B.bdf -y8 -c2 -C0,0,255
```


The other python examples show how you can take any text and render it to a Portable Pixel Map (ppm) file for display on the LED Matrix.


![Sample](https://github.com/craiggunson/weather-pi/blob/master/sample.jpg)
