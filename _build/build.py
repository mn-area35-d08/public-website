#!/usr/bin/env python3
"""
build.py — East Range D8 AA static site builder

Reads TOML data files and HTML templates, writes generated pages.

Run locally:  python _build/build.py
Triggered by: .github/workflows/build.yml on push to updates/** or nightly.
"""

# ============================================================
# Section 1. Imports
# ============================================================

import tomllib
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import quote_plus

# ============================================================
# Section 2. Paths and Constants
# ============================================================

ROOT         = Path(__file__).parent.parent
DATA         = ROOT / "updates"
TEMPLATES    = Path(__file__).parent / "templates"

EVENTS_DIR   = DATA / "events"
CONTACT_DIR  = DATA / "contact-us"

OUT_CONTACT  = ROOT / "contact"  / "index.html"
OUT_EVENTS   = ROOT / "events"   / "index.html"
OUT_MEETINGS = ROOT / "meetings" / "index.html"

TODAY = date.today()

DAYS_ORDER = [
    "Sunday", "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday",
]

CONTACT_GROUPS = ["District Officers", "District Chairs", "Web Managers"]

CONTACT_ANCHORS: dict[str, str] = {
    "District Officers": "officers",
    "District Chairs":   "chairs",
    "Web Managers":      "web-managers",
}

# ============================================================
# Section 3. Shared Helpers
# ============================================================

def load_toml(path: Path) -> dict[str, Any]:
    """Load and return a TOML file as a dict."""
    with open(path, "rb") as f:
        return tomllib.load(f)


def load_template(name: str) -> str:
    """Read a template file from _build/templates/."""
    return (TEMPLATES / name).read_text(encoding="utf-8")


def render(template: str, **replacements: str) -> str:
    """Replace {{KEY}} placeholders in template with provided values."""
    result = template
    for key, value in replacements.items():
        result = result.replace(f"{{{{{key}}}}}", value)
    return result


def esc(text: str) -> str:
    """Minimal HTML escaping for values sourced from TOML."""
    return (str(text)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">",  "&gt;")
            .replace('"', "&quot;"))


def maps_url(venue: str, address: str, city: str,
             state: str, zip_: str = "") -> str:
    """Build a Google Maps search URL from address components."""
    query = " ".join(filter(None, [venue, address, city, state, zip_]))
    return f"https://www.google.com/maps/search/?api=1&query={quote_plus(query)}"


def fmt_date(d: date) -> str:
    """Format a single date without platform-specific %-d."""
    return f"{d.strftime('%a %b')} {d.day}, {d.year}"


def fmt_date_range(start: date, end: date | None) -> str:
    """Format a single date or a date range for display."""
    if end is None or end == start:
        return fmt_date(start)
    if start.month == end.month and start.year == end.year:
        return (f"{start.strftime('%a')}-{end.strftime('%a')} "
                f"{start.strftime('%b')} {start.day}-{end.day}, {start.year}")
    return (f"{start.strftime('%a %b')} {start.day}-"
            f"{end.strftime('%a %b')} {end.day}, {end.year}")


def is_past(start: date, end: date | None) -> bool:
    """Return True if the event's last day is before today."""
    return (end if end else start) < TODAY


def location_cell(m: dict[str, Any]) -> str:
    """Build an HTML location string from a record's address fields."""
    parts: list[str] = []
    if m.get("venue") and m["venue"] != "TBD":
        parts.append(esc(m["venue"]))
    if m.get("address"):
        parts.append(esc(m["address"]))
    city_state = ", ".join(filter(None, [m.get("city", ""), m.get("state", "")]))
    if city_state:
        zip_ = m.get("zip", "")
        parts.append(esc(f"{city_state} {zip_}".strip()))
    loc = "<br>".join(parts) if parts else "TBD"
    if m.get("map_url"):
        loc += (f'\n              '
                f'<a href="{m["map_url"]}" target="_blank" rel="noopener noreferrer">Map</a>')
    return loc


def wrap_page(title: str, description: str,
              current_nav: str, main_content: str) -> str:
    """Assemble a complete HTML page from header/footer templates + content."""
    nav_items: list[tuple[str, str]] = [
        ("../",            "Home"),
        ("../meetings/",   "Meetings"),
        ("../events/",     "Events"),
        ("../resources/",  "Resources"),
        ("../forms/",      "Forms"),
        ("../contact/",    "Contact Us"),
        ("../contribute/", "Contribute to AA"),
    ]

    def nav_link(href: str, label: str) -> str:
        active = ' aria-current="page"' if label == current_nav else ""
        return f'<li><a href="{href}"{active}>{label}</a></li>'

    nav_links = "\n            ".join(nav_link(h, l) for h, l in nav_items)

    header = render(
        load_template("_header.html"),
        TITLE       = esc(title),
        DESCRIPTION = esc(description),
        NAV_LINKS   = nav_links,
    )
    footer = render(
        load_template("_footer.html"),
        YEAR = str(TODAY.year),
    )
    return header + main_content + footer




# ============================================================
# Section 4. Meetings Builder
# ============================================================

def _meeting_row(m: dict[str, Any]) -> str:
    """Return a <tr> string for one weekly meeting record."""
    url = maps_url(
        m.get("venue", ""), m.get("address", ""),
        m.get("city",  ""), m.get("state",   ""), m.get("zip", ""),
    )
    loc = (
        f'{esc(m.get("venue",   ""))}<br>'
        f'{esc(m.get("address", ""))}<br>'
        f'{esc(m.get("city", ""))}, {esc(m.get("state", ""))} '
        f'{esc(m.get("zip", ""))}<br>'
        f'<a href="{url}" target="_blank" rel="noopener noreferrer">Map</a>'
    )
    return (
        f'            <tr>\n'
        f'              <td>{esc(m.get("time",  ""))}</td>\n'
        f'              <td>{esc(m.get("name",  ""))}</td>\n'
        f'              <td>{esc(m.get("type",  ""))}</td>\n'
        f'              <td>{loc}</td>\n'
        f'            </tr>'
    )


def _day_section(day: str, meetings: list[dict[str, str]]) -> str:
    """Return a full <section> for one day's meetings."""
    rows = "\n".join(_meeting_row(m) for m in meetings)
    return f"""    <section id="{day.lower()}">
      <h2>{day}</h2>
      <div class="table-wrap">
        <table class="meetings-table">
          <thead>
            <tr>
              <th scope="col">Time</th>
              <th scope="col">Meeting</th>
              <th scope="col">Type</th>
              <th scope="col">Location</th>
            </tr>
          </thead>
          <tbody>
{rows}
          </tbody>
        </table>
      </div>
    </section>"""


def build_meetings() -> None:
    """Build meetings/index.html from updates/meetings.toml."""
    print("Building meetings page…")
    data     = load_toml(DATA / "meetings.toml")
    meetings = data.get("meeting", [])

    # Group by day, preserving canonical order
    by_day: dict[str, list[dict[str, str]]] = {d: [] for d in DAYS_ORDER}
    for m in meetings:
        day = m["day"]
        if day in by_day:
            by_day[day].append(m)
        else:
            print(f"  WARNING: unknown day '{day}' in meetings.toml — skipped")

    # Day navigation links
    day_nav_items = "".join(
        f'<li><a href="#{d.lower()}">{d}</a></li>\n        '
        for d in DAYS_ORDER if by_day[d]
    )
    day_nav = (
        f'    <nav class="day-nav" aria-label="Meetings by day">\n'
        f'      <ul>\n'
        f'        {day_nav_items.strip()}\n'
        f'      </ul>\n'
        f'    </nav>'
    )

    day_sections = "\n\n".join(
        _day_section(day, by_day[day])
        for day in DAYS_ORDER if by_day[day]
    )

    template = load_template("meetings.html")
    main     = render(template, DAY_NAV=day_nav, DAY_SECTIONS=day_sections)

    OUT_MEETINGS.parent.mkdir(parents=True, exist_ok=True)
    OUT_MEETINGS.write_text(
        wrap_page(
            "Meetings | East Range, MN D8 AA",
            "East Range AA meetings by day of week",
            "Meetings", main,
        ),
        encoding="utf-8",
    )
    print(f"  Written: {OUT_MEETINGS}")


# ============================================================
# Section 5. Events Builder
# ============================================================

def _district_as_event(m: dict[str, str]) -> dict[str, Any]:
    """Convert a [[district]] record to the same shape as [[special]]."""
    return {
        "date_start": m["date"],
        "date_end":   None,
        "time":       "District Mtg",
        "name":       f"{m.get('host', '')} Hosting",
        "venue":      m.get("venue",   ""),
        "address":    m.get("address", ""),
        "city":       m.get("city",    ""),
        "state":      m.get("state",   ""),
        "zip":        m.get("zip",     ""),
        "map_url":    m.get("map_url", ""),
        "info":       "Committee 6:30 PM / General 7:00 PM",
    }


def _event_row(e: dict[str, Any]) -> str:
    """Return a <tr> string for one event record."""
    start = e["date_start"]
    end   = e.get("date_end")
    css   = ' class="past-event"' if is_past(start, end) else ""

    info_parts: list[str] = []
    if e.get("flyer_url"):
        info_parts.append(
            f'<a href="{e["flyer_url"]}" target="_blank" rel="noopener noreferrer">Flyer Front</a>'
        )
    if e.get("flyer_back_url"):
        info_parts.append(
            f'<a href="{e["flyer_back_url"]}" target="_blank" rel="noopener noreferrer">Flyer Back</a>'
        )
    if e.get("info"):
        info_parts.append(esc(e["info"]))

    return (
        f'            <tr{css}>\n'
        f'              <td>{fmt_date_range(start, end)}</td>\n'
        f'              <td>{esc(e.get("time", ""))}</td>\n'
        f'              <td>{esc(e.get("name", ""))}</td>\n'
        f'              <td>{location_cell(e)}</td>\n'
        f'              <td>{"<br>".join(info_parts)}</td>\n'
        f'            </tr>'
    )


def build_events() -> None:
    """Build events/index.html from updates/events/YYYY.toml files."""
    print("Building events page…")
    year_files = sorted(EVENTS_DIR.glob("*.toml"))
    if not year_files:
        print("  WARNING: no TOML files found in updates/events/ — skipped")
        return

    # Merge all years; district records are normalized to event shape
    all_events: list[dict[str, Any]] = []
    for yf in year_files:
        data = load_toml(yf)
        all_events.extend(data.get("special", []))
        for m in data.get("district", []):
            all_events.append(_district_as_event(m))

    all_events.sort(key=lambda e: e["date_start"])

    events_rows = "\n".join(_event_row(e) for e in all_events)

    template = load_template("events.html")
    main     = render(template, EVENTS_ROWS=events_rows)

    OUT_EVENTS.parent.mkdir(parents=True, exist_ok=True)
    OUT_EVENTS.write_text(
        wrap_page(
            "Events | East Range, MN D8 AA",
            "East Range AA district events and meeting schedule",
            "Events", main,
        ),
        encoding="utf-8",
    )
    print(f"  Written: {OUT_EVENTS}")


# ============================================================
# Section 6. Contact Builder
# ============================================================

def _contact_row(e: dict[str, Any]) -> str:
    """Return a <tr> string for one contact directory entry."""
    # Position cell — Treasurer gets a link to reports
    position = esc(e.get("position", ""))
    if e.get("reports_url"):
        position += f' (<a href="{e["reports_url"]}">reports</a>)'

    # Email cell
    email     = e.get("email", "N/A")
    email_cell = (
        f'<a href="mailto:{esc(email)}">{esc(email)}</a>'
        if email and email != "N/A" else "N/A"
    )

    # Phone cell — prefer notes (multi-number) over plain phone
    phone_raw  = e.get("notes") or e.get("phone", "N/A")
    if phone_raw and phone_raw != "N/A":
        # Build a tel: link from the first number's digits
        first: str = phone_raw.split("/")[0].strip()
        digits     = "".join(c for c in first if c.isdigit())
        rest_parts = [p.strip() for p in phone_raw.split("/")[1:]]
        phone_cell = (
            f'<a href="tel:{digits}">{esc(first)}</a>'
            + ("".join(f"<br>{esc(p)}" for p in rest_parts) if rest_parts else "")
        ) if len(digits) >= 10 else esc(phone_raw)
    else:
        phone_cell = "N/A"

    return (
        f'            <tr>\n'
        f'              <td>{position}</td>\n'
        f'              <td>{esc(e.get("name", ""))}</td>\n'
        f'              <td>{email_cell}</td>\n'
        f'              <td>{phone_cell}</td>\n'
        f'            </tr>'
    )


def build_contact() -> None:
    """Build contact/index.html from updates/contact-us/YYYY.toml (latest year)."""
    print("Building contact page…")
    year_files = sorted(CONTACT_DIR.glob("*.toml"))
    if not year_files:
        print("  WARNING: no TOML files found in updates/contact-us/ — skipped")
        return

    # Use only the most recent year file for the live page;
    # older files are kept as an archive of past officers.
    data    = load_toml(year_files[-1])
    entries = data.get("entry", [])

    # Group entries preserving CONTACT_GROUPS order
    by_group: dict[str, list[dict[str, Any]]] = {g: [] for g in CONTACT_GROUPS}
    for e in entries:
        g = e.get("group", "")
        if g in by_group:
            by_group[g].append(e)
        else:
            print(f"  WARNING: unknown contact group '{g}' — skipped")

    rows_by_anchor: dict[str, str] = {
        CONTACT_ANCHORS[g]: "\n".join(_contact_row(e) for e in by_group[g])
        for g in CONTACT_GROUPS
    }

    template = load_template("contact.html")
    main     = render(
        template,
        OFFICERS_ROWS    = rows_by_anchor["officers"],
        CHAIRS_ROWS      = rows_by_anchor["chairs"],
        WEB_MANAGERS_ROWS= rows_by_anchor["web-managers"],
    )

    OUT_CONTACT.parent.mkdir(parents=True, exist_ok=True)
    OUT_CONTACT.write_text(
        wrap_page(
            "Contact Us | East Range, MN D8 AA",
            "Contact East Range District 8 AA officers and chairs",
            "Contact Us", main,
        ),
        encoding="utf-8",
    )
    print(f"  Written: {OUT_CONTACT}")


# ============================================================
# Final Section. Entry Point
# ============================================================

if __name__ == "__main__":
    print(f"Building site (today = {TODAY}) …")
    build_meetings()
    build_events()
    build_contact()
    print("Done.")