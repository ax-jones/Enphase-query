
import httplib
import json
import StringIO

def getsolarval():
  h1 = httplib.HTTPConnection("10.1.19.58")
  h1.request("GET", "/production?locale.en")
  r1 = h1.getresponse()
  dat = r1.read()
  #print dat
  for line in StringIO.StringIO(dat):
    if "Currently" in line:
      sres = line[37:].split("W")[0]
      if "," in sres:
		sres = sres.replace(',', '')
      if "k" in sres:
		sres = sres.split("k")[0]
		fres = float(sres)
      else:
		fres = float(sres) / 1000.0
      return fres


def main():
  print getsolarval()

if __name__ == "__main__":
  main()
