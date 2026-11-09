# Updating the District 8 Website

Collaborators can update website information directly in GitHub.
No software or experience is needed.

## Becoming an Editor

1. Sign up for a free GitHub account.
2. Request access to our
   [GitHub organization](https://github.com/mn-area35-d08) from
   `dcm8@area35.org` or `dist8area35webmanager@gmail.com`.

## Accessing the Website Repository

Go to our [public-website repository](https://github.com/mn-area35-d08/public-website).

---

## Meetings: Make an Update

1. Open [meetings.toml](public-website/updates/meetings.toml).
2. Click the pencil icon (Edit this file).
3. Find the meeting you want to update.
4. Change only the information that needs updating.
5. Click **Commit changes**.
6. Enter a short description of your changes and commit/save.

The website [meetings page](https://mn-area35-d08.github.io/public-website/meetings/)
will update automatically based on the new information.
Allow about 10 minutes for the change to take effect.

### Meetings: Example

For example, to change the Orr Tuesday Night meeting time.

1. Open [updates/meetings.toml](https://github.com/mn-area35-d08/public-website/blob/main/updates/meetings.toml).
2. Click the pencil icon (Edit this file).
3. Scroll to Tuesday and find the Orr meeting information:

   ```toml
   [[meeting]]
   day     = "Tuesday"
   time    = "7:00pm"
   name    = "Orr Tuesday Night"
   type    = "Closed"
   venue   = "Holy Cross Church"
   address = "10696 Shady Grove Lane"
   city    = "Orr"
   state   = "MN"
   zip     = "55771"
   ```

4. Change: "7:00pm" to "6:00pm" (or whatever the correct time is and be sure to put it in quotes).
5. Click **Commit changes**.
6. Enter a short description of your changes
   (e.g., `Change Orr Tuesday meeting time`) and commit/save.

---

## Events: Add a New Event

Events have one data file per year.
The exact file will depend on the year of the event.

For example, if editing a 2027 event:

1. Open [events/2027.toml](https://github.com/mn-area35-d08/public-website/blob/main/updates/events/2027.toml).
2. Click the pencil icon (Edit this file).
3. Find the event just before the one you want to add.
4. Copy and paste the prior event information block to make a new one.
5. Edit the new one to reflect the new event information.
6. Click **Commit changes**.
7. Enter a short description (e.g., `Added new Jan 14 event`) and commit/save.

The website [events page](https://mn-area35-d08.github.io/public-website/events/)
will update automatically based on the new information.
Allow about 10 minutes for the change to take effect.

### Events: Example

For example, to add a new event.

1. Open [events/2027.toml](https://github.com/mn-area35-d08/public-website/blob/main/updates/events/2027.toml).
2. Click the pencil icon (Edit this file).
3. Find the event just before the one you want to add.
4. Copy and paste the prior event information block to make a new one, for example:

   ```toml
   [[special]]
   date_start = 2027-03-05
   date_end   = 2027-03-07
   time       = "Fri-Sun Conference"
   name       = "West Central Regional Service Conference"
   city       = "Breezy Point"
   state      = "MN"
   info       = "District 8 hospitality volunteers"
   flyer_url = "https://www.area35.org/wp-content/uploads/2026/02/WCRAASC-Save-the-Date-Flyer-2027.pdf"
   ```

5. Edit the new one to reflect the new event information.

   ```toml
   [[special]]
   date_start = 2027-04-03
   date_end   = 2027-04-04
   time       = "Sat-Sun Assembly"
   name       = "Area 35 Spring Assembly"
   venue      = "Barker's Island Inn"
   city       = "Superior"
   state      = "WI"
   ```

6. Click **Commit changes**.
7. Enter a short description (e.g., `Added new 2027 event`) and commit/save.

The website [events page](https://mn-area35-d08.github.io/public-website/events/)
will update automatically based on the new information.
Allow about 10 minutes for the change to take effect.

---

## Other Website Changes

For other updates, find the corresponding file,
click the pencil icon, make your changes, and commit.

GitHub automatically maintains the history of every change.
