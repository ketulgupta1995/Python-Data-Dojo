import pandas as pd
import numpy as np
%matplotlib inline
import os

trains=pd.read_csv("isl_wise_train_detail_03082015_v1.csv")
train_no =trains.groupby('Train No.')

train_no.head()
train_no.size()
train_no.size().max()
type(train_no.size())

