# SWAG Nginx Configuration Dashboard

A Python parser and visualization dashboard tool for inspectable mappings of Nginx reverse-proxy configuration files (specifically tailored for LinuxServer.io SWAG - Secure Web Application Gateway containers).

## Purpose
- Scans `site-confs` and `proxy-confs` directory trees.
- Extracts upstream backends, subdomains, subfolders, and port mappings.
- Outputs structural mapping of reverse-proxied routes and DuckDNS/domain targets.

## Usage
```bash
python swag-dashboard.py
```
