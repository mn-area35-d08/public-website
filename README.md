# East Range, MN District 8 AA - Supplemental Public Website

[![Build success](https://github.com/mn-area35-d08/public-website/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/mn-area35-d08/public-website/actions/workflows/build.yml)
[![Link check](https://github.com/mn-area35-d08/public-website/actions/workflows/links.yml/badge.svg?branch=main)](https://github.com/mn-area35-d08/public-website/actions/workflows/links.yml)

This is a free supplemental website for East Range District 8 AA.
The main district website is at **[eastrangedist8.com](https://eastrangedist8.com/)**.

## Benefits of This Approach (GitHub Pages)

This site is hosted for free on GitHub Pages.
That helps when service positions turn over:

- **No hosting bill** - no credit card, no renewal, no account transfer
- **No shared passwords** - each person gets their own free GitHub account;
  access is added or removed by the web manager in seconds
- **No admin to hand off** - when an officer changes, just update their GitHub
  access; the new person picks up where the last one left off
- **No maintenance surprises** - no WordPress updates, no plugins, no PHP
  security patches; the site keeps working even if nobody touches it for months
- **Everything is backed up automatically** - GitHub keeps the full history of
  every change ever made, by whom, and when; nothing can be accidentally lost

## Working Folders

Updates are mostly confined to these folders:

| Folder       | What it holds                                                        |
| ------------ | -------------------------------------------------------------------- |
| `treasurer/` | Treasurer reports (uploaded directly by treasurer)                   |
| `updates/`   | **Data files** - edit these to update meetings, events, and contacts |

## How the Site Updates

Meetings, events, and contact information are kept in the `updates/` folder.
After an update, an automatic process runs and updates the website.
The badge at the top of this page shows whether the last automatic build
succeeded (green) or failed (red).

## How To: Add a New Event

1. Log in to [github.com](https://github.com) with your GitHub account.
2. Navigate to [`updates/events/2026.toml`](https://github.com/mn-area35-d08/public-website/blob/main/updates/events/2026.toml).
3. Click the **pencil icon** (Edit this file) near the top right.
4. Scroll to the bottom of the file.
5. Paste a new event block - copy the example below and fill in your details:

```toml
[[special]]
date_start = 2026-11-15
time       = "7pm Speaker"
name       = "Your Event Name Here"
venue      = "Venue Name"
address    = "123 Main St"
city       = "Virginia"
state      = "MN"
info       = "Any extra info here, or delete this line"
```

6. Check that the date format is `YYYY-MM-DD` and all lines look correct.
7. Click **Commit changes**, add a short note like `Add November speaker meeting`, and click **Commit**.

The event will appear on the website within about 30 seconds.
Past events hide automatically; no need to delete them.

## How To: Update a Contact

1. Navigate to [`updates/contact-us/2026.toml`](https://github.com/mn-area35-d08/public-website/blob/main/updates/contact-us/2026.toml).
2. Click the **pencil icon**.
3. Find the person's `[[entry]]` block and update their name, email, or phone.
4. Click **Commit changes**.

## How To: Upload a Treasurer Report

The treasurer folder is at [`treasurer/`](./treasurer/).
Upload PDF reports directly to that folder through the GitHub web interface:

1. Navigate to the [`treasurer/`](https://github.com/mn-area35-d08/public-website/tree/main/treasurer) folder.
2. Click **Add file / Upload files**.
3. Drag in the PDF or click to choose it.
4. Name the file clearly, e.g. `2026-03-treasurer-report.pdf`.
5. Click **Commit changes**.

The file will be linked from the treasurer page automatically.

## District Monthly Meetings

District 8 holds a **Committee Meeting at 6:30 PM** followed by the
**General District Committee Meeting at 7:00 PM**.
The location and day of the week changes each month.

| Date | Host Group | Location |
||-|-|
| Fri Jan 9 | Pike Sandy | Pike Town Hall, 6862 Co Hwy 68, Embarrass MN 55732 |
| Mon Feb 2 | Biwabik Sunday Night | United Church of Christ, 501 Main St, Biwabik MN 55708 |
| Tue Mar 3 | Cook Sunday Night | Trinity Lutheran Church, 231 2nd St E, Cook MN 55723 |
| Wed Apr 8 | Virginia Fri Night Open | St. Paul's Episcopal, 231 3rd St S, Virginia MN 55792 |
| Thu May 7 | Ely Happy, Joyous & Free | First Presbyterian, 226 E Harvey St, Ely MN 55731 |
| Fri Jun 12 | Ely Monday Women's | LedgeRock Community Church, 1515 E Camp St, Ely MN 55731 |
| Mon Jul 6 | Virginia Back to Basics | Peace United Methodist, 303 S 9th Ave W, Virginia MN 55792 |
| Tue Aug 4 | Virginia Fri Night Open | St. Paul's Episcopal, 231 3rd St S, Virginia MN 55792 |
| Wed Sep 9 | Gilbert Tuesday Night | St. Joseph's Catholic, 515 Summit St N, Gilbert MN 55741 |
| Thu Oct 8 | Virginia Fri Night Open | St. Paul's Episcopal, 231 3rd St S, Virginia MN 55792 |
| Fri Nov 6 | Aurora Big Book | Location TBD |
| Mon Dec 7 | Lake Vermilion 12×12 | Immanuel Lutheran, 304 Spruce St, Tower MN 55790 |

## Area and Sister Sites

- [Area 35](https://www.area35.org/) - Northern Minnesota
- [District 9: Hibbing](https://hibbingaread9aa.com/)
- [District 16: Grand Rapids](https://grandrapidsareamnaa.com/)

## Resources for Web Managers

- [Generate QR Codes](https://denisecase.github.io/qr-gen/) - useful for flyers
- [GitHub web editor guide](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files) - how to edit files on github.com without installing anything
