#!/usr/bin/env python3
"""Bloom — an optional at-a-glance status board for your terminal.

Renders status.json in the terminal, refreshing every 30 seconds.
Edit status.json by hand any time to update it.
"""

import json
import os
import sys
import time
from datetime import date, datetime

STATUS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "status.json")
REFRESH = 30

R = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[31m"
GRN = "\033[32m"
YEL = "\033[33m"
CYN = "\033[36m"
WHT = "\033[97m"

LEVEL_COLOR = {"red": RED, "amber": YEL, "green": GRN}
LEVEL_ICON = {"red": "🔴", "amber": "🟡", "green": "🟢"}


def term_width():
    try:
        return min(os.get_terminal_size().columns, 110)
    except OSError:
        return 100


def load_status():
    try:
        with open(STATUS) as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        return {"error": str(e)}


def days_until(datestr):
    try:
        d = datetime.strptime(datestr, "%Y-%m-%d").date()
        return (d - date.today()).days
    except ValueError:
        return None


def fmt_deadline(dl):
    delta = days_until(dl.get("date", ""))
    label = dl.get("label", "?")
    datestr = dl.get("date", "?")
    if delta is None:
        return f"{DIM}{datestr}{R}  {label}"
    if delta < 0:
        return f"{RED}{BOLD}OVERDUE {abs(delta)}d{R}  {label} ({datestr})"
    if delta == 0:
        return f"{RED}{BOLD}TODAY{R}  {label}"
    color = RED if delta <= 3 else YEL if delta <= 14 else GRN
    return f"{color}{BOLD}D-{delta}{R}  {label} ({datestr})"


def hr(w, ch="─"):
    return DIM + ch * w + R


def wrap(text, width, indent):
    words = str(text).split()
    lines, cur = [], ""
    for word in words:
        if cur and len(cur) + 1 + len(word) > width - indent:
            lines.append(cur)
            cur = word
        else:
            cur = f"{cur} {word}".strip()
    if cur:
        lines.append(cur)
    pad = " " * indent
    return [(pad if i else "") + ln for i, ln in enumerate(lines)]


def render(data):
    w = term_width()
    out = []
    now = datetime.now().strftime("%a %d %b %Y  %H:%M:%S")
    title = f"{BOLD}{WHT}⚔  BLOOM{R}"
    out.append(f"{title}{' ' * max(1, w - 26 - len(now))}{DIM}{now}{R}")
    out.append(hr(w, "═"))

    if "error" in data:
        out.append(f"{RED}Cannot read status.json: {data['error']}{R}")
        return "\n".join(out)

    updated = data.get("updated", "?")
    out.append(f"{DIM}intel updated: {updated}   ·   refresh: {REFRESH}s   ·   edit: status.json{R}")
    out.append("")

    # Countdown strip — all deadlines across fronts, soonest first
    all_dl = []
    for key, front in data.get("fronts", {}).items():
        for dl in front.get("deadlines", []):
            all_dl.append((dl.get("date", "9999-99-99"), key.upper(), dl))
    all_dl.sort()
    if all_dl:
        out.append(f"{BOLD}{CYN}⏱  COUNTDOWNS{R}")
        for _, tag, dl in all_dl[:8]:
            out.append(f"   {fmt_deadline(dl)} {DIM}[{tag}]{R}")
        out.append("")

    for key, front in data.get("fronts", {}).items():
        if not front:
            continue
        lvl = front.get("level", "amber")
        color = LEVEL_COLOR.get(lvl, YEL)
        icon = LEVEL_ICON.get(lvl, "🟡")
        name = front.get("name", key.upper())
        out.append(f"{icon} {BOLD}{color}{name}{R}  {DIM}·{R} {front.get('status', '')}")
        for item in front.get("items", [])[:5]:
            out.extend("   " + ln for ln in wrap(f"• {item}", w, 5))
        actions = front.get("actions", [])
        if actions:
            out.append(f"   {DIM}next:{R} {YEL}{actions[0]}{R}")
        out.append("")

    pris = data.get("priorities", [])
    if pris:
        out.append(hr(w))
        out.append(f"{BOLD}{WHT}🎯 PRIORITY STACK (do in order){R}")
        for i, p in enumerate(pris[:6], 1):
            out.extend("   " + ln for ln in wrap(f"{i}. {p}", w, 6))
    return "\n".join(out)


def main():
    once = "--once" in sys.argv
    while True:
        data = load_status()
        sys.stdout.write("\033[2J\033[H" if not once else "")
        print(render(data))
        if once:
            return
        try:
            time.sleep(REFRESH)
        except KeyboardInterrupt:
            print(f"\n{DIM}war room closed{R}")
            return


if __name__ == "__main__":
    main()
