import time

from app import api
from app.api import torrent_client
from app.api import beet_queue
from app.api import events

import requests
import eventlet


INTERVAL = 5


def _process(torrent):
    pass
    # # 'torrent seen' -> on the last iteration, the torrent was downloading
    # # and betanin indented to process it when it finishes 
    # if not state.was_seen(torrent.id) and torrent.is_downloaded:
    #     return
    # # torrent is new and (downloading or downloaded)
    # if torrent.is_downloaded:
    #     beet_queue.add(torrent)
    #     state.mark_imported(torrent.id)
    # else: # torrent is downloading
    #     state.is_downloading(torrent.id)


def _update_torrents():
    new_torrents = list(torrent_client.get_torrents())
    for torrents in new_torrents():
        print(torrent)


def _worker():
    while True:
        # _update_torrents()
        # for key, value in list(torrent_client.get_torrents())
            
        # for torrent in api.torrents:
        #     _process(torrent)
        # events.torrents_grabbed()
        eventlet.sleep(INTERVAL)


def start_worker():
    print("starting client worker")
    eventlet.spawn(_worker)
