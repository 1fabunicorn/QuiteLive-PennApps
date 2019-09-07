#!/usr/bin/env bash
cd app && gunicorn3 -b localhost:5000 --pid=app.pid threadstesting:app