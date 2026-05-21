import logging
from collections import OrderedDict

import api_lib
import settings


def get_meetings():
    data = api_lib.getMeetings(settings.API_CLIENT)

    if data is None:
        return []
    elif 'meetings' not in data['response']:
        return []
    elif data['response']['meetings'] is None:
        return []

    meetings = []
    try:
        if type(data['response']['meetings']['meeting']) == list:
            meetings = data['response']['meetings']['meeting']
        else:
            meetings.append(data['response']['meetings']['meeting'])
    except KeyError:
        logging.warning("Failed to parse meetings")
    except TypeError:
        return []

    response = []

    for meeting in meetings:
        if not isinstance(meeting, dict):
            continue

        response.append(meeting)

    return response


def get_recordings(state: str) -> int:
    data = api_lib.getRecordings(settings.API_CLIENT, state)

    if not data or 'response' not in data:
        return 0

    response = data['response']

    if response.get('messageKey') == 'noRecordings':
        return 0

    if response.get('recordings') is None:
        return 0

    try:
        count = response.get('totalElements')
        return int(count) if count is not None else 0
    except (KeyError, ValueError, TypeError):
        logging.warning("Failed to parse totalElements from recordings response")
        return 0
