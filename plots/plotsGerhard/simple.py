#!/usr/bin/env python
'''
Small nucleus for training etc
'''

# Standard imports and batch mode
import ROOT, os
ROOT.gROOT.SetBatch(True)


#from math                                import sqrt, cos, sin, pi
from RootTools.core.standard             import *
from StopsDilepton.tools.user            import plot_directory
from StopsDilepton.tools.helpers         import deltaPhi
from StopsDilepton.tools.objectSelection import getFilterCut
from StopsDilepton.tools.cutInterpreter  import cutInterpreter

#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--signal',             action='store',      default="T8bbllnunu_XCha0p5_XSlep0p5_800_1",  nargs='?', help="signal sample")
argParser.add_argument('--mode',               action='store',      default="all",  nargs='?', choices = ['all', 'mumu', 'emu', 'ee'], help="dilepton mode")
argParser.add_argument('--background',         action='store',      default="TTLep_pow",     nargs='?', help="background sample")
argParser.add_argument('--small',                                   action='store_true',     help='Run only on a small subset of the data?', )
argParser.add_argument('--plot_directory',     action='store',      default='analysisPlots_test')
argParser.add_argument('--selection',          action='store',      default='njet2p-btag1p-relIso0.12-looseLeptonVeto-mll20-met80-metSig5-dPhiJet0-dPhiJet1')
args = argParser.parse_args()

#
# Logger
#
import StopsDilepton.tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:                        args.plot_directory += "_small"

#
# Make samples, will be searched for in the postProcessing directory
#
postProcessing_directory = "postProcessed_80X_v35/dilepTiny/"
from StopsDilepton.samples.cmgTuples_Summer16_mAODv2_postProcessed import *
postProcessing_directory = "postProcessed_80X_v35/dilepTiny"
from StopsDilepton.samples.cmgTuples_FastSimT8bbllnunu_mAODv2_25ns_postProcessed import *

# Read variables and sequences
#
read_variables = ["weight/F", "l1_eta/F" , "l1_phi/F", "l2_eta/F", "l2_phi/F", "JetGood[pt/F,eta/F,phi/F,btagCSV/F]", "dl_mass/F", "dl_eta/F", "dl_mt2ll/F", "dl_mt2bb/F", "dl_mt2blbl/F",
                  "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I", "nJetGood/I"]

#
# default offZ for SF
offZ = "&&abs(dl_mass-91.1876)>15" if not (args.selection.count("onZ") or args.selection.count("allZ") or args.selection.count("offZ")) else ""
def getLeptonSelection( mode ):
  if   mode=="mumu": return "nGoodMuons==2&&nGoodElectrons==0&&isOS&&isMuMu" + offZ
  elif mode=="mue":  return "nGoodMuons==1&&nGoodElectrons==1&&isOS&&isEMu"
  elif mode=="ee":   return "nGoodMuons==0&&nGoodElectrons==2&&isOS&&isEE" + offZ
  elif mode=="all":  return "nGoodMuons+nGoodElectrons==2&&isOS&&( " + "(isEE||isMuMu)" + offZ + "|| isEMu)"


signal     = eval(args.signal)
signal.setSelectionString([getFilterCut(isData=False, badMuonFilters = "Summer16"), getLeptonSelection(args.mode)])
signal.name           = "signal"

background = eval(args.background)
background.setSelectionString([getFilterCut(isData=False, badMuonFilters = "Summer16"), getLeptonSelection(args.mode)])
background.name           = "background"

for sample in [signal, background]:
  if args.small:
        sample.reduceFiles( to = 1 )


r = signal.treeReader(variables = map( TreeVariable.fromString, read_variables) )
#signal.chain.SetBranchStatus("*",1)
r.start()
while r.run():
    print r.event.met_pt

r = background.treeReader(variables = map( TreeVariable.fromString, read_variables) )
#background.chain.SetBranchStatus("*",1)
r.start()
while r.run():
    print r.event.met_pt