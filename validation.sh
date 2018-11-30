#!/bin/bash

DSID=363769;
channel="vbf_eta700_140_zz_llll_13TeV";
rm splitres.txt orires.txt;
grep "^  9000006" /afs/cern.ch/user/a/akotwal/public/group.phys-gener.MG5_aMCatNLO201.${DSID}.${channel}.TXT.mc15_v1._00001.events >> orires.txt;
for i in `seq 19`;
	#`seq 55`;
do
  if [ $i -lt 10 ]; then 
    n=0$i
  else
    n=$i
  fi
  echo ${n}
  grep "^  9000006" group.phys-gener.MG5_aMCatNLO201.${DSID}.${channel}.TXT.mc15_v1._000${n}.events | wc -l
  grep "^  9000006" group.phys-gener.MG5_aMCatNLO201.${DSID}.${channel}.TXT.mc15_v1._000${n}.events >> splitres.txt

done
