#!/usr/bin/env python3

import webbrowser
import logging
import sys

import toml

l = logging.getLogger(__name__)
l.setLevel(logging.INFO)

l.info("[+] Loading mod urls...")
with open("mods.toml") as fp:
    mods = toml.load(fp)

l.info("[+] Opening urls in web browser...")
for mod_name, mod_data in mods.items():
    platforms = mod_data.get("platforms", None)
    if platforms and sys.platform not in platforms:
        continue
    
    mod_url = mod_data.get("url", None)
    if not mod_url:
        l.critical(f"The mod {mod_name} had no URL... this is not good. Go fix it!") 
        continue 

    webbrowser.open_new_tab(mod_url)
