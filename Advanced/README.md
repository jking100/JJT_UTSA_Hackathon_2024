The PDP data does not include any information on county in its pesticide testing observations. While it is very easy to extract the collection state from the first two characters of sample ID, it is much more difficult to infer the county from this data alone. However, one crucial clue lies in the commodity column, which tells us which crop was tested for pesticides.

We do have county data in the form of Agricultural Census Data since 1840. We wondered if this data could be harnessed to make inferences about the county of origin in the PDP data set. That is, could we use the historical proportions of crops grown by county to make a statistical guess about which specific county a particular crop being tested for pesticides may have originated?

We tested this idea on the Agricultural Census data from Texas. We filtered out animal data and used only data from 1992 and later, since the earliest available PDP analyses are from 1994. We then grouped data across 4 censuses to calculate the average proportion of the county area being used to grow each crop (1992-2017), and adjusted this likelihood by county size.

Next, we created a function that creates a sampling distribution for a given crop based on the relative likelihoods among all counties. The likelihoods are normalized and then sampled with replacement to create a sampling distribution. A second function bootstraps this process, repeating it a user-specified number of times and aggregating a list of counties by frequency of appearing in sampling distributions. In this way, we can generate a probabilistic list of where a crop may have been grown while still retaining uncertainty.

However, this does not solve the county inference problem. The number of crops tested in the PDP far exceeds the number of crops in the census file. More complete commodity information in the census file could inform county inferences in the PDP data set via likelihoods by crop, but even then, imputation still comes with heavy caveats.

Relevant data files for this track: /Provided_data/USDA_PDP_AnalyticalResults.csv, /Provided_data/AgChange/*
