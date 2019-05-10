#!/usr/bin/env python3
from oauth2client.client import GoogleCredentials
import json
import googleapiclient.discovery
import os.path
import sys

DISCOVERY_URL = (
    'https://monorail-prod.appspot.com/_ah/api/discovery/v1/apis/'
    '{api}/{apiVersion}/rest')


def query(q, credentials):
    monorail = googleapiclient.discovery.build(
        'monorail', 'v1',
        discoveryServiceUrl=DISCOVERY_URL,
        credentials=credentials)
    return monorail.issues().list(projectId='chromium', can='open', q=q).execute()

def main():
    CREDENTIALS_FILE = sys.argv[1]
    RESULTS_FILE = sys.argv[2]

    QUERIES = [
        ('Ecosystem Infra: unconfirmed and untriaged', { 'q': 'component:Blink>Infra>Ecosystem status:Unconfirmed,Untriaged' }),
        ('Ecosystem Infra: P0 issues >2 days', { 'q': 'component:Blink>Infra>Ecosystem Pri=0 modified<today-2' }),
        ('Ecosystem Infra: P1 issues >30 days', { 'q': 'component:Blink>Infra>Ecosystem Pri=1 modified<today-30' }),
        ('Ecosystem Infra: P2 issues >60 days', { 'q': 'component:Blink>Infra>Ecosystem Pri=2 modified<today-60' }),
        ('Blink Infra: unconfirmed and untriaged', { 'q': 'component:Blink>Infra status:Unconfirmed,Untriaged' }),
        ('Blink Infra: P0 issues >2 days', { 'q': 'component:Blink>Infra Pri=0 modified<today-2' }),
        ('Blink Infra: P1 issues >30 days', { 'q': 'component:Blink>Infra Pri=1 modified<today-30' }),
        ('Blink Infra: P2 issues >60 days', { 'q': 'component:Blink>Infra Pri=2 modified<today-60' }),
    ]

    if os.path.exists(CREDENTIALS_FILE):
        credentials = GoogleCredentials.from_stream(CREDENTIALS_FILE)
    else:
        credentials = GoogleCredentials.get_application_default()

    results = {}

    for label, args in QUERIES:
        results[args['q']] = query(args['q'], credentials)

    with open(RESULTS_FILE, 'w+') as f:
        json.dump(results, f, indent=2, sort_keys=True)


if __name__ == "__main__":
    main()
