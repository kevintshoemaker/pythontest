import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt


# Create a DataFrame with random data
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))
print(df)


