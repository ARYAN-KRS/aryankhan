import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from AK64 import o
    Ao()
elif bit == '32bit':
    from AK import o
    o()
else:
    print('\ YOUR DEVICE IS NOT SUPPORT FOR THIS COMMAND')
    os.system('exit')
