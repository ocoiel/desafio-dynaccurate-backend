#!/bin/bash
# wait-for-it.sh
# Source: https://github.com/vishnubob/wait-for-it

host="$1"
port="$2"
timeout="${3:-60}"

shift 3
cmd="$@"

echo "Waiting for $host:$port..."

while ! nc -z "$host" "$port"; do
    sleep 1
    ((timeout--))

    if [[ $timeout -eq 0 ]]; then
        echo "Timeout occurred. Exiting."
        exit 1
    fi
done

echo "$host:$port is available."

exec $cmd
