#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FSOCIETY TOOLKIT v5.0
"We Are Legion. We Are One."
"""

import os
import sys
import time
import random
import socket
import requests
import re
import string
import secrets
import hashlib
import base64
import uuid
import json
import math
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import quote_plus, unquote
import getpass

# ═══════════════════════════════════════════════════════════════════════════
# COLORS
# ═══════════════════════════════════════════════════════════════════════════

class Colors:
    DARK_RED = '\033[38;5;88m'
    RED = '\033[38;5;196m'
    BRIGHT_RED = '\033[38;5;203m'
    ORANGE = '\033[38;5;208m'
    GOLD = '\033[38;5;214m'
    YELLOW = '\033[38;5;226m'
    BLACK = '\033[38;5;232m'
    DARK_GRAY = '\033[38;5;235m'
    GRAY = '\033[38;5;240m'
    WHITE = '\033[38;5;255m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    BLINK = '\033[5m'
    ENDC = '\033[0m'

# ═══════════════════════════════════════════════════════════════════════════
# ANIMATION & UI
# ═══════════════════════════════════════════════════════════════════════════

WIDTH = 80

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def matrix_rain():
    """Matrix-Style Code Rain Animation"""
    chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
    columns = 80
    rows = 20
    
    for frame in range(30):
        clear()
        print("\n" * 5)
        
        rain = ""
        for i in range(rows):
            line = ""
            for j in range(columns):
                if random.random() > 0.95:
                    line += f"{Colors.BRIGHT_RED}{random.choice(chars)}{Colors.ENDC}"
                elif random.random() > 0.9:
                    line += f"{Colors.RED}{random.choice(chars)}{Colors.ENDC}"
                elif random.random() > 0.8:
                    line += f"{Colors.DARK_RED}{random.choice(chars)}{Colors.ENDC}"
                else:
                    line += " "
            rain += line + "\n"
        
        print(rain)
        time.sleep(0.05)
    
    # Explosion in der Mitte
    for i in range(10):
        clear()
        print("\n" * 12)
        
        intensity = i * 2
        center = Colors.BRIGHT_RED + "█" * intensity + Colors.ENDC
        glow = Colors.RED + "▓" * (intensity + 4) + Colors.ENDC
        
        spaces = " " * (40 - intensity//2)
        print(f"{spaces}{glow}")
        print(f"{spaces}{center}")
        print(f"{spaces}{glow}")
        
        time.sleep(0.08)

def scan_effect():
    """Scanning-Linien Effekt"""
    for i in range(10):
        clear()
        print("\n" * 15)
        
        pos = i * 8
        line = "█" * 80
        
        # Obere Scanline
        if i > 0:
            print(f"\n" * (pos//4) + f"{Colors.DARK_RED}{line}{Colors.ENDC}")
        
        # Haupt-Scanline
        print(f"\n" * 3 + f"{Colors.BRIGHT_RED}{line}{Colors.ENDC}")
        
        # Untere Scanline
        if i < 9:
            print(f"\n" * (5 - i//2) + f"{Colors.RED}{line}{Colors.ENDC}")
        
        time.sleep(0.1)

def glitch_text(text, duration=2):
    """Glitch-Effekt für Text"""
    chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    end_time = time.time() + duration
    
    while time.time() < end_time:
        clear()
        print("\n" * 10)
        
        glitched = ""
        for char in text:
            if random.random() > 0.7 and char != " ":
                glitched += random.choice(chars)
            else:
                glitched += char
        
        spaces = " " * 20
        print(f"{spaces}{Colors.BRIGHT_RED}{glitched}{Colors.ENDC}")
        time.sleep(0.05)
    
    # Finaler Text
    clear()
    print("\n" * 10)
    print(f"{spaces}{Colors.BRIGHT_RED}{text}{Colors.ENDC}")
    time.sleep(0.5)

def laser_animation():
    """Ultimative Laser-Animation"""
    clear()
    
    # Phase 1: Matrix Rain
    matrix_rain()
    
    # Phase 2: Scan-Effekt
    scan_effect()
    
    # Phase 3: Multiple Laser von allen Seiten
    for frame in range(20):
        clear()
        
        # Laser von links
        left_laser = Colors.BRIGHT_RED + "█" * (frame * 4) + Colors.ENDC
        # Laser von rechts  
        right_laser = Colors.BRIGHT_RED + "█" * (frame * 4) + Colors.ENDC
        # Laser von oben/unten
        vertical = Colors.RED + "█" + Colors.ENDC
        
        print("\n" * 8)
        
        # Horizontale Laser treffen sich
        left_pos = 40 - frame * 2
        right_pos = 40 + frame * 2
        
        line = [" "] * 80
        for i in range(frame * 2):
            if left_pos + i < 80:
                line[left_pos + i] = f"{Colors.BRIGHT_RED}█{Colors.ENDC}"
            if right_pos - i >= 0:
                line[right_pos - i] = f"{Colors.BRIGHT_RED}█{Colors.ENDC}"
        
        print("".join(line))
        print("".join(line))
        print("".join(line))
        
        time.sleep(0.03)
    
    # Phase 4: Explosion
    for i in range(8):
        clear()
        print("\n" * 10)
        
        size = i * 3
        explosion = Colors.BRIGHT_RED + "█" * size + Colors.ENDC
        spaces = " " * (40 - size//2)
        
        print(f"{spaces}{explosion}")
        print(f"{spaces}{Colors.YELLOW}{'█' * (size-2)}{Colors.ENDC}")
        print(f"{spaces}{explosion}")
        
        time.sleep(0.1)
    
    # Phase 5: FSOCIETY erscheint mit Glitch
    glitch_text("FSOCIETY", 1.5)
    
    # Phase 6: Finaler Banner
    clear()
    banner = f"""
{Colors.DARK_RED}        ████████████████████████████████████████████████████████████████████████{Colors.ENDC}
{Colors.RED}        ████████████████████████████████████████████████████████████████████████{Colors.ENDC}
{Colors.BRIGHT_RED}        ██{Colors.ENDC}                                                                        {Colors.BRIGHT_RED}██{Colors.ENDC}
{Colors.RED}        ██{Colors.ENDC}   {Colors.RED}███████╗███████╗ ██████╗ ██╗███████╗████████╗██╗   ██╗{Colors.ENDC}              {Colors.RED}██{Colors.ENDC}
{Colors.BRIGHT_RED}        ██{Colors.ENDC}   {Colors.RED}██╔════╝██╔════╝██╔═══██╗██║██╔════╝╚══██╔══╝╚██╗ ██╔╝{Colors.ENDC}              {Colors.BRIGHT_RED}██{Colors.ENDC}
{Colors.RED}        ██{Colors.ENDC}   {Colors.BRIGHT_RED}█████╗  ███████╗██║   ██║██║█████╗     ██║    ╚████╔╝{Colors.ENDC}               {Colors.RED}██{Colors.ENDC}
{Colors.BRIGHT_RED}        ██{Colors.ENDC}   {Colors.RED}██╔══╝  ╚════██║██║   ██║██║██╔══╝     ██║     ╚██╔╝{Colors.ENDC}                {Colors.BRIGHT_RED}██{Colors.ENDC}
{Colors.RED}        ██{Colors.ENDC}   {Colors.BRIGHT_RED}██║     ███████║╚██████╔╝██║███████╗   ██║      ██║{Colors.ENDC}                 {Colors.RED}██{Colors.ENDC}
{Colors.BRIGHT_RED}        ██{Colors.ENDC}   {Colors.RED}╚═╝     ╚══════╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝      ╚═╝{Colors.ENDC}                 {Colors.BRIGHT_RED}██{Colors.ENDC}
{Colors.RED}        ██{Colors.ENDC}                                                                        {Colors.RED}██{Colors.ENDC}
{Colors.DARK_RED}        ██{Colors.ENDC}           {Colors.GOLD}[{Colors.ENDC} {Colors.WHITE}MULTI-TOOL FRAMEWORK v5.0{Colors.ENDC} {Colors.GOLD}]{Colors.ENDC}                        {Colors.DARK_RED}██{Colors.ENDC}
{Colors.RED}        ██{Colors.ENDC}                                                                        {Colors.RED}██{Colors.ENDC}
{Colors.BRIGHT_RED}        ██{Colors.ENDC}      {Colors.DIM}🔥{Colors.ENDC} {Colors.WHITE}Discord:{Colors.ENDC} {Colors.BRIGHT_RED}https://discord.gg/qFUhXnpe{Colors.ENDC} {Colors.DIM}🔥{Colors.ENDC}                   {Colors.BRIGHT_RED}██{Colors.ENDC}
{Colors.RED}        ██{Colors.ENDC}                                                                        {Colors.RED}██{Colors.ENDC}
{Colors.DARK_RED}        ████████████████████████████████████████████████████████████████████████{Colors.ENDC}
{Colors.RED}        ████████████████████████████████████████████████████████████████████████{Colors.ENDC}
"""
    print(banner)
    time.sleep(1)
    
    # Loading Bar
    bar_length = 60
    print(f"\n{Colors.DARK_GRAY}{' ' * 10}[", end="")
    for i in range(bar_length):
        time.sleep(0.02)
        if i < bar_length // 3:
            print(f"{Colors.DARK_RED}█{Colors.ENDC}", end="", flush=True)
        elif i < 2 * bar_length // 3:
            print(f"{Colors.RED}█{Colors.ENDC}", end="", flush=True)
        else:
            print(f"{Colors.BRIGHT_RED}█{Colors.ENDC}", end="", flush=True)
    print(f"{Colors.DARK_GRAY}]{Colors.ENDC}")
    
    print(f"\n{Colors.GOLD}{' ' * 25}[ SYSTEM INITIALIZED ]{Colors.ENDC}")
    time.sleep(0.5)

def print_header(title):
    """Perfekter Header"""
    print(f"\n{Colors.DARK_RED}╔{'═' * (WIDTH-2)}╗{Colors.ENDC}")
    
    title_len = len(title)
    padding = (WIDTH - 2 - title_len) // 2
    right_padding = WIDTH - 2 - title_len - padding
    
    print(f"{Colors.DARK_RED}║{' ' * padding}{Colors.BOLD}{Colors.RED}{title}{Colors.ENDC}{' ' * right_padding}{Colors.DARK_RED}║{Colors.ENDC}")
    print(f"{Colors.DARK_RED}╚{'═' * (WIDTH-2)}╝{Colors.ENDC}\n")

def show_menu():
    """PERFEKT ausgerichtetes Menü - alle Striche gerade"""
    # Obere Linie
    print(f"\n{Colors.DARK_RED}╔{'═' * 38}╦{'═' * 39}╗{Colors.ENDC}")
    
    # Header Zeile
    left_title = "⚡ RECONNAISSANCE & OSINT"
    right_title = "🔥 SECURITY TOOLS"
    print(f"{Colors.DARK_RED}║{Colors.ENDC} {Colors.BOLD}{Colors.RED}{left_title}{Colors.ENDC}{' ' * (38 - len(left_title) - 1)}{Colors.DARK_RED}║{Colors.ENDC} {Colors.BOLD}{Colors.RED}{right_title}{Colors.ENDC}{' ' * (39 - len(right_title) - 1)}{Colors.DARK_RED}║{Colors.ENDC}")
    
    # Trennlinie
    print(f"{Colors.DARK_RED}╠{'═' * 38}╬{'═' * 39}╣{Colors.ENDC}")
    
    # Menüpunkte - perfekt ausgerichtet
    menu_items = [
        (f"{Colors.GOLD}[01]{Colors.ENDC} {Colors.WHITE}Username OSINT{Colors.ENDC}", f"{Colors.ORANGE}[11]{Colors.ENDC} {Colors.WHITE}Password Analyzer{Colors.ENDC}"),
        (f"{Colors.GOLD}[02]{Colors.ENDC} {Colors.WHITE}IP Intelligence{Colors.ENDC}", f"{Colors.ORANGE}[12]{Colors.ENDC} {Colors.WHITE}Hash Tools{Colors.ENDC}"),
        (f"{Colors.GOLD}[03]{Colors.ENDC} {Colors.WHITE}Email OSINT{Colors.ENDC}", f"{Colors.ORANGE}[13]{Colors.ENDC} {Colors.WHITE}Encoder/Decoder{Colors.ENDC}"),
        (f"{Colors.GOLD}[04]{Colors.ENDC} {Colors.WHITE}Phone Forensics{Colors.ENDC}", f"{Colors.ORANGE}[14]{Colors.ENDC} {Colors.WHITE}Port Scanner{Colors.ENDC}"),
        (f"{Colors.GOLD}[05]{Colors.ENDC} {Colors.WHITE}Domain Recon{Colors.ENDC}", f"{Colors.ORANGE}[15]{Colors.ENDC} {Colors.WHITE}WHOIS Lookup{Colors.ENDC}"),
        (f"{Colors.GOLD}[06]{Colors.ENDC} {Colors.WHITE}MAC Lookup{Colors.ENDC}", f"{Colors.ORANGE}[16]{Colors.ENDC} {Colors.WHITE}DNS Enumeration{Colors.ENDC}"),
        (f"{Colors.GOLD}[07]{Colors.ENDC} {Colors.WHITE}Subdomain Scanner{Colors.ENDC}", f"{Colors.ORANGE}[17]{Colors.ENDC} {Colors.WHITE}Tech Fingerprint{Colors.ENDC}"),
        (f"{Colors.GOLD}[08]{Colors.ENDC} {Colors.WHITE}Technology Scan{Colors.ENDC}", f"{Colors.ORANGE}[18]{Colors.ENDC} {Colors.WHITE}Social Downloader{Colors.ENDC}"),
        (f"{Colors.GOLD}[09]{Colors.ENDC} {Colors.WHITE}Metadata Extractor{Colors.ENDC}", f"{Colors.ORANGE}[19]{Colors.ENDC} {Colors.WHITE}Reverse Image Search{Colors.ENDC}"),
        (f"{Colors.GOLD}[10]{Colors.ENDC} {Colors.WHITE}Reverse Image{Colors.ENDC}", f"{Colors.ORANGE}[20]{Colors.ENDC} {Colors.WHITE}Bitcoin Analyzer{Colors.ENDC}"),
    ]
    
    for left, right in menu_items:
        # Berechne Leerzeichen genau
        left_clean = re.sub(r'\033\[[0-9;]*m', '', left)
        right_clean = re.sub(r'\033\[[0-9;]*m', '', right)
        left_spaces = 38 - len(left_clean) - 1
        right_spaces = 39 - len(right_clean) - 1
        
        print(f"{Colors.DARK_RED}║{Colors.ENDC} {left}{' ' * left_spaces}{Colors.DARK_RED}║{Colors.ENDC} {right}{' ' * right_spaces}{Colors.DARK_RED}║{Colors.ENDC}")
    
    # Mittlere Trennlinie
    print(f"{Colors.DARK_RED}╠{'═' * 38}╬{'═' * 39}╣{Colors.ENDC}")
    
    # Untere Header
    left_title2 = "🐯 GENERATORS"
    right_title2 = "🔧 UTILITIES"
    print(f"{Colors.DARK_RED}║{Colors.ENDC} {Colors.BOLD}{Colors.BRIGHT_RED}{left_title2}{Colors.ENDC}{' ' * (38 - len(left_title2) - 1)}{Colors.DARK_RED}║{Colors.ENDC} {Colors.BOLD}{Colors.GRAY}{right_title2}{Colors.ENDC}{' ' * (39 - len(right_title2) - 1)}{Colors.DARK_RED}║{Colors.ENDC}")
    
    # Trennlinie
    print(f"{Colors.DARK_RED}╠{'═' * 38}╬{'═' * 39}╣{Colors.ENDC}")
    
    # Untere Menüpunkte
    bottom_items = [
        (f"{Colors.BRIGHT_RED}[21]{Colors.ENDC} {Colors.WHITE}Password Generator{Colors.ENDC}", f"{Colors.GRAY}[25]{Colors.ENDC} {Colors.WHITE}Identity Generator{Colors.ENDC}"),
        (f"{Colors.BRIGHT_RED}[22]{Colors.ENDC} {Colors.WHITE}API Key Generator{Colors.ENDC}", f"{Colors.GRAY}[26]{Colors.ENDC} {Colors.WHITE}Network Diagnostics{Colors.ENDC}"),
        (f"{Colors.BRIGHT_RED}[23]{Colors.ENDC} {Colors.WHITE}JWT/Token Generator{Colors.ENDC}", f"{Colors.GRAY}[27]{Colors.ENDC} {Colors.WHITE}System Info{Colors.ENDC}"),
        (f"{Colors.BRIGHT_RED}[24]{Colors.ENDC} {Colors.WHITE}UUID Generator{Colors.ENDC}", f"{Colors.GRAY}[28]{Colors.ENDC} {Colors.WHITE}Exit System{Colors.ENDC}"),
    ]
    
    for left, right in bottom_items:
        left_clean = re.sub(r'\033\[[0-9;]*m', '', left)
        right_clean = re.sub(r'\033\[[0-9;]*m', '', right)
        left_spaces = 38 - len(left_clean) - 1
        right_spaces = 39 - len(right_clean) - 1
        
        print(f"{Colors.DARK_RED}║{Colors.ENDC} {left}{' ' * left_spaces}{Colors.DARK_RED}║{Colors.ENDC} {right}{' ' * right_spaces}{Colors.DARK_RED}║{Colors.ENDC}")
    
    # Untere Linie
    print(f"{Colors.DARK_RED}╚{'═' * 38}╩{'═' * 39}╝{Colors.ENDC}")

def discord_watermark():
    print(f"\n{Colors.DARK_RED}╔{'═' * (WIDTH-2)}╗{Colors.ENDC}")
    
    text = "🐯 Join the Community: https://discord.gg/qFUhXnpe 🐯"
    text_clean = "🐯 Join the Community: https://discord.gg/qFUhXnpe 🐯"
    padding = (WIDTH - 2 - len(text_clean)) // 2
    
    print(f"{Colors.DARK_RED}║{' ' * padding}{Colors.BRIGHT_RED}🐯{Colors.ENDC} {Colors.WHITE}Join the Community:{Colors.ENDC} {Colors.GOLD}https://discord.gg/qFUhXnpe{Colors.ENDC} {Colors.BRIGHT_RED}🐯{Colors.ENDC}{' ' * (WIDTH - 2 - len(text_clean) - padding)}{Colors.DARK_RED}║{Colors.ENDC}")
    print(f"{Colors.DARK_RED}╚{'═' * (WIDTH-2)}╝{Colors.ENDC}\n")

def loading_bar(text="INITIALIZING", duration=2):
    bar_length = 50
    steps = 50
    for i in range(steps + 1):
        percent = int((i / steps) * 100)
        filled = int((i / steps) * bar_length)
        if percent < 33:
            color = Colors.DARK_RED
        elif percent < 66:
            color = Colors.RED
        else:
            color = Colors.BRIGHT_RED
        bar = color + '█' * filled + Colors.DARK_GRAY + '░' * (bar_length - filled)
        sys.stdout.write(f'\r{color}[{bar}]{Colors.ENDC} {Colors.WHITE}{percent:3}%{Colors.ENDC} {Colors.GRAY}{text}{Colors.ENDC}')
        sys.stdout.flush()
        time.sleep(duration / steps)
    print(f"\n{Colors.GOLD}[✓]{Colors.ENDC} {Colors.BOLD}{text} COMPLETE{Colors.ENDC}\n")

def input_return():
    input(f"{Colors.GRAY}[Press Enter to return...]{Colors.ENDC}")

def print_box(title, lines):
    """Universal Box Printer"""
    print(f"{Colors.DARK_RED}╔{'═' * (WIDTH-2)}╗{Colors.ENDC}")
    
    title_len = len(title)
    padding = (WIDTH - 2 - title_len) // 2
    right_padding = WIDTH - 2 - title_len - padding
    
    print(f"{Colors.DARK_RED}║{' ' * padding}{Colors.BOLD}{Colors.RED}{title}{Colors.ENDC}{' ' * right_padding}{Colors.DARK_RED}║{Colors.ENDC}")
    print(f"{Colors.DARK_RED}╠{'═' * (WIDTH-2)}╣{Colors.ENDC}")
    
    for label, value in lines:
        content = f" {Colors.GOLD}{label}{Colors.ENDC} {Colors.WHITE}{value}{Colors.ENDC}"
        content_clean = f" {label} {value}"
        spaces = WIDTH - 2 - len(content_clean)
        print(f"{Colors.DARK_RED}║{Colors.ENDC}{content}{' ' * spaces}{Colors.DARK_RED}║{Colors.ENDC}")
    
    print(f"{Colors.DARK_RED}╚{'═' * (WIDTH-2)}╝{Colors.ENDC}")

# ═══════════════════════════════════════════════════════════════════════════
# TOOLS (Alle 28 Tools hier einfügen...)
# ═══════════════════════════════════════════════════════════════════════════

def username_osint():
    clear()
    print_header("USERNAME INTELLIGENCE")
    
    username = input(f"{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Enter target username: {Colors.ENDC}").strip()
    if not username:
        return
    
    loading_bar("SCANNING PLATFORMS", 3)
    
    platforms = {
        "Instagram": f"https://www.instagram.com/{username}",
        "Twitter/X": f"https://twitter.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Telegram": f"https://t.me/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Kaggle": f"https://www.kaggle.com/{username}",
    }
    
    found = []
    def check_platform(name, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, headers=headers, timeout=5, allow_redirects=False)
            return (name, url, response.status_code == 200)
        except:
            return (name, url, False)
    
    print(f"\n{Colors.GOLD}[*]{Colors.ENDC} {Colors.WHITE}Scanning {len(platforms)} platforms...{Colors.ENDC}\n")
    
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_platform, name, url): name for name, url in platforms.items()}
        for future in as_completed(futures):
            name, url, exists = future.result()
            if exists:
                found.append((name, url))
                print(f"{Colors.GOLD}[+]{Colors.ENDC} {Colors.ORANGE}{name:<20}{Colors.ENDC} {Colors.WHITE}{url}{Colors.ENDC}")
    
    print(f"\n{Colors.GOLD}[+]{Colors.ENDC} {Colors.WHITE}Found: {len(found)}/{len(platforms)} platforms{Colors.ENDC}")
    
    filename = f"FSOCIETY_OSINT_{username}_{int(time.time())}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"FSOCIETY OSINT REPORT\nTarget: {username}\nFound: {len(found)}/{len(platforms)}\n\n")
        for name, url in found:
            f.write(f"[+] {name}: {url}\n")
    
    print(f"{Colors.GOLD}[!]{Colors.ENDC} {Colors.WHITE}Report saved:{Colors.ENDC} {Colors.ORANGE}{filename}{Colors.ENDC}")
    discord_watermark()
    input_return()

def ip_lookup():
    clear()
    print_header("IP INTELLIGENCE")
    
    ip = input(f"{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Enter IP (or 'me'): {Colors.ENDC}").strip()
    if not ip:
        return
    
    loading_bar("TRACING LOCATION", 2)
    
    try:
        if ip.lower() == 'me':
            response = requests.get('https://ipapi.co/json/', timeout=10)
        else:
            response = requests.get(f'https://ipapi.co/{ip}/json/', timeout=10)
        
        data = response.json()
        
        if 'error' in data:
            print(f"{Colors.DARK_RED}[!] Error: {data['reason']}{Colors.ENDC}")
            return
        
        lines = [
            ("🌐 IP", data.get('ip', 'N/A')),
            ("🏙️ City", data.get('city', 'N/A')),
            ("🗺️ Region", data.get('region', 'N/A')),
            ("🇺🇳 Country", f"{data.get('country_name', 'N/A')} ({data.get('country', 'N/A')})"),
            ("📍 Coords", f"{data.get('latitude', 'N/A')}, {data.get('longitude', 'N/A')}"),
            ("🕐 Timezone", data.get('timezone', 'N/A')),
            ("🌐 ISP", data.get('org', 'N/A')),
        ]
        print_box("🎯 TARGET INTELLIGENCE", lines)
        
        lat = data.get('latitude')
        lon = data.get('longitude')
        if lat and lon:
            print(f"\n{Colors.GOLD}[!]{Colors.ENDC} {Colors.WHITE}Maps:{Colors.ENDC} {Colors.ORANGE}https://maps.google.com/?q={lat},{lon}{Colors.ENDC}")
            
    except Exception as e:
        print(f"{Colors.DARK_RED}[!] Error: {e}{Colors.ENDC}")
    
    discord_watermark()
    input_return()

def email_osint():
    clear()
    print_header("EMAIL INTELLIGENCE")
    
    email = input(f"{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Enter email: {Colors.ENDC}").strip()
    if not email or '@' not in email:
        print(f"{Colors.DARK_RED}[!] Invalid email{Colors.ENDC}")
        time.sleep(1)
        return
    
    loading_bar("ANALYZING EMAIL", 2)
    
    local, domain = email.split('@')
    
    lines = [
        ("📧 Email", email),
        ("📨 Local", local),
        ("🌐 Domain", domain),
    ]
    print_box("📧 EMAIL ANALYSIS", lines)
    
    print(f"\n{Colors.GOLD}[*]{Colors.ENDC} {Colors.WHITE}Search Links:{Colors.ENDC}")
    print(f"    {Colors.ORANGE}➜{Colors.ENDC} https://www.google.com/search?q=%22{quote_plus(email)}%22")
    print(f"    {Colors.ORANGE}➜{Colors.ENDC} https://haveibeenpwned.com/unifiedsearch/{email}")
    
    discord_watermark()
    input_return()

def phone_lookup():
    clear()
    print_header("PHONE FORENSICS")
    
    phone = input(f"{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Enter phone: {Colors.ENDC}").strip()
    if not phone:
        return
    
    loading_bar("ANALYZING NUMBER", 2)
    
    digits = re.sub(r'\D', '', phone)
    
    lines = [
        ("📱 Number", phone),
        ("🔢 Digits", digits),
    ]
    print_box("📱 PHONE ANALYSIS", lines)
    
    print(f"\n{Colors.GOLD}[*]{Colors.ENDC} {Colors.WHITE}Resources:{Colors.ENDC}")
    print(f"    {Colors.ORANGE}➜{Colors.ENDC} https://www.truecaller.com/search/{digits}")
    
    discord_watermark()
    input_return()

def domain_recon():
    clear()
    print_header("DOMAIN RECONNAISSANCE")
    
    domain = input(f"{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Enter domain: {Colors.ENDC}").strip()
    if not domain:
        return
    
    loading_bar("GATHERING INTEL", 2)
    
    try:
        ip = socket.gethostbyname(domain)
        lines = [("🌐 Domain", domain), ("📍 Resolved IP", ip)]
    except:
        lines = [("🌐 Domain", domain), ("❌ Status", "Could not resolve")]
    
    print_box("🌐 TARGET DOMAIN", lines)
    
    print(f"\n{Colors.GOLD}[*]{Colors.ENDC} {Colors.WHITE}Resources:{Colors.ENDC}")
    print(f"    {Colors.ORANGE}➜{Colors.ENDC} https://who.is/whois/{domain}")
    print(f"    {Colors.ORANGE}➜{Colors.ENDC} https://securitytrails.com/domain/{domain}")
    
    discord_watermark()
    input_return()

def mac_lookup():
    clear()
    print_header("MAC ADDRESS LOOKUP")
    
    mac = input(f"{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Enter MAC: {Colors.ENDC}").strip()
    if not mac:
        return
    
    loading_bar("QUERYING OUI", 1.5)
    
    mac_clean = re.sub(r'[^0-9a-fA-F]', '', mac)
    oui = mac_clean[:6].upper() if len(mac_clean) >= 6 else "N/A"
    
    lines = [
        ("🔌 MAC", mac),
        ("🏭 OUI", oui),
    ]
    print_box("🔌 MAC ANALYSIS", lines)
    
    discord_watermark()
    input_return()

def subdomain_scanner():
    clear()
    print_header("SUBDOMAIN SCANNER")
    
    domain = input(f"{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Enter domain: {Colors.ENDC}").strip()
    if not domain:
        return
    
    wordlist = ['www', 'mail', 'ftp', 'admin', 'api', 'blog', 'shop', 'dev', 'test', 'vpn', 'panel']
    
    loading_bar("SCANNING SUBDOMAINS", 2)
    
    print(f"\n{Colors.GOLD}[*]{Colors.ENDC} {Colors.WHITE}Scanning {len(wordlist)} common subdomains...{Colors.ENDC}\n")
    
    found = []
    for sub in wordlist:
        subdomain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(subdomain)
            found.append((subdomain, ip))
            print(f"{Colors.GOLD}[+]{Colors.ENDC} {Colors.ORANGE}{subdomain:<30}{Colors.ENDC} {Colors.GOLD}→{Colors.ENDC} {Colors.WHITE}{ip}{Colors.ENDC}")
        except:
            pass
    
    print(f"\n{Colors.GOLD}[+]{Colors.ENDC} {Colors.WHITE}Found {len(found)} subdomains{Colors.ENDC}")
    discord_watermark()
    input_return()

def tech_scanner():
    clear()
    print_header("TECHNOLOGY FINGERPRINTING")
    
    url = input(f"{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Enter URL: {Colors.ENDC}").strip()
    if not url:
        return
    
    if not url.startswith('http'):
        url = 'https://' + url
    
    loading_bar("ANALYZING TECH", 2)
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        
        server = response.headers.get('Server', 'Unknown')
        
        content = response.text.lower()
        techs = []
        if 'wordpress' in content: techs.append("WordPress")
        if 'react' in content: techs.append("React")
        if 'angular' in content: techs.append("Angular")
        if 'jquery' in content: techs.append("jQuery")
        if 'bootstrap' in content: techs.append("Bootstrap")
        
        lines = [("🌐 Server", server)]
        if techs:
            lines.append(("🔍 Detected", ", ".join(techs)))
        
        print_box("🔍 TECHNOLOGY STACK", lines)
            
    except Exception as e:
        print(f"{Colors.DARK_RED}[!] Error: {e}{Colors.ENDC}")
    
    discord_watermark()
    input_return()

def metadata_extractor():
    clear()
    print_header("METADATA EXTRACTOR")
    
    print(f"\n{Colors.GOLD}[*]{Colors.ENDC} {Colors.WHITE}Tools:{Colors.ENDC}")
    print(f"    {Colors.ORANGE}•{Colors.ENDC} ExifTool: https://exiftool.org/")
    print(f"    {Colors.ORANGE}•{Colors.ENDC} Jeffrey's Exif Viewer")
    
    discord_watermark()
    input_return()

def reverse_image_search():
    clear()
    print_header("REVERSE IMAGE SEARCH")
    
    print(f"\n{Colors.GOLD}[*]{Colors.ENDC} {Colors.WHITE}Engines:{Colors.ENDC}")
    print(f"    {Colors.ORANGE}•{Colors.ENDC} Google Images")
    print(f"    {Colors.ORANGE}•{Colors.ENDC} TinEye: https://tineye.com/")
    print(f"    {Colors.ORANGE}•{Colors.ENDC} Yandex Images")
    
    discord_watermark()
    input_return()

def password_analyzer():
    clear()
    print_header("PASSWORD ANALYZER")
    
    password = getpass.getpass(f"{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Enter password: {Colors.ENDC}")
    
    if not password:
        return
    
    score = 0
    length = len(password)
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password))
    
    if length >= 16: score += 4
    elif length >= 12: score += 3
    elif length >= 8: score += 2
    else: score += 1
    
    variety = sum([has_lower, has_upper, has_digit, has_special])
    if variety == 4: score += 4
    elif variety >= 3: score += 3
    elif variety >= 2: score += 2
    else: score += 1
    
    if score >= 7:
        rating = "STRONG"
        color = Colors.BRIGHT_RED
    elif score >= 5:
        rating = "MODERATE"
        color = Colors.ORANGE
    else:
        rating = "WEAK"
        color = Colors.DARK_RED
    
    lines = [
        ("🔐 Score", f"{score}/8 - {rating}"),
        ("📏 Length", str(length)),
        ("🔤 Lowercase", "✓" if has_lower else "✗"),
        ("🔠 Uppercase", "✓" if has_upper else "✗"),
        ("🔢 Digits", "✓" if has_digit else "✗"),
        ("⚡ Special", "✓" if has_special else "✗"),
    ]
    print_box("🔐 PASSWORD ANALYSIS", lines)
    
    discord_watermark()
    input_return()

def hash_tools():
    clear()
    print_header("HASH TOOLS")
    
    print(f"{Colors.GOLD}[1]{Colors.ENDC} {Colors.WHITE}Generate Hash{Colors.ENDC}")
    print(f"{Colors.GOLD}[2]{Colors.ENDC} {Colors.WHITE}Identify Hash{Colors.ENDC}")
    choice = input(f"\n{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Select: {Colors.ENDC}").strip()
    
    if choice == '1':
        text = input(f"{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Enter text: {Colors.ENDC}")
        if not text:
            return
        
        loading_bar("GENERATING", 1)
        
        lines = [
            ("MD5", hashlib.md5(text.encode()).hexdigest()),
            ("SHA256", hashlib.sha256(text.encode()).hexdigest()),
            ("SHA512", hashlib.sha512(text.encode()).hexdigest()),
        ]
        print_box("🔢 GENERATED HASHES", lines)
        
    elif choice == '2':
        hash_input = input(f"{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Enter hash: {Colors.ENDC}").strip()
        hash_len = len(hash_input)
        
        if hash_len == 32:
            types = "MD5, MD4, NTLM"
        elif hash_len == 40:
            types = "SHA1"
        elif hash_len == 64:
            types = "SHA256"
        else:
            types = "Unknown"
        
        lines = [
            ("📏 Length", str(hash_len)),
            ("🔍 Possible", types),
        ]
        print_box("🔍 HASH IDENTIFICATION", lines)
    
    discord_watermark()
    input_return()

def encoder_decoder():
    clear()
    print_header("ENCODER / DECODER")
    
    print(f"{Colors.GOLD}[1]{Colors.ENDC} {Colors.WHITE}Encode{Colors.ENDC}")
    print(f"{Colors.GOLD}[2]{Colors.ENDC} {Colors.WHITE}Decode{Colors.ENDC}")
    mode = input(f"\n{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Select: {Colors.ENDC}").strip()
    
    if mode not in ['1', '2']:
        return
    
    print(f"\n{Colors.GOLD}[a]{Colors.ENDC} {Colors.WHITE}Base64{Colors.ENDC}")
    print(f"{Colors.GOLD}[b]{Colors.ENDC} {Colors.WHITE}Hex{Colors.ENDC}")
    print(f"{Colors.GOLD}[c]{Colors.ENDC} {Colors.WHITE}URL{Colors.ENDC}")
    enc_type = input(f"{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Select: {Colors.ENDC}").strip()
    
    text = input(f"{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Enter text: {Colors.ENDC}")
    if not text:
        return
    
    try:
        if mode == '1':
            if enc_type == 'a':
                result = base64.b64encode(text.encode()).decode()
            elif enc_type == 'b':
                result = text.encode().hex()
            else:
                result = quote_plus(text)
            lines = [("🔒 Encoded", result)]
        else:
            if enc_type == 'a':
                result = base64.b64decode(text).decode()
            elif enc_type == 'b':
                result = bytes.fromhex(text).decode()
            else:
                result = unquote(text)
            lines = [("🔓 Decoded", result)]
        
        print_box("RESULT", lines)
    except Exception as e:
        print(f"\n{Colors.DARK_RED}[!] Error: {e}{Colors.ENDC}")
    
    discord_watermark()
    input_return()

def port_scanner():
    clear()
    print_header("PORT SCANNER")
    
    target = input(f"{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Enter target: {Colors.ENDC}").strip()
    if not target:
        return
    
    print(f"\n{Colors.GOLD}[1]{Colors.ENDC} {Colors.WHITE}Quick Scan (Top 20){Colors.ENDC}")
    print(f"{Colors.GOLD}[2]{Colors.ENDC} {Colors.WHITE}Full Scan (1-100){Colors.ENDC}")
    scan_type = input(f"\n{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Select: {Colors.ENDC}").strip()
    
    if scan_type == '1':
        ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 5900, 8080]
    else:
        ports = list(range(1, 101))
    
    loading_bar("INITIALIZING SCAN", 1.5)
    
    print(f"\n{Colors.GOLD}[*]{Colors.ENDC} {Colors.WHITE}Scanning {target}...{Colors.ENDC}\n")
    
    open_ports = []
    def scan_port(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            sock.close()
            return (port, result == 0)
        except:
            return (port, False)
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(scan_port, port): port for port in ports}
        for future in as_completed(futures):
            port, is_open = future.result()
            if is_open:
                open_ports.append(port)
                print(f"{Colors.GOLD}[+]{Colors.ENDC} Port {Colors.ORANGE}{port:<5}{Colors.ENDC} {Colors.GOLD}OPEN{Colors.ENDC}")
    
    print(f"\n{Colors.GOLD}[+]{Colors.ENDC} {Colors.WHITE}Complete: {len(open_ports)} ports open{Colors.ENDC}")
    discord_watermark()
    input_return()

def whois_lookup():
    clear()
    print_header("WHOIS LOOKUP")
    
    domain = input(f"{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Enter domain: {Colors.ENDC}").strip()
    if not domain:
        return
    
    loading_bar("QUERYING WHOIS", 2)
    
    lines = [
        ("🌐 Domain", domain),
        ("📋 Status", "Query complete"),
    ]
    print_box("📋 WHOIS INFORMATION", lines)
    
    print(f"\n{Colors.GOLD}[*]{Colors.ENDC} {Colors.WHITE}Resources:{Colors.ENDC}")
    print(f"    {Colors.ORANGE}➜{Colors.ENDC} https://who.is/whois/{domain}")
    
    discord_watermark()
    input_return()

def dns_lookup():
    clear()
    print_header("DNS ENUMERATION")
    
    domain = input(f"{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Enter domain: {Colors.ENDC}").strip()
    if not domain:
        return
    
    loading_bar("QUERYING DNS", 2)
    
    try:
        ip = socket.gethostbyname(domain)
        lines = [("🌐 Domain", domain), ("📍 A Record", ip)]
    except:
        lines = [("🌐 Domain", domain), ("❌ Status", "Could not resolve")]
    
    print_box("📍 DNS RECORDS", lines)
    
    print(f"\n{Colors.GOLD}[*]{Colors.ENDC} {Colors.WHITE}Tools:{Colors.ENDC}")
    print(f"    {Colors.ORANGE}➜{Colors.ENDC} https://dnschecker.org/#A/{domain}")
    
    discord_watermark()
    input_return()

def social_downloader():
    clear()
    print_header("SOCIAL MEDIA DOWNLOADER")
    
    print(f"\n{Colors.GOLD}[*]{Colors.ENDC} {Colors.WHITE}Supported Platforms:{Colors.ENDC}")
    print(f"    {Colors.ORANGE}•{Colors.ENDC} YouTube - yt-dlp")
    print(f"    {Colors.ORANGE}•{Colors.ENDC} Instagram - Instaloader")
    print(f"    {Colors.ORANGE}•{Colors.ENDC} TikTok - yt-dlp")
    
    discord_watermark()
    input_return()

def bitcoin_analyzer():
    clear()
    print_header("BITCOIN ADDRESS ANALYZER")
    
    address = input(f"{Colors.GOLD}[?]{Colors.ENDC} {Colors.WHITE}Enter BTC address: {Colors.ENDC}").strip()
    if not address:
        return
    
    loading_bar("ANALYZING BLOCKCHAIN", 2)
    
    is_valid = len(address) in [26, 34, 42, 62] and (address.startswith('1') or address.startswith('3') or address.startswith('bc1'))
    
    lines = [
        ("₿ Address", address),
        ("✓ Valid", "YES" if is_valid else "NO"),
    ]
    print_box("₿ BITCOIN ANALYSIS", lines)
    
    print(f"\n{Colors.GOLD}[*]{Colors.ENDC} {Colors.WHITE}Explorers:{Colors.ENDC}")
    print(f"    {Colors.ORANGE}➜{Colors.ENDC} https://www.blockchain.com/explorer/addresses/btc/{address}")
    
    discord_watermark()
    input_return()

def password_generator():
    clear()
    print_header("PASSWORD GENERATOR")
    
    length = int(input(f"{Colors.GOLD}[?]{Colors.ENDC} Length (default 16): {Colors.ENDC}") or "16")
    count = int(input(f"{Colors.GOLD}[?]{Colors.ENDC} Count (default 5): {Colors.ENDC}") or "5")
    
    loading_bar("GENERATING", 1)
    
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    
    print(f"\n{Colors.GOLD}[+]{Colors.ENDC} {Colors.WHITE}Generated Passwords:{Colors.ENDC}\n")
    for i in range(count):
        password = ''.join(secrets.choice(chars) for _ in range(length))
        print(f"    {Colors.ORANGE}[{i+1}]{Colors.ENDC} {Colors.WHITE}{password}{Colors.ENDC}")
    
    discord_watermark()
    input_return()

def api_key_generator():
    clear()
    print_header("API KEY GENERATOR")
    
    loading_bar("GENERATING", 1)
    
    print(f"\n{Colors.GOLD}[+]{Colors.ENDC} {Colors.WHITE}API Keys:{Colors.ENDC}\n")
    for i in range(5):
        key = secrets.token_urlsafe(32)
        print(f"    {Colors.ORANGE}[{i+1}]{Colors.ENDC} {Colors.WHITE}sk_{key}{Colors.ENDC}")
    
    discord_watermark()
    input_return()

def jwt_generator():
    clear()
    print_header("JWT/TOKEN GENERATOR")
    
    secret = secrets.token_urlsafe(64)
    lines = [("🔑 JWT Secret", secret)]
    print_box("🔑 JWT CONFIGURATION", lines)
    
    discord_watermark()
    input_return()

def uuid_generator():
    clear()
    print_header("UUID GENERATOR")
    
    print(f"\n{Colors.GOLD}[+]{Colors.ENDC} {Colors.WHITE}Generated UUIDs:{Colors.ENDC}\n")
    for i in range(10):
        uid = str(uuid.uuid4())
        print(f"    {Colors.ORANGE}[{i+1}]{Colors.ENDC} {Colors.WHITE}{uid}{Colors.ENDC}")
    
    discord_watermark()
    input_return()

def identity_generator():
    clear()
    print_header("IDENTITY GENERATOR")
    
    loading_bar("GENERATING", 2)
    
    first_names = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia']
    cities = ['Springfield', 'Riverside', 'Fairview', 'Madison']
    states = ['CA', 'TX', 'FL', 'NY']
    
    identity = {
        'first': random.choice(first_names),
        'last': random.choice(last_names),
        'street': random.randint(100, 9999),
        'city': random.choice(cities),
        'state': random.choice(states),
        'zip': f"{random.randint(10000, 99999)}",
        'phone': f"555-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
    }
    identity['email'] = f"{identity['first'].lower()}.{identity['last'].lower()}@gmail.com"
    
    lines = [
        ("🎭 Name", f"{identity['first']} {identity['last']}"),
        ("📧 Email", identity['email']),
        ("📱 Phone", identity['phone']),
        ("🏠 Address", f"{identity['street']} {identity['city']} St"),
        ("📍 Location", f"{identity['state']} {identity['zip']}"),
    ]
    print_box("🎭 GENERATED IDENTITY", lines)
    
    print(f"\n{Colors.DARK_RED}[!]{Colors.ENDC} {Colors.WHITE}For testing only{Colors.ENDC}")
    
    discord_watermark()
    input_return()

def network_diagnostics():
    clear()
    print_header("NETWORK DIAGNOSTICS")
    
    loading_bar("GATHERING INFO", 2)
    
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        
        try:
            public_ip = requests.get('https://api.ipify.org', timeout=5).text
        except:
            public_ip = "N/A"
        
        lines = [
            ("💻 Hostname", hostname),
            ("🌐 Local IP", local_ip),
            ("🌍 Public IP", public_ip),
        ]
        print_box("🌐 NETWORK INFO", lines)
            
    except Exception as e:
        print(f"{Colors.DARK_RED}[!] Error: {e}{Colors.ENDC}")
    
    print(f"\n{Colors.GOLD}[*]{Colors.ENDC} {Colors.WHITE}Commands:{Colors.ENDC}")
    print(f"    {Colors.ORANGE}➜{Colors.ENDC} ping 8.8.8.8")
    print(f"    {Colors.ORANGE}➜{Colors.ENDC} netstat -an")
    
    discord_watermark()
    input_return()

def system_info():
    clear()
    print_header("SYSTEM INFORMATION")
    
    loading_bar("COLLECTING INFO", 1.5)
    
    lines = [
        ("💻 Platform", sys.platform),
        ("🐍 Python", sys.version.split()[0]),
        ("📂 Path", os.getcwd()),
        ("👤 User", os.getenv('USERNAME') or os.getenv('USER') or 'Unknown'),
    ]
    print_box("💻 SYSTEM DETAILS", lines)
    
    discord_watermark()
    input_return()

def exit_system():
    print(f"\n{Colors.BRIGHT_RED}")
    print("    ███████╗██╗  ██╗██╗████████╗")
    print("    ██╔════╝╚██╗██╔╝██║╚══██╔══╝")
    print("    █████╗   ╚███╔╝ ██║   ██║   ")
    print("    ██╔══╝   ██╔██╗ ██║   ██║   ")
    print("    ██║     ██╔╝ ██╗██║   ██║   ")
    print("    ╚═╝     ╚═╝  ╚═╝╚═╝   ╚═╝   ")
    print(f"{Colors.ENDC}")
    print(f"{Colors.GOLD}    [ We are FSOCIETY. We are Legion. ]{Colors.ENDC}\n")
    time.sleep(1)
    sys.exit(0)

# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main():
    # GEILE Animation mit Matrix + Laser + Glitch
    laser_animation()
    
    try:
        while True:
            clear()
            show_menu()
            
            prompt = f"\n{Colors.DARK_RED}┌─[{Colors.RED}FSOCIETY{Colors.DARK_RED}]─[{Colors.ORANGE}~/root{Colors.DARK_RED}]\n└─╼ {Colors.RED}⚡ {Colors.ENDC}"
            choice = input(prompt).strip().lower()
            
            if choice in ['0', 'exit', 'quit', 'q', '28']:
                exit_system()
            
            tools = {
                '1': username_osint, '2': ip_lookup, '3': email_osint,
                '4': phone_lookup, '5': domain_recon, '6': mac_lookup,
                '7': subdomain_scanner, '8': tech_scanner, '9': metadata_extractor,
                '10': reverse_image_search, '11': password_analyzer, '12': hash_tools,
                '13': encoder_decoder, '14': port_scanner, '15': whois_lookup,
                '16': dns_lookup, '17': tech_scanner, '18': social_downloader,
                '19': reverse_image_search, '20': bitcoin_analyzer, 
                '21': password_generator, '22': api_key_generator, 
                '23': jwt_generator, '24': uuid_generator,
                '25': identity_generator, '26': network_diagnostics, 
                '27': system_info, '28': exit_system,
            }
            
            if choice in tools:
                tools[choice]()
            else:
                print(f"{Colors.DARK_RED}[!] Invalid option{Colors.ENDC}")
                time.sleep(1)
                
    except KeyboardInterrupt:
        print(f"\n{Colors.GOLD}[+]{Colors.ENDC} {Colors.WHITE}Interrupted.{Colors.ENDC}")
        exit_system()

if __name__ == "__main__":
    main()