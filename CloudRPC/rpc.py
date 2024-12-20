from pypresence import Presence, DiscordNotFound
from rich.console import Console
from .helper import date_format
from rich import print

console = Console()


class CloudRPC:
    client_id = 1140224106009206864
    RPC = Presence(client_id)

    def connect_rpc(self):
        with console.status(
            "[red bold]Connecting to discord..", spinner="dots2"
        ) as status:
            try:
                self.RPC.connect()
                status.stop()
                print(":white_check_mark: [bright_blue bold]Connected to discord!")
            except DiscordNotFound:
                status.stop()
                print("[red bold]Please sure you started discord![/]")
                quit(0)

    def update_rpc(
        self,
        state: str,
        details: str,
        large_image: str,
        link: str,
        end: int,
        playing: bool,
        liked: bool,
        station,
        volume,
        playlist,
    ):
        if playing:
            if not station and not playlist:
                self.RPC.update(
                    state=state,
                    details=details,
                    large_image=large_image,
                    large_text=f"{volume}% volume",
                    buttons=[
                        {"label": "Listen", "url": link},
                        {
                            "label": "Github",
                            "url": "https://github.com/dest4590/CloudRPC",
                        },
                    ],
                    end=end,
                    small_image="cloudrpc_logo" if not liked else "heart",
                    small_text="CloudRPC" if not liked else "Liked",
                )

            elif station:
                self.RPC.update(
                    state=state,
                    details=details,
                    large_image=large_image,
                    large_text=f"{volume}% volume",
                    buttons=[
                        {"label": "Listen", "url": link},
                        {
                            "label": "Listen Station",
                            "url": "https://soundcloud.com/discover/sets/track-stations:"
                            + str(station).split("%3A")[1],
                        },
                    ],
                    end=end,
                    small_image="station",
                    small_text=(
                        "Listening Station!"
                        if not liked
                        else "Listening Station, Liked track!"
                    ),
                )

            elif playlist:
                self.RPC.update(
                    state=state,
                    details=details,
                    large_image=large_image,
                    large_text=f"{volume}% volume",
                    buttons=[
                        {"label": "Listen", "url": link},
                        {
                            "label": "Listen Playlist",
                            "url": "https://soundcloud.com/" + str(playlist),
                        },
                    ],
                    end=end,
                    small_image="playlist",
                    small_text=(
                        "Listening Playlist!"
                        if not liked
                        else "Listening Playlist, Liked track!"
                    ),
                )

        else:
            self.RPC.update(
                state=state,
                details=details,
                large_image=large_image,
                large_text="Cat",
                small_image="cloudrpc_logo",
                small_text="CloudRPC",
            )

        print(date_format + " [bright_blue]Updated RPC")
