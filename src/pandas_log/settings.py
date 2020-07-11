"""
pandas_log.settings
~~~~~~~~~~~~~~~~~~~

.. note::

   The ``pandas_log.settings`` module is copied directly from
   the following GitHub repository by the author Eyal Trabelsi:
   https://github.com/eyaltrabelsi/pandas-log

   * The ``pandas-log`` version copied here is ``pandas-log==0.1.7``
   * I make not claims of authorship for this submodule
   * Instead, I have copied this module in order to more
   deeply investigate the methods used in the ``pandas-log`` package.
"""

ORIGINAL_METHOD_PREFIX = "original_"
PATCHED_LOG_METHOD_PREFIX = "log_"
DATAFRAME_ADDITIONAL_METHODS_TO_OVERIDE = [
    "copy",
    "reset_index",
    "__getitem__",
    "__setitem__",
]
DATAFRAME_METHODS_TO_OVERIDE = [
    "query",
    "drop",
    "dropna",
    "assign",
    "sort_index",
    "sort_values",
    "head",
    "tail",
    "sample",
    "fillna",
    "merge",
    "join",
    "nlargest",
    "nsmallest",
    "apply",
    "iterrows",
    "applymap",
    "pipe",
    "rolling",
    "groupby",
    "rename",
    "agg",
    "aggregate",
    "stack",
    "unstack",
    "pivot",
    "pivot_table",
    "mask",
    "max",
    "mean",
    "median",
    "melt",
    "replace",
    "skew",
    "notna",
    "kurt",
    "expanding",
    "drop_duplicates",
    "bfill",
    "corr",
    "corrwith",
    "droplevel",
    "explode",
    "ffill",
    "filter",
    "first",
    "kurtosis",
    "align",
    "transform",
    "update",
    "squeeze",
    "shift",
    "rank",
    "nunique",
    "min",
    "mod",
    "mode",
    "std",
]
SERIES_METHODS_TO_OVERIDE = ["mask", "where"]
