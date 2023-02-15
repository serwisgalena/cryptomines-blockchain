#!/usr/bin/env bash
# Post install script for the UI .deb to place symlinks in places to allow the CLI to work similarly in both versions

set -e

ln -s /opt/cryptomines/resources/app.asar.unpacked/daemon/cryptomines /usr/bin/cryptomines || true
ln -s /opt/cryptomines/cryptomines-blockchain /usr/bin/cryptomines-blockchain || true
