# Ecosystem Infra Rotation

This is a tool for the [Ecosystem Infra](https://bit.ly/ecosystem-infra) rotation.

## Usage

Visit https://ecosystem-infra-rotation.appspot.com/ and follow the instructions.

If you reload often you might hit the GitHub API limit for unauthenticated requests.
If this happens, [generate a new access token](https://github.com/settings/tokens/new)
and pass it in the URL: https://ecosystem-infra-rotation.appspot.com/#GH_TOKEN=abcdef

### Dependencies

This is an AppEngine project, so we assume you already have Google Cloud SDK
(including Python plugins) set up locally.

You will need to have npm on your machine. (Instructions are omitted as they
vary across platforms.) In addition, install `python3` and `virtualenv`, e.g.
on Debian/Ubuntu:
```bash
sudo apt install python3 virtualenv python3-venv
```

## Running locally

To build and run the tool locally:
```bash
./build.sh && dev_appserver.py .
```

This will serve the tool at http://localhost:8080/.

## Deploying

To build and deploy to production (you will need to `gcloud auth login` first):
```bash
./build.sh && ./deploy.sh
```
