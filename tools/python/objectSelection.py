# StopsDilepton
from StopsDilepton.tools.helpers import mZ, getVarValue, getObjDict, deltaR

# standard imports 
from math import *
import numbers
import textwrap     # for CutBased Ele ID
import operator

jetVars = ['eta','pt','phi','btagDeepB', 'btagCSVV2', 'jetId', 'area', 'rawFactor']

def getJets(c, jetVars=jetVars, jetColl="Jet"):
    return [getObjDict(c, jetColl+'_', jetVars, i) for i in range(int(getVarValue(c, 'n'+jetColl)))]

def jetId(j, ptCut=30, absEtaCut=2.4, ptVar='pt', idVar='jetId'):
  return j[ptVar]>ptCut and abs(j['eta'])<absEtaCut and ( j[idVar] > 0 if idVar is not None else True )

def getGoodJets(c, ptCut=30, absEtaCut=2.4, jetVars=jetVars, jetColl="Jet", ptVar='pt'):
    return filter(lambda j:jetId(j, ptCut=ptCut, absEtaCut=absEtaCut, ptVar='pt'), getJets(c, jetVars, jetColl=jetColl))

def getAllJets(c, leptons, ptCut=30, absEtaCut=2.4, jetVars=jetVars, jetCollections=[ "Jet"], idVar='jetId'):

    jets = sum( [ filter(lambda j:jetId(j, ptCut=ptCut, absEtaCut=absEtaCut, idVar=idVar), getJets(c, jetVars, jetColl=coll)) for coll in jetCollections], [] )
    res  = []

    for jet in jets:
        clean = True
        for lepton in leptons:
            if deltaR(lepton, jet) < 0.4:
                clean = False
                break
        if clean:
            res.append(jet)

    res.sort( key = lambda j:-j['pt'] )

    return res


def isBJet(j, tagger = 'DeepCSV', year = 2016):
    if tagger == 'CSVv2':
        if year == 2016:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
            return j['btagCSVV2'] > 0.8484 
        elif year == 2017 or year == 2018:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
            return j['btagCSVV2'] > 0.8838 
        else:
            raise (NotImplementedError, "Don't know what cut to use for year %s"%year)
    elif tagger == 'DeepCSV':
        if year == 2016:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
            return j['btagDeepB'] > 0.6321
        elif year == 2017:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
            return j['btagDeepB'] > 0.4941
        elif year == 2018:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation102X
            return j['btagDeepB'] > 0.4184
        else:
            raise (NotImplementedError, "Don't know what cut to use for year %s"%year)

def getGenLeps(c):
    return [getObjDict(c, 'genLep_', ['eta','pt','phi','charge', 'pdgId', 'sourceId'], i) for i in range(int(getVarValue(c, 'ngenLep')))]

def getGenParts(c):
    return [getObjDict(c, 'GenPart_', ['eta','pt','phi','charge', 'pdgId', 'motherId', 'grandmotherId'], i) for i in range(int(getVarValue(c, 'nGenPart')))]

genVars = ['eta','pt','phi','mass','charge', 'status', 'pdgId', 'genPartIdxMother', 'statusFlags','index'] 
def getGenPartsAll(c, genVars=genVars):
    return [getObjDict(c, 'GenPart_', genVars, i) for i in range(int(getVarValue(c, 'nGenPart')))]

def filterGenPhotons( genParts, status=None ):
    photons = list( filter( lambda l: abs(l['pdgId']) == 22 and l['status'] > 0, genParts ) )
    return photons

def genLepFromZ( genParts ):
    ''' get all gen leptons (e,m,tau) from Z
    '''
    leptons = list( filter( lambda l: abs(l['pdgId']) in [11,13,15] and abs(genParts[l['genPartIdxMother']]['pdgId']) == 23, genParts ) )
    return leptons

def get_index_str( index ):
    if isinstance(index, int):
        index_str = "["+str(index)+"]"
    elif type(index)==type(""):
        if index.startswith('[') and index.endswith(']'):
            index_str = index
        else:
            index_str = '['+index+']'
    elif index is None:
        index_str=""
    else:
        raise ValueError( "Don't know what to do with index %r" % index )
    return index_str

def alwaysTrue(*args, **kwargs):
  return True
def alwaysFalse(*args, **kwargs):
  return False

def mergeCollections( a, b ):
    allKeys = []
    for coll in [a[0], b[0]]:
        keys = coll.keys()
        for k in keys:
            if k not in allKeys: allKeys += [k]

    merged = a + b
    for m in merged:
        for key in allKeys:
            if not m.has_key(key):
                m[key] = float('nan')

    return merged

## MUONS ##
def muonSelector( lepton_selection, year, ptCut = 10):
    # tigher isolation applied on analysis level
    if lepton_selection == 'tight':
        def func(l):
            return \
                l["pt"]                 >= ptCut \
                and abs(l["eta"])       < 2.4 \
                and l['pfRelIso03_all'] < 0.20 \
                and l["sip3d"]          < 4.0 \
                and abs(l["dxy"])       < 0.05 \
                and abs(l["dz"])        < 0.1 \
                and l["mediumId"] 
    elif lepton_selection == 'tightMiniIso02':
        def func(l):
            return \
                l["pt"]                 >= ptCut \
                and abs(l["eta"])       < 2.4 \
                and l['miniPFRelIso_all'] < 0.20 \
                and l["sip3d"]          < 4.0 \
                and abs(l["dxy"])       < 0.05 \
                and abs(l["dz"])        < 0.1 \
                and l["mediumId"] 
    elif lepton_selection == 'tightNoIso':
        def func(l):
            return \
                l["pt"]                 >= ptCut \
                and abs(l["eta"])       < 2.4 \
                and l["sip3d"]          < 4.0 \
                and abs(l["dxy"])       < 0.05 \
                and abs(l["dz"])        < 0.1 \
                and l["mediumId"] 
    elif lepton_selection == 'loose':
        def func(l):
            return \
                l["pt"]                 >= ptCut \
                and abs(l["eta"])       < 2.4 \
                and l['pfRelIso03_all'] < 0.20 \
                and l["sip3d"]          < 4.0 \
                and abs(l["dxy"])       < 0.05 \
                and abs(l["dz"])        < 0.1
    return func

def muonSelectorString(relIso03 = 0.2, ptCut = 20, absEtaCut = 2.4, dxy = 0.05, dz = 0.1, index = "Sum"):
    idx = None if (index is None) or (type(index)==type("") and index.lower()=="sum") else index
    index_str = get_index_str( index  = idx)
    string = [\
                "Muon_pt"+index_str+">=%s"%ptCut ,
                "abs(Muon_eta"+index_str+")<%s" % absEtaCut ,
                "Muon_mediumId"+index_str+">=1" ,
                "Muon_sip3d"+index_str+"<4.0" ,
                "abs(Muon_dxy"+index_str+")<%s" % dxy ,
                "abs(Muon_dz"+index_str+")<%s" % dz ,
                "Muon_pfRelIso03_all"+index_str+"<%s" % relIso03 ,
             ]
    if type(index)==type("") and index.lower()=='sum':
        return 'Sum$('+'&&'.join(string)+')'
    else:
        return '&&'.join(string)

## ELECTRONS ##

# Electron bitmap
# or  https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/mc102X_doc.html
# Attention: only for nanoAOD v94x or higher (in 80x, only 2 bits are used)
vidNestedWPBitMapNamingList = \
    ['GsfEleMissingHitsCut',
     'GsfEleConversionVetoCut',
     'GsfEleRelPFIsoScaledCut',
     'GsfEleEInverseMinusPInverseCut',
     'GsfEleHadronicOverEMEnergyScaledCut',
     'GsfEleFull5x5SigmaIEtaIEtaCut',
     'GsfEleDPhiInCut',
     'GsfEleDEtaInSeedCut',
     'GsfEleSCEtaMultiRangeCut',
     'MinPtCut']
vidNestedWPBitMap           = { 'fail':0, 'veto':1, 'loose':2, 'medium':3, 'tight':4 }  # Bitwise (Electron vidNestedWPBitMap ID flags (3 bits per cut), '000'=0 is fail, '001'=1 is veto, '010'=2 is loose, '011'=3 is medium, '100'=4 is tight)

def cutBasedEleBitmap( integer ):
    return [int( x, 2 ) for x in textwrap.wrap("{0:030b}".format(integer),3) ]

def cbEleSelector( quality, removeCuts = [] ):
    if quality not in vidNestedWPBitMap.keys():
        raise Exception( "Don't know about quality %r" % quality )
    if type( removeCuts ) == str:
        removeCuts = [removeCuts]

    # construct a list of thresholds the electron has to satisfy 
    thresholds = []
    for cut in removeCuts:
        if cut not in vidNestedWPBitMapNamingList:
            raise Exception( "Don't know about ele cut %r" % cut )
    for cut in vidNestedWPBitMapNamingList:
        if cut not in removeCuts: 
            thresholds.append( vidNestedWPBitMap[quality] )
        else:
            thresholds.append( 0 )

    # construct the selector
    def _selector( integer ):
        return all(map( lambda x: operator.ge(*x), zip( cutBasedEleBitmap(integer), thresholds ) ))
    return _selector

def eleSelector( lepton_selection, year, ptCut = 10):
    # tigher isolation applied on analysis level. cutBased corresponds to Fall17V2 ID for all 2016-2018.
    if lepton_selection == 'tight':
        def func(l):
            return \
                l["pt"]                 >= ptCut \
                and abs(l["eta"])       < 2.4 \
                and l['cutBased']       >= 4 \
                and l['pfRelIso03_all'] < 0.20 \
                and l["convVeto"] \
                and ord(l["lostHits"])  == 0 \
                and l["sip3d"]          < 4.0 \
                and abs(l["dxy"])       < 0.05 \
                and abs(l["dz"])        < 0.1
    elif lepton_selection == 'tightMiniIso02':
        cbEleSelector_ = cbEleSelector( 'tight', removeCuts = ['GsfEleRelPFIsoScaledCut'] )
        def func(l):
            return \
                l["pt"]                 >= ptCut \
                and abs(l["eta"])       < 2.4 \
                and cbEleSelector_(l['vidNestedWPBitmap']) \
                and l["miniPFRelIso_all"] < 0.2
    elif lepton_selection == 'tightNoIso':
        cbEleSelector_ = cbEleSelector( 'tight', removeCuts = ['GsfEleRelPFIsoScaledCut'] )
        def func(l):
            return \
                l["pt"]                 >= ptCut \
                and abs(l["eta"])       < 2.4 \
                and cbEleSelector_(l['vidNestedWPBitmap']) 
#    elif lepton_selection == 'tightNoIso':
#        def func(l):
#            return \
#                l["pt"]                 >= ptCut \
#                and abs(l["eta"])       < 2.4 \
#                and ( l['cutBased']       >= 4 or l['mvaFall17V2noIso_WP80'] )\
#                and l["convVeto"] \
#                and ord(l["lostHits"])  == 0 \
#                and l["sip3d"]          < 4.0 \
#                and abs(l["dxy"])       < 0.05 \
#                and abs(l["dz"])        < 0.1
    elif lepton_selection == 'medium':
        def func(l):
            return \
                l["pt"]                 >= ptCut \
                and abs(l["eta"])       < 2.4 \
                and l['cutBased']       >= 3 \
                and l['pfRelIso03_all'] < 0.20 \
                and l["convVeto"] \
                and ord(l["lostHits"])  == 0 \
                and l["sip3d"]          < 4.0 \
                and abs(l["dxy"])       < 0.05 \
                and abs(l["dz"])        < 0.1
    elif lepton_selection == 'loose':
        def func(l):
            return \
                l["pt"]                 >= ptCut \
                and abs(l["eta"])       < 2.4 \
                and l['cutBased']       >= 1 \
                and l['pfRelIso03_all'] < 0.20 \
                and l["convVeto"] \
                and ord(l["lostHits"])  == 0 \
                and l["sip3d"]          < 4.0 \
                and abs(l["dxy"])       < 0.05 \
                and abs(l["dz"])        < 0.1
    return func

def eleSelectorString(relIso03 = 0.2, eleId = 4, ptCut = 20, absEtaCut = 2.4, dxy = 0.05, dz = 0.1, index = "Sum", noMissingHits=True):
    idx = None if (index is None) or (type(index)==type("") and index.lower()=="sum") else index
    index_str = get_index_str( index  = idx)
    string = [\
                "Electron_pt"+index_str+">=%s" % ptCut ,
                "abs(Electron_eta"+index_str+")<%s" % absEtaCut ,
                "Electron_convVeto"+index_str+"",
                "Electron_lostHits"+index_str+"==0" if noMissingHits else "(1)",
                "Electron_sip3d"+index_str+"<4.0" ,
                "abs(Electron_dxy"+index_str+")<%s" % dxy ,
                "abs(Electron_dz"+index_str+")<%s" % dz ,
                "Electron_pfRelIso03_all"+index_str+"<%s" % relIso03 ,
                "Electron_cutBased"+index_str+">=%s"%eleId , # Fall17V2 ID
             ]

    if type(index)==type("") and index.lower()=='sum':
        return 'Sum$('+'&&'.join(string)+')'
    else:
        return '&&'.join(string)

leptonVars_data = ['eta','etaSc', 'pt','phi','dxy', 'dz','tightId', 'pdgId', 'mediumMuonId', 'miniRelIso', 'relIso03', 'sip3d', 'mvaIdSpring15', 'convVeto', 'lostHits', 'jetPtRelv2', 'jetPtRatiov2', 'eleCutId_Spring2016_25ns_v1_ConvVetoDxyDz']
leptonVars = leptonVars_data + ['mcMatchId','mcMatchAny']

electronVars_data = ['pt','eta','phi','pdgId','cutBased','miniPFRelIso_all','pfRelIso03_all','sip3d','lostHits','convVeto','dxy','dz','charge','deltaEtaSC','mvaFall17V2noIso_WP80', 'vidNestedWPBitmap']
electronVars = electronVars_data + []

muonVars_data = ['pt','eta','phi','pdgId','mediumId','miniPFRelIso_all','pfRelIso03_all','sip3d','dxy','dz','charge']
muonVars = muonVars_data + []

def getLeptons(c, collVars=leptonVars):
    return [getObjDict(c, 'LepGood_', collVars, i) for i in range(int(getVarValue(c, 'nLepGood')))]

def getMuons(c, collVars=muonVars):
    return [getObjDict(c, 'Muon_', collVars, i) for i in range(int(getVarValue(c, 'nMuon')))]
def getElectrons(c, collVars=electronVars):
    return [getObjDict(c, 'Electron_', collVars, i) for i in range(int(getVarValue(c, 'nElectron')))]

def getGoodMuons(c, collVars=muonVars, mu_selector = alwaysFalse):
    return [l for l in getMuons(c, collVars) if mu_selector(l)]

def getGoodElectrons(c, collVars=electronVars, ele_selector = alwaysFalse):
    return [l for l in getElectrons(c, collVars) if ele_selector(l)]


tauVars=['eta','pt','phi','pdgId','charge', 'dxy', 'dz', 'idDecayModeNewDMs', 'idCI3hit', 'idAntiMu','idAntiE','mcMatchId']

def getTaus(c, collVars=tauVars):
    return [getObjDict(c, 'TauGood_', collVars, i) for i in range(int(getVarValue(c, 'nTauGood')))]

def looseTauID(l, ptCut=20, absEtaCut=2.4):
    return \
        l["pt"]>=ptCut\
        and abs(l["eta"])<absEtaCut\
        and l["idDecayModeNewDMs"]>=1\
        and l["idCI3hit"]>=1\
        and l["idAntiMu"]>=1\
        and l["idAntiE"]>=1\

def getGoodTaus(c, collVars=tauVars):
    return [l for l in getTaus(c,collVars=collVars) if looseTauID(l)]

idCutBased={'loose':0 ,'medium':1, 'tight':2}
photonVars=['eta','pt','phi','mass','cutBased']
photonVarsMC = photonVars + ['mcPt']

def getPhotons(c, collVars=None, idLevel='loose', year=2016):
    if collVars is None:
        collVars = ['eta','pt','phi','mass','cutBased'] if (not (year == 2017 or year == 2018)) else ['eta','pt','phi','mass','cutBasedBitmap']
    return [getObjDict(c, 'Photon_', collVars, i) for i in range(int(getVarValue(c, 'nPhoton')))]

def getGoodPhotons(c, ptCut=50, idLevel="loose", isData=True, collVars=None, year=2016):
    idVar = "cutBased" if (not (year == 2017 or year == 2018)) else "cutBasedBitmap"
    #if collVars is None: collVars = photonVars if isData else photonVarsMC
    collVars = ['eta','pt','phi','mass','cutBased'] if (not (year == 2017 or year == 2018)) else ['eta','pt','phi','mass','cutBasedBitmap']
    return [p for p in getPhotons(c, collVars) if p[idVar] > idCutBased[idLevel] and p['pt'] > ptCut ] # > 2 is tight for 2016, 2017 and 2018


def genPhotonSelector( photon_selection=None ):
    # According to AN-2017/197
    if photon_selection == 'overlapTTGamma':
        # Remove events from ttbar sample, keep ttgamma events
        def func(g):
            if g["pt"]       <= 13:  return False
            if abs(g["eta"]) >= 3.0: return False
            return True
        return func

    elif photon_selection == 'overlapZWGamma':
        # Remove events from DY and W+jets sample, keep Zgamma and Wgamma events
        def func(g):
            if g["pt"]       <= 15:  return False
            if abs(g["eta"]) >= 2.6: return False
            return True
        return func

    elif photon_selection == 'overlapSingleTopTch':
        # Remove events from single top t-channel sample, keep single top + photon events
        def func(g):
            if g["pt"]       <= 10:  return False
            if abs(g["eta"]) >= 2.6: return False
            return True
        return func

    else:
        # general gen-photon selection
        def func(g):
            if g["pt"]       <= 13:    return False
            if abs(g["eta"]) >= 1.479: return False
            return True
        return func
