#!/bin/bash

BASEDIR=`pwd`
for i in 01 02 03 04 05 06 07 08  09 10 11 12 13 14 15 16 17 18 19 20 
  do
   mkdir -p $i
   cd $i

    for j in 02  03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 
     do
      if [ $i -lt $j ]
       then
       mkdir -p $j
        cd $j
       
        for k in 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20
         do
          if [ $j -lt $k ]
           then 
             mkdir -p $k 
             cd $k
             cat $BASEDIR/mono_$i.xyz $BASEDIR/mono_$j.xyz $BASEDIR/mono_$k.xyz $BASEDIR/meth.xyz > tetra.xyz
             cat $BASEDIR/head tetra.xyz $BASEDIR/tail > run4b.inp
             cd ../
           fi
         done
         cp ../../one_j_script.sh .
         #sbatch -H one_j_script.sh
         sbatch  one_j_script.sh
        cd ../
       fi
     done
   cd ../
  done
