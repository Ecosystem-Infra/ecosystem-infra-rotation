from oauth2client.client import GoogleCredentials
import googleapiclient.discovery

DISCOVERY_URL = (
    'https://monorail-prod.appspot.com/_ah/api/discovery/v1/apis/'
    '{api}/{apiVersion}/rest')

MONORAIL_KEY = 'monorail-key.json'


def query(q):
    credentials = GoogleCredentials.from_stream(MONORAIL_KEY)

    monorail = googleapiclient.discovery.build(
        'monorail', 'v1',
        discoveryServiceUrl=DISCOVERY_URL,
        credentials=credentials)
    return monorail.issues().list(projectId='chromium', can='open', q=q).execute()
