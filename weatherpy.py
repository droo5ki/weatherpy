# -*- coding: utf-8 -*-

import sys
import requests

def getCityName(zipcode):
  ''' need to figure out how the '''
  ''' docsting stuff works '''
  
  url = 'http://api.wunderground.com/api/0b0139e2a0f25fb7/geolookup/q/%s.json' % zipcode
  response = requests.get(url)
  
  return response.json()['location']['city']

def getCurrentTemp(zipcode):
  
    url = 'http://api.wunderground.com/api/0b0139e2a0f25fb7/conditions/q/%s.json' % zipcode
    response = requests.get(url)
    return response.json()['current_observation']['temp_f']

if __name__ == '__main__':
  
  zipcode = sys.argv[1]
  if sys.argv < 1:
     print 'Too few args'
     exit()
  else:
    city = getCityName(zipcode)
    curr_temp_f = getCurrentTemp(zipcode) 
  d = '\xb0'
  print "The current temperature is %s F in %s." % (curr_temp_f,city)
