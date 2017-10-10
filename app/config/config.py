# -*- coding:utf-8 -*-


# Author: hillguo 
# Date: 2017-07-05

import sys
import os
import getopt
import json

from tornado.options import define, options


__json_data = open(os.path.join(os.path.dirname(__file__), 'debug.json'))

rootDir = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
configDict = json.load(__json_data)

define('port', default=configDict['port'], help="run on the given port", type=int)
define('debug', default=configDict['is_debug'], type=bool)
define('db_path', default=configDict['db_path'], type=str)
define('static_path', default=os.path.join(rootDir, configDict['static_path']), type=str)
define('template_path', default=os.path.join(rootDir,configDict['template_path']), type=str)
define('xsrf_cookies', default=configDict['xsrf_cookies'], type=bool)
define('cookie_secret', default=configDict['cookie_secret'], type=str)
define('base_dirname', default=rootDir, type=str)
define('login_url', default=configDict['login_url'], type=str)
define('logger_name', default=configDict['logger_name'], type=str)
define('sep_logger', default=configDict['sep_logger'], type=str)

sys.path.append(rootDir)

if __name__ == "__main__":
    print (configDict)
#print (configDict)
