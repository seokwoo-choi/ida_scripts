# argv
import sys
import os
def get_script_directory():
    dir_path = os.path.dirname(sys.argv[0])
    return dir_path
