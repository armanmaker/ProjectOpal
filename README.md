<pre>

 ____  ____   ___   ____    ___    __ ______       ___   ____   ____  _     
|    \|    \ /   \ |    |  /  _]  /  ]      |     /   \ |    \ /    || |    
|  o  )  D  )     ||__  | /  [_  /  /|      |    |     ||  o  )  o  || |    
|   _/|    /|  O  |__|  ||    _]/  / |_|  |_|    |  O  ||   _/|     || |___ 
|  |  |    \|     /  |  ||   [_/   \_  |  |      |     ||  |  |  _  ||     |
|  |  |  .  \     \  `  ||     \     | |  |      |     ||  |  |  |  ||     |
|__|  |__|\_|\___/ \____||_____|\____| |__|       \___/ |__|  |__|__||_____|
                                                                            
</pre>
Source: https://www.shadowlabs.cc/project-opal
[![Github](https://img.shields.io/badge/Github-Shadowlabs-green?style=for-the-badge&logo=github)](https://github.com/shadowlabscc)
[![Reddit](https://img.shields.io/badge/Reddit-Shadowlabs-orange?style=for-the-badge&logo=reddit)](https://reddit.com/r/shadowlabs)
[![Instagram](https://img.shields.io/badge/IG-shadowlabs-red?style=for-the-badge&logo=instagram)](https://www.instagram.com/shadowlabscc)
[![Twitter](https://img.shields.io/badge/Twitter-blue?style=for-the-badge&logo=twitter)](https://twitter.com/shadowlabscc)
[![Facebook](https://img.shields.io/badge/Facebook-purple?style=for-the-badge&logo=facebook)](https://facebook.com/shadowlabscc)
[![GitHub issues](https://img.shields.io/github/issues/shadowlabscc/ProjectOpal.svg)](https://github.com/shadowlabscc/ProjectOpal/issues)
[![GitHub stars](https://img.shields.io/github/stars/shadowlabscc/ProjectOpal.svg)](https://github.com/shadowlabscc/ProjectOpal/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/shadowlabscc/ProjectOpal.svg)](https://github.com/shadowlabscc/ProjectOpal/network)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/shadowlabscc/ProjectOpal.svg?style=popout)](https://twitter.com/intent/tweet?text=Wow:&url=https://github.com/shadowlabscc/ProjectOpal)

# Opal (Python2)[Why python2? well i like it and it was old project]
Stealth post-exploitation framework for Wordpress CMS

***Official ProjectOpal Repository.***

# What is it and why was it made?
We intentionally made it for our penetration testing jobs however its getting grey hairs now so we thought we would like to pass it on to the public!. ProjectOpal or Opal.
<br>
Is a stealth post exploit framework for wordpress sites that can hide its trace from logs and obfuscate it's way through the system! :)<br>
Fun cool features it creates an admin user that is hidden from all users including admins! just note its stored in the database so don't forget to delete your traces.

<img src="https://i.imgur.com/dPd8AHt.png">
<pre>
WORDPRESS:
  Login: opal@wordpress.com
  (Default) Pass: QCa9KT4eAvxzC5Kk or projectopal

  Backend Login:
    (Default) Login: QCa9KT4eAvxzC5Kk

LOGINTAMP:
  allows you to login to any user

CHAPPY:
  Creates a administrator account

USERDUMP:
  Dumps all user entries

LOCATE:
  Gets implant location
</pre>

If you need any help feel free to contact us at sales@shadowlabs.cc.


Enjoy!

# Getting Started

Clone the repository with git:
```
git clone https://github.com/shadowlabscc/ProjectOpal.git && cd ProjectOpal
```
```
python opal.py
```
or
```
python Injector.py (Edit the config.py!)
```

You will see a start-up screen. Type help and get to know your shell better :)

# Features:

These are features that Shadowlabs Team prides themself on based on this program:

- Bypass WAF(Web application firewall)
- Hidden/Stealth
- Let's you login to any user
- Dump entire user entries
- Create a persistent admin account that is hidden
- Obfuscated implant
- Multi-functionality


<pre>
├── Injector
│   ├── Dolly2.zip
│   ├── Injector.py
│   └── config.py
├── Wordpress
│   ├── 64fc9f8191afee3231e7197a27b8ee0c.php
│   ├── index.php
│   └── install.php
├── lib
│   ├── banner.txt
│   ├── config.password
│   ├── config.target
│   └── persistent_head.txt
└── opal.py
</pre>
