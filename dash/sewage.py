import pandas as pd
import os

path_parent = os.path.dirname(os.getcwd())
# os.chdir(path_parent)
yearIndex = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

amphetamine_2011 = pd.read_csv(path_parent + '/sewerdata/emcdda/amphetamine/WW-data-amphetamine-2011.csv', delimiter=',')
amphetamine_2012 = pd.read_csv(path_parent + '/sewerdata/emcdda/amphetamine/WW-data-amphetamine-2012.csv', delimiter=',')
amphetamine_2013 = pd.read_csv(path_parent + '/sewerdata/emcdda/amphetamine/WW-data-amphetamine-2013.csv', delimiter=',')
amphetamine_2014 = pd.read_csv(path_parent + '/sewerdata/emcdda/amphetamine/WW-data-amphetamine-2014.csv', delimiter=',')
amphetamine_2015 = pd.read_csv(path_parent + '/sewerdata/emcdda/amphetamine/WW-data-amphetamine-2015.csv', delimiter=',')
amphetamine_2016 = pd.read_csv(path_parent + '/sewerdata/emcdda/amphetamine/WW-data-amphetamine-2016.csv', delimiter=',')
amphetamine_2017 = pd.read_csv(path_parent + '/sewerdata/emcdda/amphetamine/WW-data-amphetamine-2017.csv', delimiter=',')
amphetamine_2018 = pd.read_csv(path_parent + '/sewerdata/emcdda/amphetamine/WW-data-amphetamine-2018.csv', delimiter=',')
amphetamine_2019 = pd.read_csv(path_parent + '/sewerdata/emcdda/amphetamine/WW-data-amphetamine-2019.csv', delimiter=',')
amphetamine_2020 = pd.read_csv(path_parent + '/sewerdata/emcdda/amphetamine/WW-data-amphetamine-2020.csv', delimiter=',')

amphetamine_2011_NL_daily = amphetamine_2011[amphetamine_2011['country'] == "NL"][['Daily mean']]
amphetamine_2011_NL_daily_mean = amphetamine_2011_NL_daily.mean().iloc[0]

amphetamine_2012_NL_daily = amphetamine_2012[amphetamine_2012['country'] == "NL"][['Daily mean']]
amphetamine_2012_NL_daily_mean = amphetamine_2012_NL_daily.mean().iloc[0]

amphetamine_2013_NL_daily = amphetamine_2013[amphetamine_2013['country'] == "NL"][['Daily mean']]
amphetamine_2013_NL_daily_mean = amphetamine_2013_NL_daily.mean().iloc[0]

amphetamine_2014_NL_daily = amphetamine_2014[amphetamine_2014['country'] == "NL"][['Daily mean']]
amphetamine_2014_NL_daily_mean = amphetamine_2014_NL_daily.mean().iloc[0]

amphetamine_2015_NL_daily = amphetamine_2015[amphetamine_2015['country'] == "NL"][['Daily mean']]
amphetamine_2015_NL_daily_mean = amphetamine_2015_NL_daily.mean().iloc[0]

amphetamine_2016_NL_daily = amphetamine_2016[amphetamine_2016['country'] == "NL"][['Daily mean']]
amphetamine_2016_NL_daily_mean = amphetamine_2016_NL_daily.mean().iloc[0]

amphetamine_2017_NL_daily = amphetamine_2017[amphetamine_2017['country'] == "NL"][['Daily mean']]
amphetamine_2017_NL_daily_mean = amphetamine_2017_NL_daily.mean().iloc[0]

amphetamine_2018_NL_daily = amphetamine_2018[amphetamine_2018['country'] == "NL"][['Daily mean']]
amphetamine_2018_NL_daily_mean = amphetamine_2018_NL_daily.mean().iloc[0]

amphetamine_2019_NL_daily = amphetamine_2019[amphetamine_2019['country'] == "NL"][['Daily mean']]
amphetamine_2019_NL_daily_mean = amphetamine_2019_NL_daily.mean().iloc[0]

amphetamine_2020_NL_daily = amphetamine_2020[amphetamine_2020['country'] == "NL"][['Daily mean']]
amphetamine_2020_NL_daily_mean = amphetamine_2020_NL_daily.mean().iloc[0]

amphetamine_series = pd.Series([amphetamine_2011_NL_daily_mean, amphetamine_2012_NL_daily_mean, amphetamine_2013_NL_daily_mean, amphetamine_2014_NL_daily_mean, amphetamine_2015_NL_daily_mean, amphetamine_2016_NL_daily_mean, amphetamine_2017_NL_daily_mean, amphetamine_2018_NL_daily_mean, amphetamine_2019_NL_daily_mean, amphetamine_2020_NL_daily_mean])
amphetamine_series.index = yearIndex


methamphetamine_2011 = pd.read_csv(path_parent + '/sewerdata/emcdda/methamphetamine/WW-data-methamphetamine-2011.csv', delimiter=',')
methamphetamine_2012 = pd.read_csv(path_parent + '/sewerdata/emcdda/methamphetamine/WW-data-methamphetamine-2012.csv', delimiter=',')
methamphetamine_2013 = pd.read_csv(path_parent + '/sewerdata/emcdda/methamphetamine/WW-data-methamphetamine-2013.csv', delimiter=',')
methamphetamine_2014 = pd.read_csv(path_parent + '/sewerdata/emcdda/methamphetamine/WW-data-methamphetamine-2014.csv', delimiter=',')
methamphetamine_2015 = pd.read_csv(path_parent + '/sewerdata/emcdda/methamphetamine/WW-data-methamphetamine-2015.csv', delimiter=',')
methamphetamine_2016 = pd.read_csv(path_parent + '/sewerdata/emcdda/methamphetamine/WW-data-methamphetamine-2016.csv', delimiter=',')
methamphetamine_2017 = pd.read_csv(path_parent + '/sewerdata/emcdda/methamphetamine/WW-data-methamphetamine-2017.csv', delimiter=',')
methamphetamine_2018 = pd.read_csv(path_parent + '/sewerdata/emcdda/methamphetamine/WW-data-methamphetamine-2018.csv', delimiter=',')
methamphetamine_2019 = pd.read_csv(path_parent + '/sewerdata/emcdda/methamphetamine/WW-data-methamphetamine-2019.csv', delimiter=',')
methamphetamine_2020 = pd.read_csv(path_parent + '/sewerdata/emcdda/methamphetamine/WW-data-methamphetamine-2020.csv', delimiter=',')

methamphetamine_2011_NL_daily = methamphetamine_2011[methamphetamine_2011['country'] == "NL"][['methamphetamineMean2011']]
methamphetamine_2011_NL_daily_mean = methamphetamine_2011_NL_daily.mean().iloc[0]

methamphetamine_2012_NL_daily = methamphetamine_2012[methamphetamine_2012['country'] == "NL"][['Daily mean']]
methamphetamine_2012_NL_daily_mean = methamphetamine_2012_NL_daily.mean().iloc[0]

methamphetamine_2013_NL_daily = methamphetamine_2013[methamphetamine_2013['country'] == "NL"][['Daily mean']]
methamphetamine_2013_NL_daily_mean = methamphetamine_2013_NL_daily.mean().iloc[0]

methamphetamine_2014_NL_daily = methamphetamine_2014[methamphetamine_2014['country'] == "NL"][['Daily mean']]
methamphetamine_2014_NL_daily_mean = methamphetamine_2014_NL_daily.mean().iloc[0]

methamphetamine_2015_NL_daily = methamphetamine_2015[methamphetamine_2015['country'] == "NL"][['Daily mean']]
methamphetamine_2015_NL_daily_mean = methamphetamine_2015_NL_daily.mean().iloc[0]

methamphetamine_2016_NL_daily = methamphetamine_2016[methamphetamine_2016['country'] == "NL"][['Daily mean']]
methamphetamine_2016_NL_daily_mean = methamphetamine_2016_NL_daily.mean().iloc[0]

methamphetamine_2017_NL_daily = methamphetamine_2017[methamphetamine_2017['country'] == "NL"][['Daily mean']]
methamphetamine_2017_NL_daily_mean = methamphetamine_2017_NL_daily.mean().iloc[0]

methamphetamine_2018_NL_daily = methamphetamine_2018[methamphetamine_2018['country'] == "NL"][['Daily mean']]
methamphetamine_2018_NL_daily_mean = methamphetamine_2018_NL_daily.mean().iloc[0]

methamphetamine_2019_NL_daily = methamphetamine_2019[methamphetamine_2019['country'] == "NL"][['Daily mean']]
methamphetamine_2019_NL_daily_mean = methamphetamine_2019_NL_daily.mean().iloc[0]

methamphetamine_2020_NL_daily = methamphetamine_2020[methamphetamine_2020['country'] == "NL"][['Daily mean']]
methamphetamine_2020_NL_daily_mean = methamphetamine_2020_NL_daily.mean().iloc[0]

methamphetamine_series = pd.Series([methamphetamine_2011_NL_daily_mean, methamphetamine_2012_NL_daily_mean, methamphetamine_2013_NL_daily_mean, methamphetamine_2014_NL_daily_mean, methamphetamine_2015_NL_daily_mean, methamphetamine_2016_NL_daily_mean, methamphetamine_2017_NL_daily_mean, methamphetamine_2018_NL_daily_mean, methamphetamine_2019_NL_daily_mean, methamphetamine_2020_NL_daily_mean])
methamphetamine_series.index = yearIndex


MDMA_2011 = pd.read_csv(path_parent + '/sewerdata/emcdda/MDMA/WW-data-MDMA-2011.csv', delimiter=',')
MDMA_2012 = pd.read_csv(path_parent + '/sewerdata/emcdda/MDMA/WW-data-MDMA-2012.csv', delimiter=',')
MDMA_2013 = pd.read_csv(path_parent + '/sewerdata/emcdda/MDMA/WW-data-MDMA-2013.csv', delimiter=',')
MDMA_2014 = pd.read_csv(path_parent + '/sewerdata/emcdda/MDMA/WW-data-MDMA-2014.csv', delimiter=',')
MDMA_2015 = pd.read_csv(path_parent + '/sewerdata/emcdda/MDMA/WW-data-MDMA-2015.csv', delimiter=',')
MDMA_2016 = pd.read_csv(path_parent + '/sewerdata/emcdda/MDMA/WW-data-MDMA-2016.csv', delimiter=',')
MDMA_2017 = pd.read_csv(path_parent + '/sewerdata/emcdda/MDMA/WW-data-MDMA-2017.csv', delimiter=',')
MDMA_2018 = pd.read_csv(path_parent + '/sewerdata/emcdda/MDMA/WW-data-MDMA-2018.csv', delimiter=',')
MDMA_2019 = pd.read_csv(path_parent + '/sewerdata/emcdda/MDMA/WW-data-MDMA-2019.csv', delimiter=',')
MDMA_2020 = pd.read_csv(path_parent + '/sewerdata/emcdda/MDMA/WW-data-MDMA-2020.csv', delimiter=',')

MDMA_2011_NL_daily = MDMA_2011[MDMA_2011['country'] == "NL"][['Daily mean']]
MDMA_2011_NL_daily_mean = MDMA_2011_NL_daily.mean().iloc[0]

MDMA_2012_NL_daily = MDMA_2012[MDMA_2012['country'] == "NL"][['Daily mean']]
MDMA_2012_NL_daily_mean = MDMA_2012_NL_daily.mean().iloc[0]

MDMA_2013_NL_daily = MDMA_2013[MDMA_2013['country'] == "NL"][['Daily mean']]
MDMA_2013_NL_daily_mean = MDMA_2013_NL_daily.mean().iloc[0]

MDMA_2014_NL_daily = MDMA_2014[MDMA_2014['country'] == "NL"][['Daily mean']]
MDMA_2014_NL_daily_mean = MDMA_2014_NL_daily.mean().iloc[0]

MDMA_2015_NL_daily = MDMA_2015[MDMA_2015['country'] == "NL"][['Daily mean']]
MDMA_2015_NL_daily_mean = MDMA_2015_NL_daily.mean().iloc[0]

MDMA_2016_NL_daily = MDMA_2016[MDMA_2016['country'] == "NL"][['Daily mean']]
MDMA_2016_NL_daily_mean = MDMA_2016_NL_daily.mean().iloc[0]

MDMA_2017_NL_daily = MDMA_2017[MDMA_2017['country'] == "NL"][['Daily mean']]
MDMA_2017_NL_daily_mean = MDMA_2017_NL_daily.mean().iloc[0]

MDMA_2018_NL_daily = MDMA_2018[MDMA_2018['country'] == "NL"][['Daily mean']]
MDMA_2018_NL_daily_mean = MDMA_2018_NL_daily.mean().iloc[0]

MDMA_2019_NL_daily = MDMA_2019[MDMA_2019['country'] == "NL"][['Daily mean']]
MDMA_2019_NL_daily_mean = MDMA_2019_NL_daily.mean().iloc[0]

MDMA_2020_NL_daily = MDMA_2020[MDMA_2020['country'] == "NL"][['Daily mean']]
MDMA_2020_NL_daily_mean = MDMA_2020_NL_daily.mean().iloc[0]

MDMA_series = pd.Series([MDMA_2011_NL_daily_mean, MDMA_2012_NL_daily_mean, MDMA_2013_NL_daily_mean, MDMA_2014_NL_daily_mean, MDMA_2015_NL_daily_mean, MDMA_2016_NL_daily_mean, MDMA_2017_NL_daily_mean, MDMA_2018_NL_daily_mean, MDMA_2019_NL_daily_mean, MDMA_2020_NL_daily_mean])
MDMA_series.index = yearIndex

cocaine_2011 = pd.read_csv(path_parent + '/sewerdata/emcdda/cocaine/WW-data-cocaine-2011.csv', delimiter=',')
cocaine_2012 = pd.read_csv(path_parent + '/sewerdata/emcdda/cocaine/WW-data-cocaine-2012.csv', delimiter=',')
cocaine_2013 = pd.read_csv(path_parent + '/sewerdata/emcdda/cocaine/WW-data-cocaine-2013.csv', delimiter=',')
cocaine_2014 = pd.read_csv(path_parent + '/sewerdata/emcdda/cocaine/WW-data-cocaine-2014.csv', delimiter=',')
cocaine_2015 = pd.read_csv(path_parent + '/sewerdata/emcdda/cocaine/WW-data-cocaine-2015.csv', delimiter=',')
cocaine_2016 = pd.read_csv(path_parent + '/sewerdata/emcdda/cocaine/WW-data-cocaine-2016.csv', delimiter=',')
cocaine_2017 = pd.read_csv(path_parent + '/sewerdata/emcdda/cocaine/WW-data-cocaine-2017.csv', delimiter=',')
cocaine_2018 = pd.read_csv(path_parent + '/sewerdata/emcdda/cocaine/WW-data-cocaine-2018.csv', delimiter=',')
cocaine_2019 = pd.read_csv(path_parent + '/sewerdata/emcdda/cocaine/WW-data-cocaine-2019.csv', delimiter=',')
cocaine_2020 = pd.read_csv(path_parent + '/sewerdata/emcdda/cocaine/WW-data-cocaine-2020.csv', delimiter=',')

cocaine_2011_NL_daily = cocaine_2011[cocaine_2011['country'] == "NL"][['Daily mean']]
cocaine_2011_NL_daily_mean = cocaine_2011_NL_daily.mean().iloc[0]

cocaine_2012_NL_daily = cocaine_2012[cocaine_2012['country'] == "NL"][['Daily mean']]
cocaine_2012_NL_daily_mean = cocaine_2012_NL_daily.mean().iloc[0]

cocaine_2013_NL_daily = cocaine_2013[cocaine_2013['country'] == "NL"][['Daily mean']]
cocaine_2013_NL_daily_mean = cocaine_2013_NL_daily.mean().iloc[0]

cocaine_2014_NL_daily = cocaine_2014[cocaine_2014['country'] == "NL"][['Daily mean']]
cocaine_2014_NL_daily_mean = cocaine_2014_NL_daily.mean().iloc[0]

cocaine_2015_NL_daily = cocaine_2015[cocaine_2015['country'] == "NL"][['Daily mean']]
cocaine_2015_NL_daily_mean = cocaine_2015_NL_daily.mean().iloc[0]

cocaine_2016_NL_daily = cocaine_2016[cocaine_2016['country'] == "NL"][['Daily mean']]
cocaine_2016_NL_daily_mean = cocaine_2016_NL_daily.mean().iloc[0]

cocaine_2017_NL_daily = cocaine_2017[cocaine_2017['country'] == "NL"][['Daily mean']]
cocaine_2017_NL_daily_mean = cocaine_2017_NL_daily.mean().iloc[0]

cocaine_2018_NL_daily = cocaine_2018[cocaine_2018['country'] == "NL"][['Daily mean']]
cocaine_2018_NL_daily_mean = cocaine_2018_NL_daily.mean().iloc[0]

cocaine_2019_NL_daily = cocaine_2019[cocaine_2019['country'] == "NL"][['Daily mean']]
cocaine_2019_NL_daily_mean = cocaine_2019_NL_daily.mean().iloc[0]

cocaine_2020_NL_daily = cocaine_2020[cocaine_2020['country'] == "NL"][['Daily mean']]
cocaine_2020_NL_daily_mean = cocaine_2020_NL_daily.mean().iloc[0]

cocaine_series = pd.Series([cocaine_2011_NL_daily_mean, cocaine_2012_NL_daily_mean, cocaine_2013_NL_daily_mean, cocaine_2014_NL_daily_mean, cocaine_2015_NL_daily_mean, cocaine_2016_NL_daily_mean, cocaine_2017_NL_daily_mean, cocaine_2018_NL_daily_mean, cocaine_2019_NL_daily_mean, cocaine_2020_NL_daily_mean])
cocaine_series.index = yearIndex


amphetamine_series.index = pd.to_datetime(amphetamine_series.index)
methamphetamine_series.index = pd.to_datetime(methamphetamine_series.index)
MDMA_series.index = pd.to_datetime(MDMA_series.index)
cocaine_series.index = pd.to_datetime(cocaine_series.index)