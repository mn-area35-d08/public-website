"""Generate contact/index.html from the latest updates/contact-us/YYYY.toml."""

from typing import Any

from build_shared import CONTACT_DIR, OUT_CONTACT, esc, load_toml, load_template, render, wrap_page


def _email_cell(entry: dict[str, Any]) -> str:
    """Return an email link, or N/A if none is provided."""
    email = entry.get("email", "N/A")
    if not email or email == "N/A":
        return "N/A"
    return f'<a href="mailto:{esc(email)}">{esc(email)}</a>'


def _officer_row(entry: dict[str, Any]) -> str:
    """Build a District Officers row: Position, Email."""
    position = esc(entry.get("position", ""))
    if entry.get("reports_url"):
        position += f' (<a href="{esc(entry["reports_url"])}">reports</a>)'
    return (
        f"            <tr>\n"
        f"              <td>{position}</td>\n"
        f"              <td>{_email_cell(entry)}</td>\n"
        f"            </tr>"
    )


def _chair_row(entry: dict[str, Any]) -> str:
    """Build a District Chairs row: Position, Email."""
    return (
        f"            <tr>\n"
        f"              <td>{esc(entry.get('position', ''))}</td>\n"
        f"              <td>{_email_cell(entry)}</td>\n"
        f"            </tr>"
    )


def _web_manager_row(entry: dict[str, Any]) -> str:
    """Build a Web Managers row: Position, Name, Email, Phone."""
    return (
        f"            <tr>\n"
        f"              <td>{esc(entry.get('position', ''))}</td>\n"
        f"              <td>{esc(entry.get('name', 'N/A'))}</td>\n"
        f"              <td>{_email_cell(entry)}</td>\n"
        f"              <td>{esc(entry.get('phone', 'N/A'))}</td>\n"
        f"            </tr>"
    )


def build_contact() -> None:
    """Build contact page using the latest annual contact file."""
    print("Building contact page…")
    year_files = sorted(CONTACT_DIR.glob("*.toml"))
    if not year_files:
        print("  WARNING: no TOML files found in updates/contact-us/ — skipped")
        return

    # Earlier year files remain as historical records.
    data = load_toml(year_files[-1])
    entries = data.get("entry", [])

    officers = [e for e in entries if e.get("group") == "District Officers"]
    chairs = [e for e in entries if e.get("group") == "District Chairs"]
    managers = [e for e in entries if e.get("group") == "Web Managers"]

    template = load_template("contact.html")
    main = render(
        template,
        OFFICERS_ROWS="\n".join(_officer_row(e) for e in officers),
        CHAIRS_ROWS="\n".join(_chair_row(e) for e in chairs),
        WEB_MANAGERS_ROWS="\n".join(_web_manager_row(e) for e in managers),
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
