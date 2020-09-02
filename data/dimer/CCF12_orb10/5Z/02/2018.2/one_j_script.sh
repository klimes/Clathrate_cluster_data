#!/bin/sh
#PBS -S /bin/bash
#PBS -q default@cerit-pbs.cerit-sc.cz
#PBS -l select=1:ncpus=4:mem=300gb:scratch_ssd=1000gb 
#PBS -l walltime=48:00:00
#PBS -N cc_f12_5z_2b
#PBS -j oe


. /packages/run/modules-2.0/init/bash

date

cd $PBS_O_WORKDIR

ulimit -s
ulimit -s unlimited
ulimit -s

cp run2b.inp $SCRATCHDIR/

cd $SCRATCHDIR

   /storage/brno2/home/kelum/src/molpro/molpro_2018.2/bin/molpro -t 1 run2b.inp -d $SCRATCHDIR -W $SCRATCHDIR

cp run2b.out  $PBS_O_WORKDIR/

rm $SCRATCHDIR/*

exit 0
