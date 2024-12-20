<p align=center><img src="https://github.com/dest4590/CloudRPC/assets/80628386/4d201d99-808f-48e8-b81d-9dba27e558de" width=350 align=center></p>

<h1 align=center>CloudRPC</h1>

## Simple program that can share your current playing song to discord

> the project still works 01/12/2024

### Features

-   [x] Show current song in Discord
-   [x] Show whether the song is liked or not
-   [x] Showing stations
-   [x] Showing current volume
-   [x] How much time is left until the end (works even with an hour)
-   [x] Easier installation

### Installation

-   Download server from [latest release](https://github.com/dest4590/CloudRPC/releases/latest) (windows/linux), and run it
-   Install [tampermonkey](https://www.tampermonkey.net/ 'Tampermonkey'), go to the utilites tab and in the Import from URL field enter: `http://localhost:9888/script.js` (make sure the server is enabled), and install the script, go to [soundcloud](https://soundcloud.com 'SoundCloud SIte')
-   If you see the notification that CloudRPC is running, everything is working!

#### Alternate install

-   Sure you install git and python:
-   Enter this command: `git clone https://github.com/dest4590/CloudRPC.git && cd CloudRPC && pip install -r requirements.txt && python main.py`
-   Install [tampermonkey](https://www.tampermonkey.net/ 'Tampermonkey'), create a new script and copy everything from [plugin.js](https://raw.githubusercontent.com/dest4590/CloudRPC/main/plugin.js) into the new script, save and go to soundcloud
-   If you see the notification that CloudRPC is running, everything is working!

Update: `git pull`, also you need to update script for tampermonkey!

## Screenshots:

![image](https://github.com/dest4590/CloudRPC/assets/80628386/82a42568-e89a-4712-bf6a-4e4b56649564)
![image](https://github.com/dest4590/CloudRPC/assets/80628386/7291b2ef-3923-448d-82af-e154c52c4745)

## DISCLAIMER!

By using this app you take responsibility for your SoundCloud/Discord account for yourself

You can't get banned for nothing (my program doesn't violate Discord and SoundCloud TOS)

<details>
<summary>Codenames</summary>

-   1.4 - CloudPower
-   1.3 - CloudLink

</details>
