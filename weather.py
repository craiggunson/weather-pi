import urllib2,json,time


def getweather():
  global wind_gust
  global wind_dir
  global wind_spd_kt
  response = urllib2.urlopen('http://www.bom.gov.au/fwo/IDV60901/IDV60901.95872.json')
  body = response.read()
  data = json.loads(body)
  wind_gust = str(data['observations']['data'][0]['gust_kt'])
  wind_dir = str(data['observations']['data'][0]['wind_dir']);
  wind_spd_kt = str(data['observations']['data'][0]['wind_spd_kt'])
  return

def getairtemp():
  global airtemp
  response = urllib2.urlopen('http://www.bom.gov.au/fwo/IDV60901/IDV60901.94866.json')
  body = response.read()
  data = json.loads(body)
  airtemp = str(data['observations']['data'][0]['air_temp'])
  return

while True:
  getweather()
  getairtemp()
  print "wind direction:",wind_dir
  print "wind speed:",wind_spd_kt,"knots"
  print "wind gust:",wind_gust,"knots"
  print "air temp:",airtemp,"C"
  time.sleep(61)
