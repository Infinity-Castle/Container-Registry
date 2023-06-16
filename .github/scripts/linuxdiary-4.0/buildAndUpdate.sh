#!/bin/bash

while read p; do
    IFS=' ' 
    read -a line <<<"$p"
    sha256sum ${line[0]} > ${line[1]}

    IFS='/'
    read -a strarr <<<"${line[0]}"

    NAME_ARR=("${strarr[@]:6:2}")

    DIRECTORY_ARR=("${strarr[@]::${#strarr[@]}-1}")

    NAME=$(IFS=_ ; echo "${NAME_ARR[*]}")

    DIRECTORY=$(IFS=/ ; echo "${DIRECTORY_ARR[*]}")

    eval "cd ${DIRECTORY} && docker build -t ghcr.io/Infinity-Castle/${NAME}:latest ."
    eval "docker push ghcr.io/Infinity-Castle/${NAME}:latest"
done < /home/runner/work/Container-Registry/Container-Registry/.github/updates/linuxdiary-4.0

rm -f /home/runner/work/Container-Registry/Container-Registry/.github/updates/linuxdiary-4.0