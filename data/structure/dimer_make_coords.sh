#!/bin/bash

BASEDIR=`pwd`
for i in 01  02 03 04 05 06 07 08  09 10 11  12 13 14 15 16 17 18 19 20 
  do
   mkdir -p $i
   cd $i

   cat $BASEDIR/mono_$i.xyz $BASEDIR/meth.xyz > dim.xyz
   cat $BASEDIR/head dim.xyz $BASEDIR/tail > run2b.inp
   cp ../one_j_script.sh .
   sbatch  one_j_script.sh
   cd ../
  done
