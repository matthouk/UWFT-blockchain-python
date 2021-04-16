import subprocess
import json
import os
from dotenv import load_dotenv
from constants import *
load_dotenv()

mnemonic = os.getenv('MNEMONIC-HW')

command = './derive -g --mnemonic=mnemonic --numderive=5 --coin=ETH --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)

# for i in range(5): 
#    print(keys[i]['address'])

