import pycurl,json,socket,fcntl,struct,os
from StringIO import StringIO
from PIL import ImageFont,Image,ImageDraw #pip install Pillow
myip="0.1.2.3"

def getweather():
  global wind_gust
  global wind_dir
  global wind_spd_kt
  buffer = StringIO()
  c = pycurl.Curl()
  c.setopt(c.URL, 'http://www.bom.gov.au/fwo/IDV60901/IDV60901.95872.json')
  c.setopt(c.WRITEDATA, buffer)
  c.perform()
  c.close()
  body = buffer.getvalue()
  heat = json.loads(body)
  wind_gust = str(heat['observations']['data'][0]['gust_kt'])
  wind_dir = str(heat['observations']['data'][0]['wind_dir']);
  wind_spd_kt = str(heat['observations']['data'][0]['wind_spd_kt'])
  return

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15])
    )[20:24])

def writeppm():
  text = (("     wind direction:"+wind_dir, (255, 100, 0)), ("     wind speed:"+wind_spd_kt,(100,0,255)), ("     wind gust:"+wind_gust,(255,0,50)),("     ip:"+myip, (0, 0, 100)))
  font =  ImageFont.truetype("./FreeMonoBold.ttf", 16)
  all_text = ""
  for text_color_pair in text:
      t = text_color_pair[0]
      all_text = all_text + t
  width, ignore = font.getsize(all_text)

  im = Image.new("RGB", (width + 32, 16), "black")
  draw = ImageDraw.Draw(im)
  x = 0;
  for text_color_pair in text:
      t = text_color_pair[0]
      c = text_color_pair[1]
      draw.text((x, 0), t, c, font=font)
      x = x + font.getsize(t)[0]
  im.save("displaythis.ppm")
  return

#myip = str(get_ip_address('eth0'))
#print myip

getweather()
print "wind direction:",wind_dir
print "wind speed:",wind_spd_kt,"knots"
print "wind gust:",wind_gust,"knots"

writeppm()

#os.system("sudo /home/pi/rpi-rgb-led-matrix-master/led-matrix test.ppm -r16 -p8 -D1 -d")
