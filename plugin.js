// ==UserScript==
// @name         CloudRPC
// @namespace    http://github.com/dest4590/CloudRPC
// @version      1.0
// @description  Add SoundCloud Discord Rich Presence
// @author       dest4590
// @match        https://soundcloud.com/*
// @icon         https://www.google.com/s2/favicons?sz=256&domain=soundcloud.com
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    console.log('CloudRPC by dest4590')
    console.log('Starting...')

    var attempts = 0

    var updateData = function() {

        var xhr = new XMLHttpRequest();
        console.log("Send info to server")
        var url = "http://localhost:9888/update"
        xhr.open("POST", url, true)
        xhr.setRequestHeader("Content-Type", "application/json")
        xhr.addEventListener("error", function(){
            attempts++
            console.log("Send error attempts: " + attempts.toString())

            if (attempts >= 5) {
                console.log("The server failed to respond about 5 times, shutting down the script")
                window.clearInterval(sendInterval)
            }
        });

        var title = document.title
        var duration = document.querySelectorAll('div.playbackTimeline__duration span[aria-hidden="true"]')[0].innerHTML
        var current = document.querySelectorAll('div.playbackTimeline__timePassed span[aria-hidden="true"]')[0].innerHTML
        var artwork = document.querySelectorAll('div.playbackSoundBadge a div span')[0].style.backgroundImage
        var link = document.querySelectorAll('div.playbackSoundBadge__title a')[0].href
        var playbutton = document.querySelector('div.playControls__elements button.playControls__play').classList.contains("playing");

        var data = JSON.stringify({"song": title, "duration": duration, "current": current, "artwork": artwork.replace(/^url\("|"\)$/g, '').replace(/120/g, '500'), "link": link, "playing": playbutton});
        xhr.send(data);
    }

    var sendInterval = window.setInterval(updateData, 10000);
    updateData();
})();