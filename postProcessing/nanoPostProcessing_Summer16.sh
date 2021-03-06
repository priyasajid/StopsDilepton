### v5 for new MVA classifiers
#
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --flagTTBar --sample TTLep_pow #SPLIT50
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --flagTTBar --sample TTSingleLep_pow #SPLIT50
python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --flagTTBar --sample TTGJets TTGJets_ext #SPLIT50
#
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample TTZToQQ #SPLIT4
python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample TTZToLLNuNu_ext2 TTZToLLNuNu_ext3 #SPLIT9
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample TTZToLLNuNu_m1to10 #SPLIT5

#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M10to50_LO #SPLIT20
##
##python nanoPostProcessing.py  --overwrite --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M50_ext2 #SPLIT40
##python nanoPostProcessing.py  --overwrite --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M10to50 #SPLIT40
#
python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M50_LO_ext1 DYJetsToLL_M50_LO_ext2 #SPLIT50
python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M50_LO_ext1 DYJetsToLL_M50_LO_ext2 --LHEHTCut 70 #SPLIT50
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M50_HT70to100 #SPLIT10
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M50_HT100to200_ext #SPLIT10
python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M50_HT200to400 DYJetsToLL_M50_HT200to400_ext #SPLIT20
python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M50_HT400to600 DYJetsToLL_M50_HT400to600_ext #SPLIT20
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M50_HT600to800 #SPLIT10
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M50_HT800to1200 #SPLIT10
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M50_HT1200to2500 #SPLIT3
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M50_HT2500toInf #SPLIT1
#
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M10to50_LO #SPLIT20
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M10to50_LO --LHEHTCut 70 #SPLIT20
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M5to50_HT70to100 #SPLIT10
python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M5to50_HT100to200 DYJetsToLL_M5to50_HT100to200_ext #SPLIT20
python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M5to50_HT200to400 DYJetsToLL_M5to50_HT200to400_ext #SPLIT16
python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M5to50_HT400to600 DYJetsToLL_M5to50_HT400to600_ext #SPLIT4
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample DYJetsToLL_M5to50_HT600toInf #SPLIT4
#
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample TToLeptons_sch_amcatnlo #SPLIT8
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample T_tch_pow #SPLIT20
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample TBar_tch_pow #SPLIT20
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample T_tWch_ext #SPLIT12
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample TBar_tWch_ext #SPLIT11
#
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample TTHbb #SPLIT5
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample TTHnobb_pow #SPLIT11
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample THQ #SPLIT8
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample THW #SPLIT2
##python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample TGJets TGJets_ext #SPLIT20
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample tZq_ll_ext #SPLIT20
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample tWll #SPLIT1
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample tWnunu #SPLIT1
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample TTWToLNu_ext2 #SPLIT16
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample TTWToQQ #SPLIT3
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample TTGJets TTGJets_ext #SPLIT20

python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample VVTo2L2Nu VVTo2L2Nu_ext #SPLIT20
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample WWToLNuQQ #SPLIT18
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample ZZTo2Q2Nu #SPLIT20
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample ZZTo2L2Q #SPLIT4
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample ZZTo2L2Nu #SPLIT20
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample ZZTo4L #SPLIT20
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample WZTo1L1Nu2Q #SPLIT20
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample WZTo1L3Nu #SPLIT6
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample WZTo2L2Q #SPLIT20
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample WZTo3LNu_ext #SPLIT20
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample TTTT #SPLIT1
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample TTWW #SPLIT5
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample TTWZ #SPLIT5
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample TTZZ #SPLIT5
#
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample WWW_4F #SPLIT1
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample WWZ #SPLIT1
##python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample WZG #SPLIT1
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample WZZ #SPLIT2
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --sample ZZZ #SPLIT2

#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15 --skipGenLepMatching --sample T2tt_mStop_850_mLSP_100 #SPLIT2
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15 --skipGenLepMatching --sample T2tt_mStop_500_mLSP_325 #SPLIT2
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15 --skipGenLepMatching --susySignal --fastSim --sample SMS_T2tt_mStop_150to250 #SPLIT30
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15 --skipGenLepMatching --susySignal --fastSim --sample SMS_T2tt_mStop_250to350 #SPLIT30
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15 --skipGenLepMatching --susySignal --fastSim --sample SMS_T2tt_mStop_350to400 #SPLIT30
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15 --skipGenLepMatching --susySignal --fastSim --sample SMS_T2tt_mStop_400to1200 #SPLIT30

#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --susySignal --fastSim --sample SMS_T8bbllnunu_XCha0p5_XSlep0p05 #SPLIT40
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --susySignal --fastSim --sample SMS_T8bbllnunu_XCha0p5_XSlep0p5 #SPLIT40
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --susySignal --fastSim --sample SMS_T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1000 #SPLIT40
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --susySignal --fastSim --sample SMS_T8bbllnunu_XCha0p5_XSlep0p95 #SPLIT32
#python nanoPostProcessing.py  --forceProxy --skim dilep --year 2016 --processingEra stops_2016_nano_v0p15   --skipGenLepMatching --susySignal --fastSim --sample SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_700_1300 #SPLIT32

