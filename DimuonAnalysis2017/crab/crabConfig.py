from CRABClient.UserUtilities import config
config = config()

from DileptonAnalysis.AnalysisStep.samples.Samples import samples

import os
dset = os.getcwd().replace(os.path.dirname(os.getcwd())+'/', '')

print 'Submitting jobs for dataset ' + samples[dset][0]

params = samples[dset][1]
print 'Config parameters for sample',
print dset + ' :',
print params

config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = '../../test/scout_cfg.py'

config.JobType.pyCfgParams = params
config.Data.inputDataset   = samples[dset][0]
config.Data.splitting      = samples[dset][2]
config.Data.unitsPerJob    = samples[dset][4]
if samples[dset][3] != '' :
    config.Data.lumiMask   = samples[dset][3]

if config.Data.inputDataset.find('USER', len(config.Data.inputDataset)-4, len(config.Data.inputDataset)) != -1 and config.Data.inputDataset.find('avartak', 0, len(config.Data.inputDataset)) != -1 :
    config.Data.inputDBS   = 'phys03'
    print 'Dataset on phys03'

config.Site.storageSite    = 'T2_US_UCSD'

