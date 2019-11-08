
# upsty

Fast CLI upload for [psty.io](https://psty.io)

Uses S3 Bucket for hosting files. Fully configurable.

# Running

Requires:

- Python 3
- S3 Bucket Access and Credentials
- A Server To Host The API

Steps:

First install the required Python packages. Do so by running: `pip install -r requirements.txt`

After doing this make sure to set your environment variables for `AWS_ACCESS_KEY` and `AWS_SECRET_KEY`. 

Then go into `app/__init__.py` and setup the rest of your config to suit your setup.

Run `flask run` or use uWSGI or Gunicorn and you're off to the races!