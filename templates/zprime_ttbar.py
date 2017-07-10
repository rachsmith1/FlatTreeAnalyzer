import ROOT
import collections

### variable list
variables = {
    "tau32_1":{"name":"tau32_1","title":"#tau_{3,2}","bin":50,"xmin":0.0,"xmax":1.0},
    "softDroppedJet1_m":{"name":"softDroppedJet1_m","title":"Soft Dropped Mass","bin":50,"xmin":0.0,"xmax":1000.0},
    "zPrimeReconstructedMass":{"name":"zPrimeReconstructedMass","title":"Z' Reconstructed Mass (Ungroomed)","bin":50,"xmin":0.0,"xmax":50000.0},
    "zPrimeReconstructedMass_softDropped":{"name":"zPrimeReconstructedMass_softDropped","title":"Z' Reconstructed Mass (Soft Dropped)","bin":50,"xmin":0.0,"xmax":50000.0},
}

colors = {}
colors['m_{Z} = 5 TeV'] = ROOT.kBlue
colors['m_{Z} = 10 TeV'] = ROOT.kBlue
colors['m_{Z} = 15 TeV'] = ROOT.kBlue
colors['m_{Z} = 20 TeV'] = ROOT.kBlue
colors['m_{Z} = 25 TeV'] = ROOT.kBlue
colors['m_{Z} = 30 TeV'] = ROOT.kBlue
colors['m_{Z} = 35 TeV'] = ROOT.kBlue
colors['m_{Z} = 40 TeV'] = ROOT.kBlue
colors['QCD'] = ROOT.kYellow
colors['tt'] = ROOT.kRed

signal_groups = collections.OrderedDict()
signal_groups['m_{Z} = 5 TeV'] = ['pp_Zprime_5TeV_ttbar']
signal_groups['m_{Z} = 10 TeV'] = ['pp_Zprime_10TeV_ttbar']
signal_groups['m_{Z} = 15 TeV'] = ['pp_Zprime_15TeV_ttbar']
signal_groups['m_{Z} = 20 TeV'] = ['pp_Zprime_20TeV_ttbar']
signal_groups['m_{Z} = 25 TeV'] = ['pp_Zprime_25TeV_ttbar']
signal_groups['m_{Z} = 30 TeV'] = ['pp_Zprime_30TeV_ttbar']
signal_groups['m_{Z} = 35 TeV'] = ['pp_Zprime_35TeV_ttbar']
signal_groups['m_{Z} = 40 TeV'] = ['pp_Zprime_40TeV_ttbar']

background_groups = collections.OrderedDict()
background_groups['tt']  = [	
				'pp_tt012j_5f_HT_0_600',
				'pp_tt012j_5f_HT_600_1200',
				'pp_tt012j_5f_HT_1200_2100',
				'pp_tt012j_5f_HT_2100_3400',
				'pp_tt012j_5f_HT_3400_5300',
				'pp_tt012j_5f_HT_5300_8100',
				'pp_tt012j_5f_HT_8100_15000',
				'pp_tt012j_5f_HT_15000_25000',
				'pp_tt012j_5f_HT_25000_35000',
				'pp_tt012j_5f_HT_35000_100000',
			   ]

background_groups['QCD'] = [
                                'pp_jj012j_5f_HT_0_500',
                                'pp_jj012j_5f_HT_500_1000',
                                'pp_jj012j_5f_HT_1000_2000',
                                'pp_jj012j_5f_HT_2000_4000',
                                'pp_jj012j_5f_HT_4000_7200',
                                'pp_jj012j_5f_HT_7200_15000',
                                'pp_jj012j_5f_HT_15000_25000',
                                'pp_jj012j_5f_HT_25000_35000',
                                'pp_jj012j_5f_HT_35000_100000',
                           ]

# global parameters
intLumi = 3.0e+07
delphesVersion = '3.4.2'

uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.02, 0.0])
uncertainties.append([0.02, 0.02])
uncertainties.append([0.02, 0.10])

# the first time needs to be set to True
runFull = True

# base pre-#selections
selbase = 'Jet1_pt > 500. && Jet2_pt > 300. && abs(Jet1_eta) < 2.4 && abs(Jet2_eta) < 2.4'

# add mass-dependent list of event #selections here if needed...

selections = collections.OrderedDict()
selections['m_{Z} = 5 TeV'] = []
selections['m_{Z} = 5 TeV'].append(selbase + ' && tau32_1 < 0.74 && tau32_2 < 0.74 && softDroppedJet1_m < 210. && softDroppedJet1_m > 110. && softDroppedJet2_m < 210. && softDroppedJet2_m > 110. && 5*1000/Jet1_pt > 1.5 && 5*1000/Jet1_pt < 7.5 && 5*1000/Jet2_pt > 1.5 && 5*1000/Jet2_pt < 10')

selections['m_{Z} = 10 TeV'] = []
selections['m_{Z} = 10 TeV'].append(selbase + ' && tau32_1 < 0.74 && tau32_2 < 0.74 && softDroppedJet1_m < 210. && softDroppedJet1_m > 110. && softDroppedJet2_m < 210. && softDroppedJet2_m > 110. && 10*1000/Jet1_pt > 1.5 && 10*1000/Jet1_pt < 7.5 && 10*1000/Jet2_pt > 1.5 && 10*1000/Jet2_pt < 10')

selections['m_{Z} = 15 TeV'] = []
selections['m_{Z} = 15 TeV'].append(selbase + ' && tau32_1 < 0.74 && tau32_2 < 0.74 && softDroppedJet1_m < 210. && softDroppedJet1_m > 110. && softDroppedJet2_m < 210. && softDroppedJet2_m > 110. && 15*1000/Jet1_pt > 1.5 && 15*1000/Jet1_pt < 7.5 && 15*1000/Jet2_pt > 1.5 && 15*1000/Jet2_pt < 10')

selections['m_{Z} = 20 TeV'] = []
selections['m_{Z} = 20 TeV'].append(selbase + ' && tau32_1 < 0.74 && tau32_2 < 0.74 && softDroppedJet1_m < 210. && softDroppedJet1_m > 110. && softDroppedJet2_m < 210. && softDroppedJet2_m > 110. && 20*1000/Jet1_pt > 1.5 && 20*1000/Jet1_pt < 7.5 && 20*1000/Jet2_pt > 1.5 && 20*1000/Jet2_pt < 10')

selections['m_{Z} = 25 TeV'] = []
selections['m_{Z} = 25 TeV'].append(selbase + ' && tau32_1 < 0.74 && tau32_2 < 0.74 && softDroppedJet1_m < 210. && softDroppedJet1_m > 110. && softDroppedJet2_m < 210. && softDroppedJet2_m > 110. && 25*1000/Jet1_pt > 1.5 && 25*1000/Jet1_pt < 7.5 && 25*1000/Jet2_pt > 1.5 && 25*1000/Jet2_pt < 10')

selections['m_{Z} = 30 TeV'] = []
selections['m_{Z} = 30 TeV'].append(selbase + ' && tau32_1 < 0.74 && tau32_2 < 0.74 && softDroppedJet1_m < 210. && softDroppedJet1_m > 110. && softDroppedJet2_m < 210. && softDroppedJet2_m > 110. && 30*1000/Jet1_pt > 1.5 && 30*1000/Jet1_pt < 7.5 && 30*1000/Jet2_pt > 1.5 && 30*1000/Jet2_pt < 10')

selections['m_{Z} = 35 TeV'] = []
selections['m_{Z} = 35 TeV'].append(selbase + ' && tau32_1 < 0.74 && tau32_2 < 0.74 && softDroppedJet1_m < 210. && softDroppedJet1_m > 110. && softDroppedJet2_m < 210. && softDroppedJet2_m > 110. && 35*1000/Jet1_pt > 1.5 && 35*1000/Jet1_pt < 7.5 && 35*1000/Jet2_pt > 1.5 && 35*1000/Jet2_pt < 10')

selections['m_{Z} = 40 TeV'] = []
selections['m_{Z} = 40 TeV'].append(selbase + ' && tau32_1 < 0.74 && tau32_2 < 0.74 && softDroppedJet1_m < 210. && softDroppedJet1_m > 110. && softDroppedJet2_m < 210. && softDroppedJet2_m > 110. && 40*1000/Jet1_pt > 1.5 && 40*1000/Jet1_pt < 7.5 && 40*1000/Jet2_pt > 1.5 && 40*1000/Jet2_pt < 10')




