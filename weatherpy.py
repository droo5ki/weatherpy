import sys
import requests

def getCityName(zipcode):
  ''' need to figure out how the '''
  ''' docsting stuff works '''
  
  url = 'http://api.wunderground.com/api/0b0139e2a0f25fb7/geolookup/q/%s.json' % zipcode

  # construct get request
  
  r = requests.get(url)

  return r.json()['location']['city']

if __name__ == '__main__':

    zipcode = sys.argv[1]
    if sys.argv < 1:
        print 'Too few args'
        exit()
    else:
      print getCityName(zipcode)


    
