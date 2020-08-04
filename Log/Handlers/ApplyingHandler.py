import logging.config
from os import path
"""

    The ApplyingHandler handles the functionality of logging to Applying Folder

"""


class ApplyingHandler:

        logConfigurePath = path.abspath('.\\Settings\\logging.config')
        logConfig = logging.config.fileConfig(logConfigurePath)
