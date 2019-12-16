﻿# ida_scripts
Collections of IDA Pro 7.4 python scripts. 

* Get the directory containing the running python script.
```python
import sys
import os
def get_script_directory():
    dir_path = os.path.dirname(sys.argv[0])
    return dir_path
```

* To retrieve MD5 string in IDAPython 7.4 
```python
''.join(['%02X' % x for x in idaapi.retrieve_input_file_md5()])
```
