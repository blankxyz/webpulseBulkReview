#!/usr/bin/python
# Blue Coat Webpulse bulk review script
#

import urllib2
import sys
import re

HTML = re.compile(r'<[^>]+>')
QUOTE = re.compile(r'"')

def removeHtml(text):
  return HTML.sub('', text)

def removeQuotes(text):
  return QUOTE.sub('', text)

def main():

  if len(sys.argv) != 2:
    print "USAGE:", sys.argv[0], " <filename>"
    sys.exit()

  with open(sys.argv[1]) as file:
    for line in file:
      request = urllib2.Request(url='http://sitereview.bluecoat.com/rest/categorization',
                            data='url='+line)
      response = urllib2.urlopen(request)
      responseData = response.read()
      responseData = responseData[1:-1]
      responseData = removeHtml(responseData)
      responseData = removeQuotes(responseData)
      responseData = re.split(',', responseData)
      print responseData[0], responseData[-2]

if __name__ == '__main__':
  main()
