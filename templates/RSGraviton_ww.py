import ROOT
import collections

### variable list
variables = {
    'Jet1_tau32':{'name':'Jet1_tau32','title':'#tau_{3,2}','bin':50,'xmin':0.0,'xmax':1.0},
    'softDroppedJet1_m':{'name':'softDroppedJet1_m','title':'Soft Dropped Mass','bin':50,'xmin':0.0,'xmax':1000.0},
    'RSGravitonReconstructedMass':{'name':'RSGravitonReconstructedMass','title':'RSG Reconstructed Mass (Ungroomed)','bin':50,'xmin':0.0,'xmax':50000.0},
}

colors = {}
colors['m_{RSG} = 5 TeV'] = ROOT.kBlue
colors['m_{RSG} = 10 TeV'] = ROOT.kBlue
colors['m_{RSG} = 15 TeV'] = ROOT.kBlue
colors['m_{RSG} = 20 TeV'] = ROOT.kBlue
colors['m_{RSG} = 25 TeV'] = ROOT.kBlue
colors['m_{RSG} = 30 TeV'] = ROOT.kBlue
colors['m_{RSG} = 35 TeV'] = ROOT.kBlue
colors['m_{RSG} = 40 TeV'] = ROOT.kBlue
colors['QCD'] = ROOT.kYellow
colors['VV'] = ROOT.kOrange
colors['tt'] = ROOT.kRed

signal_groups = collections.OrderedDict()
signal_groups['m_{RSG} = 2 TeV']  = ['pp_RSGraviton_2TeV_ww']
signal_groups['m_{RSG} = 5 TeV']  = ['pp_RSGraviton_5TeV_ww']
signal_groups['m_{RSG} = 10 TeV'] = ['pp_RSGraviton_10TeV_ww']
signal_groups['m_{RSG} = 15 TeV'] = ['pp_RSGraviton_15TeV_ww']
signal_groups['m_{RSG} = 20 TeV'] = ['pp_RSGraviton_20TeV_ww']
signal_groups['m_{RSG} = 25 TeV'] = ['pp_RSGraviton_25TeV_ww']
signal_groups['m_{RSG} = 30 TeV'] = ['pp_RSGraviton_30TeV_ww']
signal_groups['m_{RSG} = 35 TeV'] = ['pp_RSGraviton_35TeV_ww']
signal_groups['m_{RSG} = 40 TeV'] = ['pp_RSGraviton_40TeV_ww']

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

background_groups['VV']  = [
				'pp_vv012j_4f_HT_0_300',
                                'pp_vv012j_4f_HT_300_1400',
                                'pp_vv012j_4f_HT_1400_2900',
                                'pp_vv012j_4f_HT_2900_5300',
                                'pp_vv012j_4f_HT_5300_8800',
                                'pp_vv012j_4f_HT_8800_15000',
                                'pp_vv012j_4f_HT_15000_25000',
                                'pp_vv012j_4f_HT_25000_35000',
                                #'pp_vv012j_4f_HT_35000_100000',
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

selections['m_{RSG} = 10 TeV'] = []
selections['m_{RSG} = 10 TeV'].append(selbase)




