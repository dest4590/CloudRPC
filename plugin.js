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
    'use strict'

    console.log('CloudRPC by dest4590')
    console.log('Starting...')

    var attempts = 0

    var nofitication = function() {
        var grtDiv = document.createElement("div")
        grtDiv.innerHTML = `
            <div id="gritter-notice-wrapper" class="top-right" bis_skin_checked="1" style="opacity: 0">
                <div id="gritter-item-1" class="gritter-item-wrapper oneLine" bis_skin_checked="1">
                    <div class="gritter-top" bis_skin_checked="1"></div>
                    <div class="gritter-item" bis_skin_checked="1">
                        <img src="https://i.imgur.com/ZTOLJjr.png" class="gritter-image" style="padding-top: 1.5px"/>
                        <div class="gritter-with-image" bis_skin_checked="1">
                            <span class="gritter-title">CloudRPC Loaded!</span>
                            <p>By <a href="https://github.com/dest4590/">dest4590</a></p>
                        </div>
                        <div style="clear: both" bis_skin_checked="1"></div>
                    </div>
                    <div class="gritter-bottom" bis_skin_checked="1"></div>
                </div>
            </div>
        `

        document.body.appendChild(grtDiv)

        var element = document.getElementById("gritter-notice-wrapper")
        element.style.transition = "opacity 0.5s ease-in-out"

        function fadeIn() {
            element.style.opacity = 1
        }

        setTimeout(fadeIn, 100)

        function fadeOutElement() {
            element.style.opacity = 0
        }

        setTimeout(fadeOutElement, 3500)
    }

    var updateData = function() {
        var xhr = new XMLHttpRequest()
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
        })

        xhr.onreadystatechange = () => {
            if (xhr.readyState === 4) {
              console.log("Server response: " + xhr.response)
            }
        }

        var title = document.title
        var duration = document.querySelectorAll('div.playbackTimeline__duration span[aria-hidden="true"]')[0].innerHTML
        var current = document.querySelectorAll('div.playbackTimeline__timePassed span[aria-hidden="true"]')[0].innerHTML
        var artwork = document.querySelectorAll('div.playbackSoundBadge a div span')[0].style.backgroundImage
        var link = document.querySelectorAll('div.playbackSoundBadge__title a')[0].href
        var playbutton = document.querySelector('div.playControls__elements button.playControls__play').classList.contains("playing")
        var liked = document.querySelector('div.playbackSoundBadge__actions button.sc-button-like').classList.contains("sc-button-selected")
        var station = false

        if (link.includes("in_system_playlist")) {
            station = link.match(/in_system_playlist=([^&]+)/)[1]
        }

        var data = JSON.stringify({"song": title, "duration": duration, "current": current, "artwork": artwork.replace(/^url\("|"\)$/g, '').replace(/120/g, '500'), "link": link, "playing": playbutton, "liked": liked, "station": station})
        xhr.send(data)
    }

    setTimeout(nofitication, 2000)

    var sendInterval = window.setInterval(updateData, 10000)
    updateData()
})()