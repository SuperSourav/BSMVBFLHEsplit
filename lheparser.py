import re

def main():
  print "/afs/cern.ch/user/a/akotwal/public/group.phys-gener.%s.%s.%s.TXT.%s._00001.events"%(generator, DSID, process, mcinfo)
  f = open("/afs/cern.ch/user/a/akotwal/public/group.phys-gener.%s.%s.%s.TXT.%s._00001.events"%(generator, DSID, process, mcinfo), 'r')
  commonblock = []
  l = f.readline()
  commonblock.append(l)
  while (l.strip() != "</init>"):
    #print l
    l = f.readline()
    if (re.search(r"nevents", l)): 
      totevts = int(l.split()[0].strip())
      fileIndex = 2 #(totevts/nsubevt)
      print l
      l = re.sub(r"%s"%str(totevts), str(fileIndex), l)
      print l
    commonblock.append(l)
  
  
  print totevts
  nsubevt = 2 #5500
  
  
  #event block
  countevent = 0
  printflag = False
  eventset = []
  
  lhenumber = 0 #number lhe
  
  while (l.strip() != ""):
    print printflag, "\t", l.strip()
    if (lhenumber == fileIndex):
      break
    if (countevent == nsubevt): 
      lhenumber += 1
      filllhe(commonblock, eventset, lhenumber)
      countevent = 0 #reset
      eventset = [] #reset
  
    if (l.strip() == "<event>"):
      printflag = True
      eventblock = []
    elif (l.strip() == "</event>"): 
      printflag = False
      eventblock.append("</event>\n")
      eventset = eventset+eventblock
      countevent += 1
  
    if (printflag):
      eventblock.append(l)
      print eventblock[-1]
    l = f.readline()
    print ">>", l.strip()


def filllhe(commonblock, eventblock, lhenumber):
  foutnameprefix = "group.phys-gener.%s.%s.%s.TXT.%s"%(generator, DSID, process, mcinfo)
  foutnamesuffix = ".events"
  lhenum = "._0" + str(lhenumber/10000.).split(".")[1]
  foutname = foutnameprefix + lhenum + foutnamesuffix
  fout = open(foutname, "w")
  print foutname, "\t: ", eventblock
  [fout.write(l) for l in commonblock + eventblock]
  fout.write("</LesHouchesEvents>" + "\n")
  fout.close()
  return 0

if __name__ == '__main__':
  generator = "MG5_aMCatNLO201"
  DSID = "363762"
  process = "vbf_eta400_80_zz_llnunu_13TeV"
  mcinfo = "mc15_v1"
  main()

