# -----------------------------------------------------------------------------
# Script: Failed SSH Login Parser
# Author: By Gross
# Description: Parses auth.log for failed SSH login attempts.
# Certifications: ISC2 CC, SSCP (in progress)
# Education: MS in Information Systems (Expected March 2026)
# GitHub: github.com/sarcasticwitwizard
# LinkedIn: linkedin.com/in/philliplgross
# -----------------------------------------------------------------------------

with open("/var/log/auth.log", "r") as file:
    for line in file:
        if "Failed password" in line:
            print(line.strip())
