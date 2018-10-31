# Data Transformation Project

#### Objective
To transform categorical data to facilitate visualization and cluster analysis using k-modes clustering algorithm.

#### Method
Preprocess categorical variables using scikit-learn's LabelEncoder and merge transformed variables into existing dataset. Transform LabelEncoded nominal variables into one-hot numeric arrays using scikit-learn's OneHotEncoder.

#### Datasource
Proprietary survey, n = 1,200

Variables for transformation: 
- Ordinal variables: var12, var230, var231, var232, var233
- Nominal variables: var9, var11, var13, var16, var217, var234, var235, var236, var246
