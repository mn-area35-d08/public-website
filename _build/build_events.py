"""Generate events/index.html from updates/events/YYYY.toml."""

from typing import Any

from build_shared import EVENTS_DIR, OUT_EVENTS, esc, fmt_date_range, is_past, load_toml, load_template, location_cell, render, wrap_page


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

