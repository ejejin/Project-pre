# -*- coding: UTF-8 -*-
from w0_BAIDU_py2_Firefox import BAIDU_INDEX

ID = "skyblue1294@126.com"
PW = "sky456"
KEYWORD = "%CE%ED%F6%B2"

baidu = BAIDU_INDEX()
baidu.AWAKE_BROWSER()
baidu.SEARCH_test()
baidu.LOGIN_BAIDU(ID, PW)
baidu.ACCESS_URL()

#baidu.QUIT()

