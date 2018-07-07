import sys
import os
lib_path = os.path.dirname(os.path.abspath(__file__)) + '/lib/'
sys.path.append(lib_path)

lib_path = os.path.dirname(os.path.abspath(__file__)) + '/models/'
sys.path.append(lib_path)

import date_manager