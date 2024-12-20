from .helper import Cats, logo, version, date_format, codename
from flask import Flask, request, send_file, render_template
from rich.console import Console
from datetime import datetime
from flask_cors import CORS
from .rpc import CloudRPC
import flask.cli
import logging
import sys, os
import json
import time

flask.cli.show_server_banner = lambda *args: None

console = Console(highlight=False)

console.print("[green]" + logo + "[green]")

console.print("[green bold]" + version + "[/]" + f" [gray50]({codename})[/]")

cats = Cats()

rpc = CloudRPC()
rpc.connect_rpc()

start_time = datetime.now().strftime("%d/%m/%Y at %H:%M:%S")


def time_to_seconds(time: str):
    time_parts = time.split(":")
    if len(time_parts) == 3:
        hours, minutes, seconds = map(int, time_parts)
        return hours * 3600 + minutes * 60 + seconds
    elif len(time_parts) == 2:
        minutes, seconds = map(int, time_parts)
        return minutes * 60 + seconds


base_dir = os.path.join(sys._MEIPASS) if hasattr(sys, "_MEIPASS") else None
pindir = lambda dir: (
    os.path.join(base_dir, "sources") if hasattr(sys, "_MEIPASS") else dir
)
pinfile = lambda file: (
    os.path.join(base_dir, "sources", str(file).split("/")[-1])
    if hasattr(sys, "_MEIPASS")
    else file
)


class CloudRPCServer:
    def __init__(self, debug):
        self.debug = debug

    app = Flask("CloudRPC Server", template_folder=pindir("CloudRPC/sources"))
    CORS(app)
    
    console.print(date_format + " [green]Server started at http://localhost:9888")

    logging.getLogger("werkzeug").disabled = True

    @app.route("/update", methods=["POST"])
    def update():
        data = json.loads(request.data.decode())

        console.print(date_format + " [blue]RPC update request")

        try:
            if data["playing"]:
                if not data["playlist"]:
                    song_title = str(data["song"]).split(" by ")

                    rpc.update_rpc(
                        song_title[0],
                        song_title[1],
                        data["artwork"],
                        data["link"],
                        time.time()
                        + time_to_seconds(data["duration"])
                        - time_to_seconds(data["current"]),
                        True,
                        data["liked"],
                        data["station"],
                        str(data["volume"]),
                        data["playlist"],
                    )

                elif data["playlist"]:
                    title = str(data["song"])
                    song_name, playlist_name = (
                        title[: title.find("in")],
                        title[title.rfind("in") + 2 :],
                    )
                    rpc.update_rpc(
                        "Playlist: " + playlist_name,
                        song_name,
                        data["artwork"],
                        data["link"],
                        time.time()
                        + time_to_seconds(data["duration"])
                        - time_to_seconds(data["current"]),
                        True,
                        data["liked"],
                        data["station"],
                        str(data["volume"]),
                        data["playlist"],
                    )

            else:
                assets = cats.get_random()
                rpc.update_rpc(
                    assets[0],
                    "Doesn't listen to anything",
                    assets[1],
                    None,
                    None,
                    False,
                    False,
                    False,
                    "0",
                    False,
                )

            return "200, Updated RPC"

        except Exception as e:
            console.print("[red bold]Error: " + str(e))
            return "Error: " + str(e), 500

    @app.route("/script.js")
    def script():
        console.print(date_format + " [deep_sky_blue4]Script request")
        return send_file(
            pinfile("CloudRPC/sources/plugin.js"), "text/javascript", as_attachment=True
        )

    @app.route("/")
    def index():
        console.print(date_format + " [medium_purple3]WebPanel request")
        return render_template(
            "index.html", version=version, codename=codename, start_time=start_time
        )

    @app.route("/style")
    def style():
        return send_file(pinfile("CloudRPC/sources/style.css"))

    def run(self):
        self.app.run("127.0.0.1", "9888", self.debug)
