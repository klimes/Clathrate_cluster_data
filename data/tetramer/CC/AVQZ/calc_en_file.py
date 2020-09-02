import os.path

def get_nbody(data):
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

for method in ['hf','cabs','mp2','f12','cc','ccf12b','ts','tu','f12a','f12b']:
   flb=open(method+"_avtz_bind.dat","w")
   E4btot=0.0
   
   for line in open(method+"_avtz_tot.dat","r"):
     tmp=line.split()
     tmp2=tmp[3:]
     Ebind=get_nbody(tmp2)
    
     E4btot+=Ebind[0]
     Ebind=' '.join(map(str,Ebind))
     flb.write(str(tmp[0]) +" "+ str(tmp[1])+" "+str(tmp[2])+" "+ Ebind+"\n") 
   
      #   if exi == False:
      #     #print i0+"/"+j0+"/"+k0+"/run4b.out", exi
      #     fl.write("00_"+i0+"_"+j0+"_"+k0+" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n")
      #     CABS=CABS[1::2] 
      #     fl.write("00_"+i0+"_"+j0+"_"+k0 +" 00_"+i0+"_"+j0+"_"+k0+" "+str(exi)+" "+ " ".join(HF)+"\n")
   
   flb.close()
   print( method, E4btot, E4btot*627.5096)
