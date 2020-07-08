#!/usr/bin/env python
"""
lambdata - a collection of Data Science helper functions
"""

import pandas as pd
import numpy as np
from . import example_module


#module
TEST = pd.DataFrame(np.ones(10))
Y = example_module.increment(example_module.x)
# ER: Below was causing an error for me, don't see it being used anywhere
#setup = pd.set_option.display.max_columns = 999

# ER: these functions are not getting called anywhere in the code above, are they supposed to be in the module?
#functions
def check_null(X):
  return X.isnull().sum()
def explore(X):
  return X.describe(include='all')