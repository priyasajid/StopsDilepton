import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

# Logging
import logging
logger = logging.getLogger(__name__)

from StopsDilepton.samples.color import color

# Data directory
try:
    data_directory_ = sys.modules['__main__'].data_directory
except:
    from StopsDilepton.samples.default_locations import default_locations
    data_directory_ = default_locations.mc_2017_data_directory 

# Take post processing directory if defined in main module
try:
  import sys
  postProcessing_directory_ = sys.modules['__main__'].postProcessing_directory
except:
  from StopsDilepton.samples.default_locations import default_locations
  postProcessing_directory_ = default_locations.mc_2017_postProcessing_directory 

logger.info("Loading MC samples from directory %s", os.path.join(data_directory_, postProcessing_directory_))

DY_M5to50_HT = [
                "DYJetsToLL_M10to50_LO_lheHT100", 
                "DYJetsToLL_M4to50_HT100to200_comb",
                "DYJetsToLL_M4to50_HT200to400_comb",
                "DYJetsToLL_M4to50_HT400to600_comb",
                "DYJetsToLL_M4to50_HT600toInf_comb"
                ] 

DY_M50_HT =[
            "DYJetsToLL_M50_LO_comb_lheHT70", 
            "DYJetsToLL_M50_HT70to100",
            "DYJetsToLL_M50_HT100to200",
            "DYJetsToLL_M50_HT200to400_comb",
            "DYJetsToLL_M50_HT400to600_comb",
            "DYJetsToLL_M50_HT600to800",
            "DYJetsToLL_M50_HT800to1200",
            "DYJetsToLL_M50_HT1200to2500",
            "DYJetsToLL_M50_HT2500toInf"
            ] 


dirs = {}
dirs['DY']               = ["DYJetsToLL_M50_ext2", "DYJetsToLL_M10to50" ]
dirs['DY_LO']            = ["DYJetsToLL_M50_LO_comb", "DYJetsToLL_M10to50_LO"]
dirs['DY_LO_M50']        = ["DYJetsToLL_M50_LO_comb"]
dirs['DY_lowMass_LO']    = ["DYJetsToLL_M10to50_LO"]
dirs['DY_HT_LO']         =  DY_M50_HT + DY_M5to50_HT

dirs['TTLep_pow']        = ["TTLep_pow"]
dirs['TTSingleLep_pow']  = ["TTSingleLep_pow"] 

dirs['singleTop_tWch']   = ["TBar_tWch_ext", "T_tWch_ext"]
dirs['singleTop_tch']    = ["T_tch_pow", "TBar_tch_pow"]
dirs['singleTop_sch']    = ["TToLeptons_sch_amcatnlo"]

dirs['Top_pow']          = dirs['TTLep_pow'] + dirs['singleTop_tWch'] + dirs['singleTop_tch'] + dirs['singleTop_sch']

dirs['TZQ']              = ["tZq_ll"]# tZq_nunu to be added in the next round

dirs['TTH']              = ["TTHnobb_pow", "TTHbb"]
dirs['TTZtoLLNuNu']      = ["TTZToLLNuNu", "TTZToLLNuNu_m1to10"]
dirs['TTZtoQQ']          = ["TTZToQQ"]
dirs['TTZ']              = dirs['TTZtoLLNuNu'] + dirs['TTZtoQQ']
dirs['TTW']              = ['TTWToLNu', 'TTWToQQ']
dirs['TTVV']             = ['TTWW', 'TTWZ', 'TTZZ']
dirs['TWZ']              = ['tWll', 'tWnunu']
dirs['TTTT']             = ['TTTT']
dirs['THX']              = ['THQ', 'THW']

dirs['TTXNoZ']           = dirs['TTVV'] + dirs['TTW'] + dirs['TWZ'] + dirs['TZQ'] + dirs['TTH'] + dirs['TTTT'] + dirs['THX']
dirs['TTX']              = dirs['TTXNoZ'] + dirs['TTZ']

dirs['diBosonInclusive'] = ["WW", "WZ", "ZZ"]
dirs['WW']               = ["WWToLNuQQ"]
#dirs['WW_']              = ["WWToLNuQQ_comb","WWTo2L2Nu"]
#dirs['WWTo2L2Nu']        = ["WWTo2L2Nu"]
dirs['VVTo2L2Nu']        = ["VVTo2L2Nu"]
dirs['WZ']               = ["WZTo1L1Nu2Q", "WZTo2L2Q", "WZTo1L3Nu", "WZTo3LNu_amcatnlo"]
dirs['ZZ']               = ["ZZTo2L2Q"] # "ZZTo2Q2Nu"
dirs['ZZ4l']             = ["ZZTo4L"] # "ZZTo2Q2Nu"
#dirs['ZZTo2L2Nu']        = ["ZZTo2L2Nu"]
#dirs['ZZ_']              = ["ZZTo2L2Q", "ZZTo2Q2Nu","ZZTo2L2Nu"]
dirs['diBoson']          = dirs['WW'] + dirs['WZ'] + dirs['ZZ'] + dirs['VVTo2L2Nu']
#dirs['diBoson_']         = dirs['WW_'] + dirs['WZ'] + dirs['ZZ_']
dirs['triBoson']         = ["WWW_4F","WWZ_4F","WZZ","ZZZ"] 
dirs['multiBoson']       = dirs['diBoson'] + dirs['triBoson']
#dirs['EWK']              = dirs['diBoson'] + dirs['triBoson'] + dirs['TTX']
#dirs['QCD_HT']           = ["QCD_HT300to500_comb", "QCD_HT500to700_ext", "QCD_HT700to1000_comb", "QCD_HT1000to1500_comb", "QCD_HT1500to2000_comb", "QCD_HT2000toInf_comb"]
##dirs['QCD_Mu5']          = ["QCD_Pt20to30_Mu5", "QCD_Pt50to80_Mu5", "QCD_Pt80to120_Mu5", "QCD_Pt120to170_Mu5", "QCD_Pt170to300_Mu5", "QCD_Pt300to470_Mu5", "QCD_Pt470to600_Mu5", "QCD_Pt600to800_Mu5", "QCD_Pt800to1000_Mu5", "QCD_Pt1000toInf_Mu5"]
##dirs['QCD_EM+bcToE']     = ["QCD_Pt_20to30_bcToE", "QCD_Pt_30to80_bcToE", "QCD_Pt_80to170_bcToE", "QCD_Pt_170to250_bcToE", "QCD_Pt_250toInf_bcToE", "QCD_Pt15to20_EMEnriched", "QCD_Pt20to30_EMEnriched", "QCD_Pt50to80_EMEnriched", "QCD_Pt80to120_EMEnriched", "QCD_Pt120to170_EMEnriched", "QCD_Pt170to300_EMEnriched"]
##dirs['QCD_EM+bcToE']    = ["QCD_Pt_15to20_bcToE", "QCD_Pt_20to30_bcToE", "QCD_Pt_30to80_bcToE", "QCD_Pt_80to170_bcToE", "QCD_Pt_170to250_bcToE", "QCD_Pt_250toInf_bcToE", "QCD_Pt15to20_EMEnriched", "QCD_Pt20to30_EMEnriched", "QCD_Pt30to50_EMEnriched", "QCD_Pt50to80_EMEnriched", "QCD_Pt80to120_EMEnriched", "QCD_Pt120to170_EMEnriched", "QCD_Pt170to300_EMEnriched", "QCD_Pt300toInf_EMEnriched"]
##dirs['QCD_Mu5+EM+bcToE'] = ["QCD_Pt20to30_Mu5", "QCD_Pt50to80_Mu5", "QCD_Pt80to120_Mu5", "QCD_Pt120to170_Mu5", "QCD_Pt170to300_Mu5", "QCD_Pt300to470_Mu5", "QCD_Pt470to600_Mu5", "QCD_Pt600to800_Mu5", "QCD_Pt800to1000_Mu5", "QCD_Pt1000toInf_Mu5", "QCD_Pt_20to30_bcToE", "QCD_Pt_30to80_bcToE", "QCD_Pt_80to170_bcToE", "QCD_Pt_170to250_bcToE", "QCD_Pt_250toInf_bcToE", "QCD_Pt15to20_EMEnriched", "QCD_Pt20to30_EMEnriched", "QCD_Pt50to80_EMEnriched", "QCD_Pt80to120_EMEnriched", "QCD_Pt120to170_EMEnriched", "QCD_Pt170to300_EMEnriched"]
##dirs['QCD_Mu5+EM+bcToE']= ["QCD_Pt20to30_Mu5", "QCD_Pt50to80_Mu5", "QCD_Pt80to120_Mu5", "QCD_Pt120to170_Mu5", "QCD_Pt170to300_Mu5", "QCD_Pt300to470_Mu5", "QCD_Pt470to600_Mu5", "QCD_Pt600to800_Mu5", "QCD_Pt800to1000_Mu5", "QCD_Pt1000toInf_Mu5", "QCD_Pt_15to20_bcToE", "QCD_Pt_20to30_bcToE", "QCD_Pt_30to80_bcToE", "QCD_Pt_80to170_bcToE", "QCD_Pt_170to250_bcToE", "QCD_Pt_250toInf_bcToE", "QCD_Pt15to20_EMEnriched", "QCD_Pt20to30_EMEnriched", "QCD_Pt30to50_EMEnriched", "QCD_Pt50to80_EMEnriched", "QCD_Pt80to120_EMEnriched", "QCD_Pt120to170_EMEnriched", "QCD_Pt170to300_EMEnriched", "QCD_Pt300toInf_EMEnriched"]
##dirs['QCD']              = ["QCD_Pt30to50", "QCD_Pt50to80", "QCD_Pt80to120", "QCD_Pt120to170", "QCD_Pt170to300", "QCD_Pt300to470", "QCD_Pt470to600", "QCD_Pt600to800", "QCD_Pt800to1000", "QCD_Pt1000to1400", "QCD_Pt1400to1800", "QCD_Pt1800to2400", "QCD_Pt2400to3200"]
##dirs['QCD']             = ["QCD_Pt10to15", "QCD_Pt15to30", "QCD_Pt30to50", "QCD_Pt50to80", "QCD_Pt80to120", "QCD_Pt120to170", "QCD_Pt170to300", "QCD_Pt300to470", "QCD_Pt470to600", "QCD_Pt600to800", "QCD_Pt800to1000", "QCD_Pt1000to1400", "QCD_Pt1400to1800", "QCD_Pt1800to2400", "QCD_Pt2400to3200", "QCD_Pt3200"]
#
#dirs['nonTop']           = dirs['multiBoson'] + dirs['DY_HT_LO'] + dirs['TTZ_LO'] + dirs['TTXNoZ']
#
##dirs['WGToLNuG']     = ["WGToLNuG"]
#dirs['ZGTo2LG']      = ["ZGTo2LG_ext"]
##dirs['WGJets']       = ["WGJets"]
#dirs['ZGJets']       = ["ZGJets"]
#dirs['ZG']           = dirs['ZGTo2LG'] + dirs['ZGJets']
#
directories = { key : [ os.path.join( data_directory_, postProcessing_directory_, dir) for dir in dirs[key]] for key in dirs.keys()}

#
DY_LO_17           = Sample.fromDirectory(name="DY_LO",            treeName="Events", isData=False, color=color.DY,              texName="DY (LO)",                           directory=directories['DY_LO'])
DY_LO_M50_17           = Sample.fromDirectory(name="DY_LO_M50",            treeName="Events", isData=False, color=color.DY,              texName="DY (LO)",                           directory=directories['DY_LO_M50'])
DY_lowMass_LO_17   = Sample.fromDirectory(name="DY_lowMass_LO",    treeName="Events", isData=False, color=color.DY,              texName="DY (LO)",                           directory=directories['DY_lowMass_LO'])
DY_HT_LO_17        = Sample.fromDirectory(name="DY_HT_LO",         treeName="Events", isData=False, color=color.DY,              texName="Drell-Yan",                         directory=directories['DY_HT_LO'])
Top_pow_17         = Sample.fromDirectory(name="Top_pow",          treeName="Events", isData=False, color=color.TTJets,          texName="t#bar{t}/single-t",                 directory=directories['Top_pow'])
Top_pow_1l_17      = Sample.fromDirectory(name="Top_1l_pow",       treeName="Events", isData=False, color=color.TTJets_1l,       texName="t#bar{t} (1l)",                     directory=directories['TTSingleLep_pow'])
TTX_17             = Sample.fromDirectory(name="TTX",              treeName="Events", isData=False, color=color.TTX,             texName="t#bar{t}H/W/Z, tZq",                directory=directories['TTX'])
TTXNoZ_17          = Sample.fromDirectory(name="TTXNoZ",           treeName="Events", isData=False, color=color.TTXNoZ,          texName="t#bar{t}H/W, tZq, tWZ",             directory=directories['TTXNoZ'])
TTH_17             = Sample.fromDirectory(name="TTH",              treeName="Events", isData=False, color=color.TTH,             texName="t#bar{t}H",                         directory=directories['TTH'])
TTW_17             = Sample.fromDirectory(name="TTW",              treeName="Events", isData=False, color=color.TTW,             texName="t#bar{t}W",                         directory=directories['TTW'])
TTZ_17             = Sample.fromDirectory(name="TTZ",              treeName="Events", isData=False, color=color.TTZ,             texName="t#bar{t}Z",                         directory=directories['TTZ'])
TTZtoLLNuNu_17     = Sample.fromDirectory(name="TTZtoNuNu",        treeName="Events", isData=False, color=color.TTZtoLLNuNu,     texName="t#bar{t}Z (l#bar{l}/#nu#bar{#nu})", directory=directories['TTZtoLLNuNu'])
TTZtoQQ_17         = Sample.fromDirectory(name="TTZtoQQ",          treeName="Events", isData=False, color=color.TTZtoQQ,         texName="t#bar{t}Z (q#bar{q})",              directory=directories['TTZtoQQ'])
TZQ_17             = Sample.fromDirectory(name="TZQ",              treeName="Events", isData=False, color=color.TZQ,             texName="tZq",                               directory=directories['TZQ'])
#TWZ            = Sample.fromDirectory(name="TWZ",              treeName="Events", isData=False, color=color.TWZ,             texName="tWZ",                               directory=directories['TWZ'])
#WJetsToLNu     = Sample.fromDirectory(name="WJetsToLNu",       treeName="Events", isData=False, color=color.WJetsToLNu,      texName="W(l,#nu) + Jets",                   directory=directories['WJetsToLNu'])
##WJetsToLNu_LO  = Sample.fromDirectory(name="WJetsToLNu_LO",    treeName="Events", isData=False, color=color.WJetsToLNu,      texName="W(l,#nu) + Jets (LO)",              directory=directories['WJetsToLNu_LO'])
##WJetsToLNu_HT  = Sample.fromDirectory(name="WJetsToLNu_HT",    treeName="Events", isData=False, color=color.WJetsToLNu,      texName="W(l,#nu) + Jets (HT)",              directory=directories['WJetsToLNu_HT'])
#diBoson        = Sample.fromDirectory(name="diBoson",          treeName="Events", isData=False, color=color.diBoson,         texName="VV (excl.)",                        directory=directories['diBoson'])
VVTo2L2Nu_17       = Sample.fromDirectory(name="VVTo2L2Nu",        treeName="Events", isData=False, color=color.VV,              texName="VV to ll#nu#nu",                    directory=directories['VVTo2L2Nu'])
WW_17              = Sample.fromDirectory(name="WW",               treeName="Events", isData=False, color=color.WW,              texName="WW w/o ll#nu#nu",                   directory=directories['WW'])
WZ_17              = Sample.fromDirectory(name="WZ",               treeName="Events", isData=False, color=color.WZ,              texName="WZ w/o ll#nu#nu",                   directory=directories['WZ'])
ZZ_17              = Sample.fromDirectory(name="ZZ",               treeName="Events", isData=False, color=color.ZZ,              texName="ZZ w/o ll#nu#nu",                   directory=directories['ZZ'])
ZZ4l_17            = Sample.fromDirectory(name="ZZ4l",             treeName="Events", isData=False, color=color.ZZ,              texName="ZZ(4l)",                            directory=directories['ZZ4l'])
triBoson_17        = Sample.fromDirectory(name="triBoson",         treeName="Events", isData=False, color=color.triBoson,        texName="WWW,WWZ,WZZ,ZZZ",                   directory=directories['triBoson'])
multiBoson_17      = Sample.fromDirectory(name="multiBoson",       treeName="Events", isData=False, color=color.diBoson,         texName="multi boson",                       directory=directories['multiBoson'])
#QCD_HT         = Sample.fromDirectory(name="QCD_HT",           treeName="Events", isData=False, color=color.QCD,             texName="QCD (HT)",                          directory=directories['QCD_HT'])
##QCD_Mu5        = Sample.fromDirectory(name="QCD_Mu5",          treeName="Events", isData=False, color=color.QCD,             texName="QCD (Mu5)",                         directory=directories['QCD_Mu5'])
##QCD_EMbcToE    = Sample.fromDirectory(name="QCD_EM+bcToE",     treeName="Events", isData=False, color=color.QCD,             texName="QCD (Em+bcToE)",                    directory=directories['QCD_EM+bcToE'])
##QCD_Mu5EMbcToE = Sample.fromDirectory(name="QCD_Mu5+EM+bcToE", treeName="Events", isData=False, color=color.QCD,             texName="QCD (Mu5+Em+bcToE)",                directory=directories['QCD_Mu5+EM+bcToE'])
##QCD_Pt         = Sample.fromDirectory(name="QCD",              treeName="Events", isData=False, color=color.QCD,             texName="QCD",                               directory=directories['QCD'])
#
##WGToLNuG = Sample.fromDirectory(name="WGToLNuG",       treeName="Events", isData=False, color=color.diBoson,       texName="WGToLNuG",                       directory=directories['WGToLNuG'])
##ZGTo2LG  = Sample.fromDirectory(name="ZGTo2LG",       treeName="Events", isData=False, color=color.diBoson,        texName="ZGTo2LG",                       directory=directories['ZGTo2LG'] )
##WGJets   = Sample.fromDirectory(name="WGJets",       treeName="Events", isData=False, color=color.diBoson,         texName="WGJets",                       directory=directories['WGJets']  )
##ZGJets   = Sample.fromDirectory(name="ZGJets",       treeName="Events", isData=False, color=color.diBoson,         texName="ZGJets",                       directory=directories['ZGJets']  )
#ZG        = Sample.fromDirectory(name="ZG",            treeName="Events", isData=False, color=color.QCD,             texName="ZG",                           directory=directories['ZG']  )
#EWK        = Sample.fromDirectory(name="EWK",            treeName="Events", isData=False, color=color.QCD,             texName="EWK",                           directory=directories['EWK']  )



#Top_gaussian         = copy.deepcopy(Top_pow)
#Top_gaussian.name    = Top_pow.name + ' (gaussian)'
#Top_gaussian.texName = Top_pow.texName + ' (gaussian)'
#Top_gaussian.color   = ROOT.kCyan
#Top_gaussian.setSelectionString('abs(met_pt-met_genPt)&&abs(met_pt-met_genPt)<=50&&l1_mcMatchId!=0&&l2_mcMatchId!=0')
#
#
#Top_nongaussian         = copy.deepcopy(Top_pow)
#Top_nongaussian.name    = Top_pow.name + ' (non-gaussian)'
#Top_nongaussian.texName = Top_pow.texName + ' (non-gaussian)'
#Top_nongaussian.color   = ROOT.kCyan + 2
#Top_nongaussian.setSelectionString('abs(met_pt-met_genPt)>50&&l1_mcMatchId!=0&&l2_mcMatchId!=0')
#
#
#Top_fakes         = copy.deepcopy(Top_pow)
#Top_fakes.name    = Top_pow.name + ' (fakes)'
#Top_fakes.texName = Top_pow.texName + ' (fakes)'
#Top_fakes.color   = ROOT.kCyan + 4
#Top_fakes.setSelectionString('!(l1_mcMatchId!=0&&l2_mcMatchId!=0)')


