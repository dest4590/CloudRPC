# CloudRPC

## Simple program that can share your current playing song to discord

### Installation

* Sure you install git and python: 
* Enter this command: `git clone https://github.com/dest4590/CloudRPC.git && cd CloudRPC && pip install flask flask_cors pypresence && python server.py`
* Install [tampermonkey](https://www.tampermonkey.net/ "Tampermonkey"), create a new script and copy everything from [plugin.js](https://raw.githubusercontent.com/dest4590/CloudRPC/main/plugin.js) into the new script, save and go to soundcloud
* If you see the notification that CloudRPC is running, everything is working!


Update: `git reset --hard HEAD && git clean -f -d && git pull`, also you need to update script for tampermonkey!

## Screenshots:

![image](https://github.com/dest4590/CloudRPC/assets/80628386/52e35842-5905-489e-9b54-eea08515873e)

![image](https://github.com/dest4590/CloudRPC/assets/80628386/49cf9474-8698-4518-84d6-42245bbbe08f)

## Pros
* Low memory usage:

  Tampermonkey: 48,900K, 1.6 CPU (when sending request)

  Python server: 24MB, 0.3 CPU (when processing a request and changing the RPC)  

  > Tested on Ryzen 5 3500U with 10gb ram

* Easy to use:
You need only 1 command and script to use it

* Working on Windows/Linux (MacOS not tested)

## Cons
* Python, yes, it's pretty slow, but it's suitable for such purposes, and it's easy to install
* High ram consumption from the server, maybe 30mb is a lot for someone
* Sometimes bugs can occur, please create an [issue](https://github.com/dest4590/CloudRPC/issues) so I can fix it
