#!/bin/sh
export PATH="/opt/poetry/bin:$PATH"
set -e
eval "exec $@"
