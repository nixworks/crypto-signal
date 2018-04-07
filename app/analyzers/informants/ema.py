""" EMA Indicator
"""

import math

import pandas
from talib import abstract

from analyzers.utils import IndicatorUtils


class EMA(IndicatorUtils):
    def analyze(self, historical_data, period_count=15):
        """Performs an EMA analysis on the historical data

		Args:
			historical_data (list): A matrix of historical OHCLV data.
			period_count (int, optional): Defaults to 15. The number of data points to consider for
				our exponential moving average.

		Returns:
			dict: A dictionary containing a tuple of indicator values and booleans for buy / sell
				indication.
		"""

        dataframe = self.convert_to_dataframe(historical_data)
        ema_values = abstract.EMA(dataframe, period_count)
        ema_values.dropna(how='all', inplace=True)

        return ema_values