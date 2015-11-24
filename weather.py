import urllib2,json,time

def getweather():
  global wind_gust
  global wind_dir
  global wind_spd_kt
  response = urllib2.urlopen('http://www.bom.gov.au/fwo/IDV60901/IDV60901.95872.json')
  body = response.read()
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
