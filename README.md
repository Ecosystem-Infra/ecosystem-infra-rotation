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
python3 -m venv dev_env
source dev_env/bin/activate
python3 -m pip install -r requirements.txt
./build.sh
python3 main.py
```

This will serve the tool at http://localhost:8080/. Don't forget to exit the virtual environment when you are done:
```bash
deactivate
```

## Deploying

To build and deploy to production (you will need to `gcloud auth login` first):
```bash
./build.sh && ./deploy.sh
```
