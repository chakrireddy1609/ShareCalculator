import inspect
import logging

import pytest
from selenium.webdriver import Keys

from Pages.SearchPage import SearchPage
from Utilities.TestData import TestData


@pytest.mark.usefixtures("setup")
class Test_Base:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger






