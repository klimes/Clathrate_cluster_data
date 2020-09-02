import os.path

def get_nbody(data,str):
   E2b12=float(data[5])-float(data[1])-float(data[2])
   E2b13=float(data[6])-float(data[1])-float(data[3])
   E2b14=float(data[7])-float(data[1])-float(data[4])
   E2b23=float(data[8])-float(data[2])-float(data[3])
   E2b24=float(data[9])-float(data[2])-float(data[4])
   E2b34=float(data[10])-float(data[3])-float(data[4])
   #print "2body ", str, E2b12,  E2b13, E2b14, E2b23, E2b24, E2b34

   E3b123=float(data[11])-float(data[1])-float(data[2])-float(data[3])
   E3b124=float(data[12])-float(data[1])-float(data[2])-float(data[4])
   E3b134=float(data[13])-float(data[1])-float(data[3])-float(data[4])
   E3b234=float(data[14])-float(data[2])-float(data[3])-float(data[4])
   #print E3b123, E3b124, E3b134, E3b234

   E3b123na=E3b123-E2b12-E2b13-E2b23
   E3b124na=E3b124-E2b12-E2b14-E2b24
   E3b134na=E3b134-E2b13-E2b14-E2b34
   E3b234na=E3b234-E2b23-E2b24-E2b34
   #print "3body ", str, E3b123na, E3b124na, E3b134na, E3b234na

   E4b=float(data[0])-float(data[1])-float(data[2])-float(data[3])-float(data[4])
   #print E4b
   E4bna=E4b-E2b12-E2b13-E2b14-E2b23-E2b24-E2b34-E3b123na-E3b124na-E3b134na-E3b234na
   #print "4body ", str, E4bna
   return E4bna, E2b12, E2b13, E2b14, E2b23, E2b24, E2b34, E3b123, E3b124, E3b134, E3b234


fl=open("hf_avtz_tot.dat","w")
flCABS=open("cabs_avtz_tot.dat","w")
flMP2=open("mp2_avtz_tot.dat","w")
flF12=open("f12_avtz_tot.dat","w")
flCC=open("cc_avtz_tot.dat","w")
flCCF12b=open("ccf12b_avtz_tot.dat","w")
flTu=open("tu_avtz_tot.dat","w")
flTs=open("ts_avtz_tot.dat","w")
flF12a=open("f12a_avtz_tot.dat","w")
flF12b=open("f12b_avtz_tot.dat","w")

for i in range(1,18+1):
  print (i)
  i0=str(i).zfill(2)
  for j in range(i+1,19+1):
    j0=str(j).zfill(2)
    for k in range(j+1,20+1):
      k0=str(k).zfill(2)
      exi=os.path.isfile(i0+"/"+j0+"/"+k0+"/run4b.out")
      #file does not exist, keep the line empty
      if exi == False:
        #print i0+"/"+j0+"/"+k0+"/run4b.out", exi
        fl.write("00_"+i0+"_"+j0+"_"+k0+" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n")
        flCABS.write("00_"+i0+"_"+j0+"_"+k0+" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n")
        flMP2.write("00_"+i0+"_"+j0+"_"+k0+" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n")
        flF12.write("00_"+i0+"_"+j0+"_"+k0+" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n")
        flCC.write("00_"+i0+"_"+j0+"_"+k0+" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n")
        flF12a.write("00_"+i0+"_"+j0+"_"+k0+" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n")
        flF12b.write("00_"+i0+"_"+j0+"_"+k0+" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n")
      else:
         #was the run successful? grep for the final line
         cor_exi=False
         if "Molpro calculation terminated" in open(i0+"/"+j0+"/"+k0+"/run4b.out").read():
            cor_exi=True
         if cor_exi == False:
           fl.write("00_"+i0+"_"+j0+"_"+k0+" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n")
           flCABS.write("00_"+i0+"_"+j0+"_"+k0+" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n")
           flMP2.write("00_"+i0+"_"+j0+"_"+k0+" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n")
           flF12.write("00_"+i0+"_"+j0+"_"+k0+" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n")
           flCC.write("00_"+i0+"_"+j0+"_"+k0+" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n")
           flF12a.write("00_"+i0+"_"+j0+"_"+k0+" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n")
           flF12b.write("00_"+i0+"_"+j0+"_"+k0+" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n")
         else:
           HF=[]
           CABS=[]
           MP2=[]
           MF12=[]
           CC=[]
           CCF12b=[]
           Tu=[]
           fac=[]
           Ts=[]
           F12a=[]
           F12b=[]
           count=-1
           count2=-1
           countMP2=-1
           countMF12=-1
           for line in open(i0+"/"+j0+"/"+k0+"/run4b.out"):
            if "!RHF STATE  1.1 Ene" in line:
              #print line,
              tmp=line.split()
              HF.append(tmp[4])
   
            if "New reference energy" in line:
              #print line,
              tmp=line.split()
              CABS.append(tmp[3])
   
            #get MP2 energies
            if "DF-MP2-F12 correlation energies:" in line:
              countMP2=3
              countMF12=6
            if countMP2==0:
              tmp=line.split()
              MP2.append(tmp[3])
            #get MP2-F12 energies
            if countMP2==0:
              tmp=line.split()
              MF12.append(tmp[3])
   
            #get CCSD correlation energy
            if "CCSD correlation energy" in line:
              #print line,
              tmp=line.split()
              CC.append(tmp[3])
   
            #get CCSD correlation energy
            if "CCSD-F12b correlation energy" in line:
              #print line,
              tmp=line.split()
              CCF12b.append(tmp[3])
   
            #get scaled triples energy
            if "Triples (T) contribution (scaled)" in line:
              #print line,
              tmp=line.split()
              Ts.append(tmp[4])
   
            #get scaling factor for triples
            if "Scale factor for triples energy" in line:
              #print line,
              tmp=line.split()
              fac.append(tmp[5])
   
            #get CCSD(T)-F12a energies
            if "F12a corrections for ansatz F12/3C(FIX) added to CCSD energy" in line:
              count=7
            if count==0:
              #print line,
              tmp=line.split()
              F12a.append(tmp[3])
   
            #get CCSD(T)-F12a energies
            if "F12b corrections for ansatz F12/3C(FIX) added to CCSD(T)-F12a energy" in line:
              count2=7
            if count2==0:
              #print line,
              tmp=line.split()
              F12b.append(tmp[3])
   
            count-=1
            count2-=1
            countMP2-=1
            countMF12-=1
   
           #take only every other line for CABS 
           CABS=CABS[1::2] 
           Ts=Ts[1::2] 
           for i in range(len(fac)):
             Tu.append(str(float(Ts[i])/float(fac[i])))
           
           fl.write("00_"+i0+"_"+j0+"_"+k0 +" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" "+ " ".join(HF)+"\n")
           flCABS.write("00_"+i0+"_"+j0+"_"+k0 +" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" "+ " ".join(CABS)+"\n")
           flMP2.write("00_"+i0+"_"+j0+"_"+k0 +" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" "+ " ".join(MP2)+"\n")
           flF12.write("00_"+i0+"_"+j0+"_"+k0 +" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" "+ " ".join(MF12)+"\n")
           flCC.write("00_"+i0+"_"+j0+"_"+k0 +" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" "+ " ".join(CC)+"\n")
           flCCF12b.write("00_"+i0+"_"+j0+"_"+k0 +" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" "+ " ".join(CCF12b)+"\n")
           flTs.write("00_"+i0+"_"+j0+"_"+k0 +" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" "+ " ".join(Ts)+"\n")
           flTu.write("00_"+i0+"_"+j0+"_"+k0 +" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" "+ " ".join(Tu)+"\n")
           flF12a.write("00_"+i0+"_"+j0+"_"+k0 +" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" "+ " ".join(F12a)+"\n")
           flF12b.write("00_"+i0+"_"+j0+"_"+k0 +" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" "+ " ".join(F12b)+"\n")

fl.close()
flCABS.close()
flMP2.close()
flF12.close()
flCC.close()
flCCF12b.close()
flTs.close()
flTu.close()
flF12a.close()
flF12b.close()
