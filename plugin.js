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

    var updateData = function() {
    var xhr = new XMLHttpRequest();
        console.log("sending")
        var url = "http://localhost:9888/update";
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");

        var title = document.title
        var duration = document.querySelectorAll('div.playbackTimeline__duration span[aria-hidden="true"]')[0].innerHTML
        var current = document.querySelectorAll('div.playbackTimeline__timePassed span[aria-hidden="true"]')[0].innerHTML
        var artwork = document.querySelectorAll('div.playbackSoundBadge a div span')[0].style.backgroundImage
        var link = document.querySelectorAll('div.playbackSoundBadge__title a')[0].href

        var data = JSON.stringify({"song": title, "duration": duration, "current": current, "artwork": artwork.replace(/^url\("|"\)$/g, '').replace(/120/g, '500'), "link": link});
        xhr.send(data);
    }

    window.setInterval(updateData, 10000);
    updateData();
})();