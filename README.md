# ida_scripts
Collections of IDA Pro 7.4 python scripts. 

* Get the directory containing the running python script.
```
import sys
import os
def get_script_directory():
    dir_path = os.path.dirname(sys.argv[0])
    return dir_path
```
