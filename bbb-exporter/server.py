import logging
import sys
import signal

from time import sleep

from prometheus_client import start_http_server, REGISTRY

import settings
from collector import BigBlueButtonCollector
from helpers import verify_recordings_base_dir_exists

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")


def shutdown_handler(sig, frame):
    logging.info(f"Received signal {sig}. Shutting down...")
    sys.exit(0)

if __name__ == '__main__':
    if settings.DEBUG:
        logging.getLogger().setLevel(logging.DEBUG)

    if settings.RECORDINGS_METRICS_READ_FROM_DISK:
        logging.info("Enabling recordings metrics read from disk, we will not request expensive recordings metrics "
                     "via the API")
        if verify_recordings_base_dir_exists():
            logging.debug("BigBlueButton recordings base dir exists")
        else:
            logging.fatal("BigBlueButton recordings base dir (" + settings.recordings_metrics_base_dir + ") does not " +
                          "exist. Disable RECORDINGS_METRICS_READ_FROM_DISK=true or run on BigBlueButton server.")
            sys.exit(1)

    start_http_server(settings.PORT, addr=settings.BIND_IP)
    logging.info("HTTP server started on {}:{}".format(settings.BIND_IP, settings.PORT))

    collector = BigBlueButtonCollector()

    if len(settings.ROOM_PARTICIPANTS_CUSTOM_BUCKETS) > 0:
        collector.set_room_participants_buckets(settings.ROOM_PARTICIPANTS_CUSTOM_BUCKETS)

    if len(settings.ROOM_LISTENERS_CUSTOM_BUCKETS) > 0:
        collector.set_room_listeners_buckets(settings.ROOM_LISTENERS_CUSTOM_BUCKETS)

    if len(settings.ROOM_VOICE_PARTICIPANTS_CUSTOM_BUCKETS) > 0:
        collector.set_room_voice_participants_buckets(settings.ROOM_VOICE_PARTICIPANTS_CUSTOM_BUCKETS)

    if len(settings.ROOM_VIDEO_PARTICIPANTS_CUSTOM_BUCKETS) > 0:
        collector.set_room_video_participants_buckets(settings.ROOM_VIDEO_PARTICIPANTS_CUSTOM_BUCKETS)

    REGISTRY.register(collector)

    signal.signal(signal.SIGTERM, shutdown_handler)
    signal.signal(signal.SIGINT, shutdown_handler)

    logging.info("Exporter is running. Press Ctrl+C to stop.")

    try:
        while True:
            if hasattr(signal, 'pause'):
                signal.pause()
            else:
                sleep(1)
    except SystemExit:
        pass
