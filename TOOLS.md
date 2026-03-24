# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Browser / Web Automation

I have full browser automation capability via the `browser` tool (Playwright + Chromium). I can:
- Open URLs, navigate, click, fill forms, take screenshots
- Log into websites with credentials
- Scrape content, extract data from pages
- Interact with web apps just like a human would

**I do NOT need the Chrome extension relay for this** — I have my own headless browser. Just give me a URL and/or credentials and I'll navigate myself.

Previously used to: browse leamymaths.ie, register for free trial, inspect course content, extract Vimeo video URLs.

### Leamy Maths Website Access
- **Test account:** leamyclaw+1@gmail.com / Openclaw2026 (student view)
- **Admin account:** leamyclaw+1@gmail.com (admin role granted by Jonny)
- ⚠️ **STRICT RULE: READ-ONLY. Do NOT make any changes to the site without explicit permission from Jonny.**

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
