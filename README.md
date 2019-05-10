# Ecosystem Infra Rotation

This is a tool for the [ecosystem infra](https://bit.ly/ecosystem-infra) rotation.

## Usage

Visit https://ecosystem-infra-rotation.appspot.com/ and follow the instructions.

If you reload often you might hit the GitHub API limit for unauthenticated requests.
If this happens, [generate a new access token](https://github.com/settings/tokens/new) and pass it in the URL: https://ecosystem-infra-rotation.appspot.com/#GH_TOKEN=abcdef

## Running locally

The build script needs Bower, Python 3 and Virtualenv:
```bash
sudo npm install -g bower
sudo apt install python3 virtualenv
```

To run locally:
```bash
./build.sh && ./serve.sh
```

This will serve the tool at http://localhost:8080/

## API key

The monorail queries require a `monorail-key.json` to be placed in a checkout of this repo.
You can create a new API key and download a JSON file from the [ecosystem-infra GCP project](https://console.cloud.google.com/iam-admin/serviceaccounts/project?project=ecosystem-infra).
If you don't have access and think you should, ask foolip or robertma.
See the [Monorail API access](https://bugs.chromium.org/p/monorail/issues/detail?id=3234) request for more details/clues about how this works.

## Deploying

To deploy:
```bash
./build.sh && ./deploy.sh
```
