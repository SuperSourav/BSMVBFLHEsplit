#!/bin/bash

rm splitres.txt orires.txt;
grep "^  9000006" /afs/cern.ch/user/a/akotwal/public/group.phys-gener.MG5_aMCatNLO201.363762.vbf_eta400_80_zz_llnunu_13TeV.TXT.mc15_v1._00001.events >> orires.txt;
for i in `seq 55`;
do
  if [ $i -lt 10 ]; then 
    n=0$i
  else
    n=$i
  fi
  echo ${n}
  grep "^  9000006" group.phys-gener.MG5_aMCatNLO201.363762.vbf_eta400_80_zz_llnunu_13TeV.TXT.mc15_v1._000${n}.events | wc -l
  grep "^  9000006" group.phys-gener.MG5_aMCatNLO201.363762.vbf_eta400_80_zz_llnunu_13TeV.TXT.mc15_v1._000${n}.events >> splitres.txt

done
