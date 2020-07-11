"""
pdlog.accessor
~~~~~~~~~~~~~~

.. note::

   The ``pdlog.accessor`` module is copied directly from the following
   GitHub repository: https://github.com/DataProphet/pdlog

   * The ``pdlog`` version copied here is ``pdlog==0.1.0.post0``
   * I make not claims of authorship for this submodule
   * Instead, I have copied this module in order to more
   deeply investigate the methods used in the ``pdlog`` package.
"""
from typing import Any

import pandas as pd

from . import logging


@pd.api.extensions.register_dataframe_accessor("log")
class LogAccessor:
    def __init__(self, data: pd.DataFrame):
        self._data = data

    def dropna(self, *args: Any, **kwargs: Any) -> pd.DataFrame:
        return logging.log_filter(self._data, "dropna", *args, **kwargs)

    def drop_duplicates(self, *args: Any, **kwargs: Any) -> pd.DataFrame:
        return logging.log_filter(
            self._data, "drop_duplicates", *args, **kwargs
        )

    def query(self, *args: Any, **kwargs: Any) -> pd.DataFrame:
        return logging.log_filter(self._data, "query", *args, **kwargs)

    def head(self, *args: Any, **kwargs: Any) -> pd.DataFrame:
        return logging.log_filter(self._data, "head", *args, **kwargs)

    def tail(self, *args: Any, **kwargs: Any) -> pd.DataFrame:
        return logging.log_filter(self._data, "tail", *args, **kwargs)

    def sample(self, *args: Any, **kwargs: Any) -> pd.DataFrame:
        return logging.log_filter(self._data, "sample", *args, **kwargs)

    def drop(self, *args: Any, **kwargs: Any) -> pd.DataFrame:
        return logging.log_filter(self._data, "drop", *args, **kwargs)

    def set_index(self, *args: Any, **kwargs: Any) -> pd.DataFrame:
        return logging.log_change_index(
            self._data, "set_index", *args, **kwargs
        )

    def reset_index(self, *args: Any, **kwargs: Any) -> pd.DataFrame:
        return logging.log_change_index(
            self._data, "reset_index", *args, **kwargs
        )

    def rename(self, *args: Any, **kwargs: Any) -> pd.DataFrame:
        return logging.log_rename(self._data, "rename", *args, **kwargs)

    def pivot(self, *args: Any, **kwargs: Any) -> pd.DataFrame:
        return logging.log_reshape(self._data, "pivot", *args, **kwargs)

    def melt(self, *args: Any, **kwargs: Any) -> pd.DataFrame:
        return logging.log_reshape(self._data, "melt", *args, **kwargs)

    def fillna(self, *args: Any, **kwargs: Any) -> pd.DataFrame:
        return logging.log_fillna(self._data, "fillna", *args, **kwargs)

    def bfill(self, *args: Any, **kwargs: Any) -> pd.DataFrame:
        return logging.log_fillna(self._data, "bfill", *args, **kwargs)

    def ffill(self, *args: Any, **kwargs: Any) -> pd.DataFrame:
        return logging.log_fillna(self._data, "ffill", *args, **kwargs)
