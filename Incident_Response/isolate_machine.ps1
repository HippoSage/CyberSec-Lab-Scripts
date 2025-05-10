# Blocks all inbound and outbound connections to isolate a Windows machine from the network
New-NetFirewallRule -DisplayName "IsolateHost-Out" -Direction Outbound -Action Block -Enabled True -Profile Any
New-NetFirewallRule -DisplayName "IsolateHost-In" -Direction Inbound -Action Block -Enabled True -Profile Any
