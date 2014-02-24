import sys
import requests

def getResponseFromWunderground(zipcode):
  ''' need to figure out how the '''
  ''' docsting stuff works '''
  
  url = 'http://api.wunderground.com/api/0b0139e2a0f25fb7/geolookup/q/%s.json' % zipcode

  # construct get request
  
  return requests.get(url)

def getCityName(response):
 
  return response.json()['location']['city']

def getCurrentTemperature(response):
  print response.json()
  print 
  print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  return "Current temperature is %s" % response.json()['current_observation']['temp_f']

if __name__ == '__main__':
  
  zipcode = sys.argv[1]
  if sys.argv < 1:
     print 'Too few args'
     exit()
  else:
    response = getResponseFromWunderground(zipcode)
    print getCityName(response)
    print getCurrentTemperature(response)
    
