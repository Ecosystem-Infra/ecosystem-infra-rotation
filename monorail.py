from oauth2client.client import GoogleCredentials
import googleapiclient.discovery
import google.auth.compute_engine
import google.auth.impersonated_credentials

DISCOVERY_URL = (
    'https://monorail-prod.appspot.com/_ah/api/discovery/v1/apis/'
    '{api}/{apiVersion}/rest')

# https://cs.chromium.org/chromium/infra/go/src/infra/monorail/monorail.go?l=10&rcl=201f157c7ebc2be34ebeaa03ea47de2d8f4a8233
MONORAIL_AUTH_SCOPE = 'https://www.googleapis.com/auth/userinfo.email'
MONORAIL_SERVICE_ACCOUNT = 'monorail-api@ecosystem-infra.iam.gserviceaccount.com'
# Local fallback.
MONORAIL_KEY = 'monorail-key.json'

_credentials = None


def _get_credentials():
    global _credentials
    if _credentials:
        return _credentials
    try:
        default_creds = google.auth.compute_engine.Credentials()
        _credentials = google.auth.impersonated_credentials.Credentials(
            source_credentials=default_creds,
            target_principal=MONORAIL_SERVICE_ACCOUNT,
            target_scopes=[MONORAIL_AUTH_SCOPE],
        )
    except EnvironmentError:
        _credentials = GoogleCredentials.from_stream(MONORAIL_KEY)

    return _credentials


def query(q):
    credentials = _get_credentials()
    monorail = googleapiclient.discovery.build(
        'monorail', 'v1',
        discoveryServiceUrl=DISCOVERY_URL,
        credentials=credentials)
    return monorail.issues().list(projectId='chromium', can='open', q=q).execute()
