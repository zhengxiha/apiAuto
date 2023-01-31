import time
import os
import pytest
import sys
from loguru import logger


if __name__ == '__main__':

    logger.remove()
    logger.add(sys.stderr,level="INFO")

    logger.add("./logs/{time}.log",encoding="utf-8",enqueue=True)
    logger.info("\n"
    "--------------------start--------------------"
    "\n***                                       ***"
    "\n***                                       ***"
    "\n*********************************************")


    pytest.main(['-vs',"--alluredir=reports/temps","--clean-alluredir"])
    # pytest.main()
    time.sleep(3)


    os.system("allure generate ./reports/temps -o ./reports/report_html ")
    # os.system("pytest -v -m attendance1")

