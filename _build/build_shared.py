"""Shared paths and basic HTML/TOML helpers for site builders."""

import tomllib
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import quote_plus

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

