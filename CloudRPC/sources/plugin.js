// ==UserScript==
// @name         CloudRPC
// @namespace    http://github.com/dest4590/CloudRPC
// @version      1.3
// @description  Add SoundCloud Discord Rich Presence
// @author       dest4590
// @match        https://soundcloud.com/*
// @icon         https://i.imgur.com/3CS7JNO.png
// @grant        none
// ==/UserScript==

(function () {
    'use strict'

    console.log('CloudRPC by dest4590')
    console.log('Starting...')

    window.CloudRPC_attempts = 0

    var nofitication = function (title, text) {
        var grtDiv = document.createElement("div")
        grtDiv.innerHTML = `
            <div id="gritter-notice-wrapper" class="top-right" bis_skin_checked="1" style="opacity: 0">
                <div id="gritter-item-1" class="gritter-item-wrapper oneLine" bis_skin_checked="1">
                    <div class="gritter-top" bis_skin_checked="1"></div>
                    <div class="gritter-item" bis_skin_checked="1">
                        <img src="https://i.imgur.com/ZTOLJjr.png" class="gritter-image" style="padding-top: 1.5px"/>
                        <div class="gritter-with-image" bis_skin_checked="1">
                            <span class="gritter-title">${title}</span>
                            <p>${text}</p>
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

        setTimeout(fadeOutElement, 2000)

        setTimeout(function () { grtDiv.remove() }, 100 + 3500)
    }

    var updateData = function () {
        var xhr = new XMLHttpRequest()
        console.log("Send info to server")
        var url = "http://localhost:9888/update"
        xhr.open("POST", url, true)
        xhr.setRequestHeader("Content-Type", "application/json")
        xhr.addEventListener("error", function () {
            nofitication('CloudRPC Server error', "Error attempts: " + window.CloudRPC_attempts.toString())
            window.CloudRPC_attempts++
            console.log("Error attempts: " + window.CloudRPC_attempts.toString())

            if (window.CloudRPC_attempts >= 5) {
                nofitication('CloudRPC fatal', "Shutting down the script")
                console.log("The server failed to respond about 5 times, shutting down the script")
                window.clearInterval(sendInterval)
            }
        })

        xhr.onreadystatechange = () => {
            if (xhr.readyState === 4) {
                console.log("Server response: " + xhr.response)
            }
        }

        var name = document.title
        var duration = document.querySelector('div.playbackTimeline__duration span[aria-hidden="true"]').innerHTML
        var current = document.querySelector('div.playbackTimeline__timePassed span[aria-hidden="true"]').innerHTML
        var artwork = document.querySelector('div.playbackSoundBadge a div span').style.backgroundImage
        var link = document.querySelector('div.playbackSoundBadge__title a').href
        var playbutton = document.querySelector('div.playControls__elements button.playControls__play').classList.contains("playing")
        var liked = document.querySelector('div.playbackSoundBadge__actions button.sc-button-like').classList.contains("sc-button-selected")
        var volume = document.querySelector('div.volume__sliderWrapper').getAttribute('aria-valuenow') * 100
        var station = false
        var playlist = false

        if (link.includes("in_system_playlist")) {
            station = link.match(/in_system_playlist=([^&]+)/)[1]
        }

        if (link.includes("?in=")) {
            playlist = link.match(/[?&]in=([^&]+)/)[1]
        }

        var data = JSON.stringify({ "song": name, "duration": duration, "current": current, "artwork": artwork.replace(/^url\("|"\)$/g, '').replace(/120/g, '500'), "link": link, "playing": playbutton, "liked": liked, "station": station, "volume": volume, "playlist": playlist })
        xhr.send(data)
    }

    var applyFunctions = function () {
        var cloudrpc = window.CloudRPC = {}
        cloudrpc.start = function () { window.setInterval(updateData, 10000) }
        cloudrpc.stop = function () { window.clearInterval(sendInterval) }
        cloudrpc.resetAttempts = function () { window.CloudRPC_attempts = 0 }
        cloudrpc.updateRPC = updateData
    }

    setTimeout(function () { nofitication('CloudRPC loaded!', 'By <a href="https://github.com/dest4590/">dest4590</a>') }, 2000)
    setTimeout(applyFunctions, 2000)

    var sendInterval = window.setInterval(updateData, 10000)
    updateData()
})()