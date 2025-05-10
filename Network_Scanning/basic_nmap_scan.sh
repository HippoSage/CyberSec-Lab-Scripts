#!/bin/bash

# -----------------------------------------------------------------------------
# Script: Basic Nmap Scan
# Author: By Gross
# Description: Performs a basic TCP SYN scan with version detection using Nmap.
# Certifications: ISC2 CC, SSCP (in progress)
# Education: MS in Information Systems (Expected March 2026)
# GitHub: github.com/sarcasticwitwizard
# LinkedIn: linkedin.com/in/philliplgross
# -----------------------------------------------------------------------------

echo "Enter target IP:"
read IP
nmap -sS -sV -T4 $IP
