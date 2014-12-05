import urllib, re
from optparse import OptionParser

parser = OptionParser(description = 'Teller ord (rumpe) fra URL')
parser.add_option("-w", "--word", dest="word",
                
                  help="write report to FILE", metavar="WORD")

parser.add_option("-u", "--url",  dest="url",    
                
                  help="URL to scrape", metavar="URL")   

 
(options, args) = parser.parse_args()           
if not options.word: 
    #parser.error('Ord mangler')
    word = 'rumpe'
else:
    word = options.word

if not options.url: 
    parser.error('URL mangler!')
if not options.url.startswith('http'):
    parser.error('URL mangler protokoll! (http:// eller https://)')
    
f = urllib.urlopen(options.url)
response = f.read()

words=re.findall(word, response.lower())
print """url: "%s" """ % options.url
print "ord: %s" % word
print "totalt: %s" % len(words)
