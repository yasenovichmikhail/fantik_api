#!/usr/bin/env bash

"""
reset types:
  force - set fake design to 0 unconditionally
  force_timed - if fake design is set more than 'hours' ago, set fake design to 0
  reset - reset fake design setting, new value will be set based on next /settings response
"""

import firebase_admin
import requests
import json
import tqdm
from config.config import *

from firebase_admin import messaging
from typing import List


def get_apps(api: str, enabled: List[int]):
    if api.endswith('/'):
        api = api[:-1]
    response = requests.get(f'{api}+{FIREBASE_PATH}').json()
    apps = []
    for app in response['fireBaseApplications']:
        appId = app['firebaseAppId']
        if len(enabled) > 0 and appId not in enabled:
            print(f'Firebase appId {appId} is skipped because not in whitelist')
            continue
        try:
            certificate = firebase_admin.credentials.Certificate(json.loads(app['adminSdk']))
            app = firebase_admin.initialize_app(name=str(app['firebaseAppId']), credential=certificate)
            apps.append(app)
        except Exception as e:
            print(f'Firebase app {appId} is skipped because cannot initialize: {e}')
    return apps


def b2s(b):
    return 'true' if b else 'false'


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('tokens', nargs='+', help='Tokens to send notifications to')
    parser.add_argument('--apps', default=[], nargs='*',
                        help='List of firebaseAppId to send notifications to. Empty list implies all apps. All by default',
                        type=int)
    parser.add_argument('--api', default=BASE_URL_DEV, help='API server url')
    parser.add_argument('-t', '--reset-type', dest='reset_type', choices=['force', 'force_timed', 'reset'],
                        required=True, help='Type of design reset')
    parser.add_argument('-H', '--hours', dest='hours', type=int, default=24,
                        help='when --reset-type=force_timed, specify amount of hours to apply reset, ignored otherwise')
    parser.add_argument('-n', '--notification', dest='notification', action='store_true', default=False,
                        help='Show notification on device when real design has been set')
    parser.add_argument('-c', '--clean', dest='clean', action='store_true', default=True,
                        help='Clear all preferences when reset design')
    parser.add_argument('--notification-title', dest='notification_title', default=None, required=False,
                        help='Notification title text, ignored if no --notification specified')
    parser.add_argument('--notification-body', dest='notification_body', default=None, required=False,
                        help='Notification body text, ignored if no --notification specified')
    args = parser.parse_args()
    apps = get_apps(args.api, args.apps)
    data = {
        'req_type': 'fake_design_reset',
        'reset_type': args.reset_type,
        'hours': f'{args.hours}',
        'show_notification': b2s(args.notification),
        'clean': b2s(args.clean),
    }
    if args.notification_body:
        data['notification_body'] = args.notification_body
    if args.notification_title:
        data['notification_title'] = args.notification_title
    for app in tqdm.tqdm(apps):
        for token in tqdm.tqdm(args.tokens):
            message = messaging.Message(data=data, token=token)
            response = messaging.send(message, app=app)
            print(response)
