#!/bin/bash

# -----------------------------------------------------------------------------
# Script: USB Insert Detection Script (SIEM Style)
# Author: By Gross
# Description: Monitors syslog for USB device insertions and logs events.
# Certifications: ISC2 CC, SSCP (in progress)
# Education: MS in Information Systems (Expected March 2026)
# GitHub: github.com/sarcasticwitwizard
# LinkedIn: linkedin.com/in/philliplgross
# -----------------------------------------------------------------------------

LOG_FILE="/var/log/syslog"  # Adjust this if your system uses /var/log/messages
OUTPUT_FILE="usb_alerts.log"
LAST_LINE=""

echo "USB Insert Detector by Gross"
echo "Monitoring $LOG_FILE for USB insertions..."
echo "[$(date)] Monitor started by Gross" >> $OUTPUT_FILE

while true; do
    LINE=$(tail -n 1 $LOG_FILE)

    if [[ "$LINE" != "$LAST_LINE" && "$LINE" =~ "usb" && "$LINE" =~ "storage" ]]; then
        TIMESTAMP=$(date)
        echo "[$TIMESTAMP] USB device detected: $LINE" >> $OUTPUT_FILE
        echo "ALERT: USB device plugged in at $TIMESTAMP"
    fi

    LAST_LINE="$LINE"
    sleep 5
done
