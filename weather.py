import pycurl,json
from StringIO import StringIO

buffer = StringIO()
c = pycurl.Curl()
#get melbourne weather observations
c.setopt(c.URL, 'http://www.bom.gov.au/fwo/IDV60901/IDV60901.95872.json')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
body = buffer.getvalue()


heat = json.loads(body)

wind_gust = str(heat['observations']['data'][0]['gust_kt'])
wind_dir = str(heat['observations']['data'][0]['wind_dir'])
wind_spd_kt = str(heat['observations']['data'][0]['wind_spd_kt'])

print "wind direction:",wind_dir
print "wind speed:",wind_spd_kt,"knots"
print "wind gust:",wind_gust,"knots"











