import pycurl,json,time
from StringIO import StringIO

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

while True:
  getweather()
  print "wind direction:",wind_dir
  print "wind speed:",wind_spd_kt,"knots"
  print "wind gust:",wind_gust,"knots"
  time.sleep(61)
