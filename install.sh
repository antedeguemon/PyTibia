#!/bin/bash
if [[ $EUID != 0 ]]; then
    echo "You need to be root to use this script."
    exit 1
fi

gcc pytibia/readmem.c -o readmem
mv readmem /usr/bin/readmem
rm pytibia/readmem.c

if [[ ! -f /usr/bin/readmem ]]; then
    echo "Cannot move readmem to /usr/bin directory."
fi