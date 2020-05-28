# Flask-RestX Server Starter

## Requirements

[Python 3.7](https://www.python.org/downloads/release/python-374/)
[Pip](https://pip.pypa.io/en/stable/installing/)
[Virtualenv](https://virtualenv.pypa.io/en/latest/installation/) or equivalent

## Install

```bash
# Select Python 3.7
virtualenv -p python3.7 .env
source .env/bin/activate

# Install packages
pip install -r requirements.txt
```

Last, you need to copy `settings.json` from app.teamsid.com (search: `M2Gen SSO settings.json`) into the server's `./saml` subdirectory.

## Run

```bash
./dev-server.sh
```

That's it!

You can customize your development environment by editing the `./config.py` file. For example, you can disable SSO/SAML and disable HTTPS.

## Custom Development Config

You can create this file and override the server's config for your local dev environment. It is automatically .gitignored:

`instance/config.cfg` This example is useful for local, auth-less dev:

```
AUTH_REQUIRED = False
SERVER_PORT = 5000
SSL_ENABLED = False
```

## API

### Endpoints

#### Example

http://localhost:5000/api/1/example
