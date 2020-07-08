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
setup = pd.options.display.max_columns = 999

#functions
def check_null(X):
  return X.isnull().sum()
def explore(X):
  return X.describe(include='all')