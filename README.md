# Ecosystem Infra Rotation

This is a tool for the [Ecosystem Infra](https://bit.ly/ecosystem-infra) rotation.

## Usage

Visit https://ecosystem-infra-rotation.appspot.com/ and follow the instructions.

If you reload often you might hit the GitHub API limit for unauthenticated requests.
If this happens, [generate a new access token](https://github.com/settings/tokens/new)
and pass it in the URL: https://ecosystem-infra-rotation.appspot.com/#GH_TOKEN=abcdef

This is an AppEngine project, so we assume you already have Google Cloud SDK (including
Python plugins) set up locally.

## Running locally

You will need `npm` as well as `python3` and `virtualenv`:
```bash
sudo apt install python3 virtualenv python3-venv
```

To run locally:
```bash
./build.sh && dev_appserver.py .
```

This will serve the tool at http://localhost:8080/

When running locally, you also need a private key of a service account to access Monorail:

### API key

The Monorail queries require a `monorail-key.json` to be placed in a checkout of this repo.
You can create a new JSON private key from the
[ecosystem-infra GCP project](https://console.cloud.google.com/iam-admin/serviceaccounts/project?project=ecosystem-infra).
If you don't have access and think you should, ask foolip or robertma. (Note
that this is a different GCP project from the one we deploy to.)

See [Monorail API access](https://bugs.chromium.org/p/monorail/issues/detail?id=3234)
for more details/clues about how this works.

## Deploying

To deploy:
```bash
./build.sh && ./deploy.sh
```

*You do NOT need `monorail-key.json` for deployment.*

### Details about authentication

The production deployment does not a private key because we use IAM Service
Account Credentials API (`iamcredentials.googleapis.com`) to
[create credentials](https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials)
to impersonate the service account with access to Monorail from the default
AppEngine service account.
