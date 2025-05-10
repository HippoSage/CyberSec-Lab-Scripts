# -----------------------------------------------------------------------------
# Script: Host Isolation Script
# Author: By Gross
# Description: Blocks all inbound/outbound traffic to isolate a compromised host.
# Certifications: ISC2 CC, SSCP (in progress)
# Education: MS in Information Systems (Expected March 2026)
# GitHub: github.com/sarcasticwitwizard
# LinkedIn: linkedin.com/in/philliplgross
# -----------------------------------------------------------------------------

New-NetFirewallRule -DisplayName "IsolateHost-Out" -Direction Outbound -Action Block -Enabled True -Profile Any
New-NetFirewallRule -DisplayName "IsolateHost-In" -Direction Inbound -Action Block -Enabled True -Profile Any
