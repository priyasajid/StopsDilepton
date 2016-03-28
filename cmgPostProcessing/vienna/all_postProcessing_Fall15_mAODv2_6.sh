#!/bin/sh
#nohup krenew -t -K 10 -- bash -c "python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_Pt10to15" 
#nohup krenew -t -K 10 -- bash -c "python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_Pt15to30" 
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_Pt30to50
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_Pt50to80
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_Pt80to120
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_Pt120to170
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_Pt170to300
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_Pt300to470
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_Pt470to600
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_Pt600to800
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_Pt800to1000
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_Pt1000to1400
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_Pt1400to1800
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_Pt1800to2400
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_Pt2400to3200
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_Pt3200toInf
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_HT100to200
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_HT200to300
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_HT300to500
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_HT500to700
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_HT700to1000
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_HT1000to1500
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_HT1500to2000
python cmgPostProcessing.py --skim=$1 $2  --samples=QCD_HT2000toInf