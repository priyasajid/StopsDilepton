# 
# Recipe to continue the setup of our 80X analysis after the checkout of StopsDilepton package
#
echo JetMETCorrections/Modules/ >> .git/info/sparse-checkout
git checkout

eval `scram runtime -csh`
cd $CMSSW_BASE/src

# nanoAOD tools (for MET Significance, JEC/JER...)
git clone https://github.com/danbarto/nanoAOD-tools.git PhysicsTools/NanoAODTools
cd $CMSSW_BASE/src

# RootTools (for plotting, sample handling, processing)
git clone -b 'v0.1_stops2l' --single-branch --depth 1 https://github.com/danbarto/RootTools.git
cd $CMSSW_BASE/src

# Shared samples (miniAOD/nanoAOD)
git clone -b 'v0.1_stops2l' --single-branch --depth 1 https://github.com/danbarto/Samples.git
cd $CMSSW_BASE/src

# Shared analysis tools and data
git clone -b 'v0.1_stops2l' --single-branch --depth 1 https://github.com/danbarto/Analysis.git
cd $CMSSW_BASE/src

scram b -j9

cd $CMSSW_BASE/src
git fetch origin
git checkout -b 101X origin/101X

#compile
cd $CMSSW_BASE/src && scram b -j 8 