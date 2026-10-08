"""Generate meetings/index.html from updates/meetings.toml."""

from typing import Any

from build_shared import DATA, DAYS_ORDER, OUT_MEETINGS, esc, load_toml, load_template, maps_url, render, wrap_page


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

