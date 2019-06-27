# JER study
python systematicVariation.py --era Run2016 --plot_directory v0p15 --reweightPU Central --selection lepSel-POGMetSig12-njet2p-btag0-miniIso0.2-looseLeptonVeto-mll20-onZ-mt2ll100 --beta JERonly --small

# JEC study
python systematicVariation.py --era Run2016 --plot_directory v0p15 --reweightPU Central --selection lepSel-POGMetSig12-njet2p-btag0-miniIso0.2-looseLeptonVeto-mll20-onZ-mt2ll100 --beta JEConly --small



##python systematicVariation.py --dpm --era Run2016 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-njet2p-btag0-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1-onZ --noDYHT --overwrite
##python systematicVariation.py --dpm --era Run2016 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-POGMetSig12-njet2p-btag0-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1-onZ --noDYHT --overwrite
##python systematicVariation.py --dpm --era Run2016 --plot_directory v5 --reweightPU Central --scaling top --variation_scaling --selection lepSel-njet2p-btag0-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
##python systematicVariation.py --dpm --era Run2016 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-POGMetSig12-njet2p-btag0-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite

##python systematicVariation.py --dpm --era Run2017 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-badEEJetVeto-njet2p-btag0-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1-onZ --noDYHT --overwrite
##python systematicVariation.py --dpm --era Run2017 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-badEEJetVeto-POGMetSig12-njet2p-btag0-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1-onZ --noDYHT --overwrite
##python systematicVariation.py --dpm --era Run2017 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-badEEJetVeto-njet2p-btag0-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
##python systematicVariation.py --dpm --era Run2017 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-badEEJetVeto-POGMetSig12-njet2p-btag0-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite

##python systematicVariation.py --dpm --era Run2018 --plot_directory v3 --reweightPU VUp --scaling mc --variation_scaling --selection lepSel-njet2p-btag0-relIso0.12-HEMJetVetoWide-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1-onZ --noDYHT --overwrite
##python systematicVariation.py --dpm --era Run2018 --plot_directory v3 --reweightPU VUp --scaling mc --variation_scaling --selection lepSel-POGMetSig12-njet2p-btag0-relIso0.12-HEMJetVetoWide-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1-onZ --noDYHT --overwrite
##python systematicVariation.py --dpm --era Run2018 --plot_directory v3 --reweightPU VUp --scaling mc --variation_scaling --selection lepSel-njet2p-btag0-relIso0.12-HEMJetVetoWide-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
##python systematicVariation.py --dpm --era Run2018 --plot_directory v5 --reweightPU VUp --scaling mc --variation_scaling --selection lepSel-POGMetSig12-njet2p-btag0-relIso0.12-HEMJetVetoWide-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite


# Other control regions

#python systematicVariation.py --dpm --era Run2016 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-POGMetSig0To12-njet2p-btag0-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
#python systematicVariation.py --dpm --era Run2016 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-POGMetSig0To12-njet2p-btag1p-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
#python systematicVariation.py --dpm --era Run2016 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-POGMetSig12-njet01-btag0-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
#python systematicVariation.py --dpm --era Run2016 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-POGMetSig0To12-njet01-btag0-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
#python systematicVariation.py --dpm --era Run2016 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-POGMetSig12-njet01-btag1-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
#python systematicVariation.py --dpm --era Run2016 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-POGMetSig0To12-njet01-btag1-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite

#python systematicVariation.py --dpm --era Run2017 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-badEEJetVeto-POGMetSig0To12-njet2p-btag0-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
#python systematicVariation.py --dpm --era Run2017 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-badEEJetVeto-POGMetSig0To12-njet2p-btag1p-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
#python systematicVariation.py --dpm --era Run2017 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-badEEJetVeto-POGMetSig12-njet01-btag0-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
#python systematicVariation.py --dpm --era Run2017 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-badEEJetVeto-POGMetSig0To12-njet01-btag0-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
#python systematicVariation.py --dpm --era Run2017 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-badEEJetVeto-POGMetSig12-njet01-btag1-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
#python systematicVariation.py --dpm --era Run2017 --plot_directory v5 --reweightPU Central --scaling mc --variation_scaling --selection lepSel-badEEJetVeto-POGMetSig0To12-njet01-btag1-relIso0.12-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite

#python systematicVariation.py --dpm --era Run2018 --plot_directory v3 --reweightPU VUp --scaling mc --variation_scaling --selection lepSel-POGMetSig0To12-njet2p-btag0-relIso0.12-HEMJetVetoWide-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
#python systematicVariation.py --dpm --era Run2018 --plot_directory v3 --reweightPU VUp --scaling mc --variation_scaling --selection lepSel-POGMetSig0To12-njet2p-btag1p-relIso0.12-HEMJetVetoWide-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
#python systematicVariation.py --dpm --era Run2018 --plot_directory v3 --reweightPU VUp --scaling mc --variation_scaling --selection lepSel-POGMetSig12-njet01-btag0-relIso0.12-HEMJetVetoWide-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
#python systematicVariation.py --dpm --era Run2018 --plot_directory v3 --reweightPU VUp --scaling mc --variation_scaling --selection lepSel-POGMetSig0To12-njet01-btag0-relIso0.12-HEMJetVetoWide-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
#python systematicVariation.py --dpm --era Run2018 --plot_directory v3 --reweightPU VUp --scaling mc --variation_scaling --selection lepSel-POGMetSig12-njet01-btag1-relIso0.12-HEMJetVetoWide-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite
#python systematicVariation.py --dpm --era Run2018 --plot_directory v3 --reweightPU VUp --scaling mc --variation_scaling --selection lepSel-POGMetSig0To12-njet01-btag1-relIso0.12-HEMJetVetoWide-looseLeptonVeto-mll20-dPhiJet0-dPhiJet1 --overwrite

