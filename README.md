<p align="center">
  <a align="center"><img src="https://github.com/psty-io/upsty/blob/master/github/UPSTY-banner.png?raw=true" /></a>
</p>

This repo contains the code for both the webapplication running on https://up.psty.io and also the command line tool that interfaces with it.

# About Upsty

Upsty is a tool that is inspired by https://transfer.sh which used to be nice to use until they kept having downtime. With the [service we host](https://psty.io) allowing file uploads and pastes, this felt like a nice additon to add.

# Backend

The backend folder contains the Flask application running the service. This is a simple single file Flask app that utilizes a config file in `backend/config.json`. Before starting development make sure to set up all the information inside of that config file.

# Command Line Tool

The command line tool is a `pip` program that you can install by running `pip install upsty`. This will remove the need for cURL and simply interfaces with the API on https://up.psty.io already.

# Credit

Written by [@MaxBridgland] 2019

# License

View [Here](https://github.com/psty-io/upsty/blob/master/LICENSE)
