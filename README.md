[![Meya build](https://github.com/meya-customers/front-demo/actions/workflows/meya.check-test.yaml/badge.svg)](https://github.com/meya-customers/front-demo/actions/workflows/meya.check-test.yaml)

# Front demo

Basic template BFML and Python code that runs on Meya.

# Video walkthrough
In this demo, you'll learn how to:

* extract multiple intents from an email
* handle email and chat with separate flows
* transfer control to and from a Front agent

Video walkthrough:
* [Part 1: Demo](https://www.loom.com/share/9d5416824eb64395835f9ff563733cf8)
* [Part 2: Email use-case](https://www.loom.com/share/fbc596c60741481e93e69461406f6183)
* [Part 3: Orb use-case](https://www.loom.com/share/344d65e80fa944f998fefdadbf651c72)

## Setup

```shell script
brew install python@3.8 libgit2
MEYA_AUTH_TOKEN=your_meya_auth_token
MEYA_APP_ID=app-your_app_id
# you can optionally setup a venv instead as well
python3 -m venv venv  # optional
. venv/bin/activate  # optional
pip3 install --upgrade \
    --extra-index-url https://meya:$MEYA_AUTH_TOKEN@grid.meya.ai/registry/pypi \
    "pygit2>=1.2.1" \
    "meya-sdk>=2.0.0" \
    "meya-cli>=2.0.0"
# auth (if needed)
meya auth add --auth-token $MEYA_AUTH_TOKEN
# connect to existing app
meya connect --app-id $MEYA_APP_ID
```

## Workflow
```shell script 
meya check
meya format
meya test --watch
# to download secrets
meya vault download --file vault.secret.yaml
# if new secrets (after changing the yaml file)
meya vault upload --file vault.secret.yaml
meya push --watch
# for a full rebuild (useful for production deployments)
meya push --force --build-image
```

## Setup guides
* [Front](https://docs.meya.ai/docs/how-to-setup-a-front-integration)
* [Orb](https://docs.meya.ai/docs/how-to-set-up-an-orb-integration)
* [Dialogflow](https://docs.meya.ai/docs/how-to-set-up-a-dialogflow-integration)
