import subprocess
import json
import os
# from constants import *

command = './derive -g --mnemonic=mnemonic --numderive=3 --coin=ETH --cols=path,address,privkey,pubkey --format=json'


mnemonic = os.getenv('MNEMONIC-HW')
p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)
