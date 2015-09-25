import pycurl,json
from StringIO import StringIO

buffer = StringIO()
c = pycurl.Curl()
#get melbourne weather observations
c.setopt(c.URL, 'http://www.bom.gov.au/fwo/IDV60901/IDV60901.95936.json')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
body = buffer.getvalue()


heat = json.loads(body)

current_air_temp = heat['observations']['data'][0]['air_temp']



print "current air temperature is",str(current_air_temp)












