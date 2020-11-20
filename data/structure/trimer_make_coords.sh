#!/bin/bash

BASEDIR=`pwd`
for i in 01  02 03 04 05 06 07 08 09 10  11 12 13 14 15 16 17 18 19 20 
  do
   mkdir $i
   cd $i

    for j in  02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20
     do
      if [ $i -lt $j ]
       then
        mkdir -p $j
        cd $j
       
           cat $BASEDIR/meth.xyz $BASEDIR/mono_$j.xyz $BASEDIR/mono_$i.xyz  > trim.xyz
           cat $BASEDIR/head trim.xyz $BASEDIR/tail > run3b.inp
           cp ../../one_j_script.sh .
        cd ../
       fi
      done
      #sbatch one_j_script.sh
    cd ../
  done
