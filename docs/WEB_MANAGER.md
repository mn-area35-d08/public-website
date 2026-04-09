# Web Manager Guide

## Duties

1. Manage the website regularly, checking its functionality
2. Keep website current with updated information
3. Track usage of the site and provide a monthly report to the district

## Weekly Reminder

Every Monday morning a [GitHub Issue](https://github.com/mn-area35-d08/public-website/issues)
is created automatically as a reminder to check the website. It includes a suggested list of tasks.

- See the [Issues](https://github.com/mn-area35-d08/public-website/issues) tab for open reminders
- See the automation at [`.github/workflows/weekly-web-check.yml`](../.github/workflows/weekly-web-check.yml)

## What Updates Automatically

The following pages rebuild themselves without any action from the web manager:

- **Events** - past events hide automatically every morning at midnight Central
- **Year rollover** - no action needed; just create a new `YYYY.toml` in `updates/events/` and `updates/contact-us/` each January

## Manually Update These When Things Change

| What changed                              | File to edit (update year as needed) |
| ----------------------------------------- | ------------------------------ |
| Weekly meeting added, removed, or changed | `updates/meetings.toml`        |
| New special event or district meeting     | `updates/events/2026.toml`     |
| Officer or chair name/phone/email         | `updates/contact-us/2026.toml` |
| Resource link added or changed            | `resources/index.html`         |
| Form link added or changed                | `forms/index.html`             |
| Contribution mailing address              | `contribute/index.html`        |

## How To Edit a File on GitHub

1. Navigate to the file in the repository
2. Click the **pencil icon** (Edit this file) near the top right
3. Make your changes
4. Click **Commit changes**, add a short note describing what you changed
5. Click **Commit** - the site updates within about 30 seconds

## Templates

Page structure (header, footer, nav) is controlled by files in `_build/templates/`.
Edit these if the site branding, navigation, or footer text needs to change.
Do not edit the generated output files in `meetings/`, `events/`, or `contact/` directly —
those are overwritten every time the build runs.

## Test the Build Locally

Requires [uv](https://docs.astral.sh/uv/) and Python 3.14.

```shell
uv python pin 3.14
uv run python _build/build.py
```

Generated files are written to `meetings/index.html`, `events/index.html`,
and `contact/index.html`. Review them in a browser before committing.

## Repository Layout

```
_build/
  build.py              # build script (runs automatically via GitHub Actions)
  templates/
    _header.html        # site header and nav
    _footer.html        # site footer
    meetings.html       # meetings page template
    events.html         # events page template
    contact.html        # contact page template

.github/workflows/
  build.yml             # rebuilds site on data change and nightly
  weekly-web-check.yml  # creates weekly reminder issue

contact/                # generated - do not edit directly
events/                 # generated - do not edit directly
meetings/               # generated - do not edit directly

docs/WEB_MANAGER.md     # this file

contribute/index.html   # edit directly
forms/index.html        # edit directly
resources/index.html    # edit directly

treasurer/              # treasurer uploads PDF reports here directly

updates/
  meetings.toml         # weekly AA meetings (edit to add/change/remove)
  events/2026.toml      # special events and district meetings
  contact-us/2026.toml  # officers, chairs, web managers
```
