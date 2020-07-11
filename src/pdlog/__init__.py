"""
pdlog
~~~~~

.. note::

   The ``pdlog`` package content, including all submodules are copied
   directly from a forked version of the following GitHub repository:
   https://github.com/DataProphet/pdlog

   * The ``pdlog`` version copied here is ``pdlog==0.1.0.post0``
   * I make not claims of authorship for these ``pdlog`` submodules
   * Instead, I have copied them to this project in order to more
   deeply investigate the methods used this this package.
"""
from . import accessor
from . import logging
from . import string


__all__ = ["accessor", "logging", "string"]
