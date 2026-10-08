"""Build all pages locally or from GitHub Actions: python _build/build.py."""

from build_contact import build_contact
from build_events import build_events
from build_meetings import build_meetings
from build_shared import TODAY


def main() -> None:
    """Generate the meetings, events, and contact pages."""
    print(f"Building site (today = {TODAY}) …")
    build_meetings()
    build_events()
    build_contact()
    print("Done.")


if __name__ == "__main__":
    main()
