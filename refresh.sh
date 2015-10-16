# for cron
cd /home/pi/rpi-rgb-led-matrix-master
sudo killall led-matrix
/usr/bin/python /home/pi/rpi-rgb-led-matrix-master/weather-pi.py &&
exit 0


