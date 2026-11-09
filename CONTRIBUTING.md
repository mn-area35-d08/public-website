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

That's it!
The website [meetings page](https://mn-area35-d08.github.io/public-website/meetings/)
will update automatically based on the new information.
Allow about 10 minutes for the change to take effect.

### Meetings: Update Example

For example, to change the Orr Tuesday Night meeting from 8 pm to 7 pm.

1. Open [updates/meeting.toml](./updates/meetings.toml).
2. Click the pencil icon (Edit this file).
3. Scroll to Tuesday and find the Orr meeting information:

   ```toml
   [[meeting]]
   day     = "Tuesday"
   time    = "8:00pm"
   name    = "Orr Tuesday Night"
   type    = "Closed"
   venue   = "Holy Cross Church"
   address = "10696 Shady Grove Lane"
   city    = "Orr"
   state   = "MN"
   zip     = "55771"
   ```

4. Change: "8:00pm" to "7:00pm".
5. Click **Commit changes**.
6. Enter a short description of your changes
   (e.g., `Change Orr Tuesday meeting to 7 pm`) and commit/save.

---

## Events: Add a New Event

1. Open [2027.toml](public-website/events/2027.toml).
2. Click the pencil icon (Edit this file).
3. Find the event just before the one you want to add.
4. Copy and paste the prior event information block to make a new one.
5. Edit the new one to reflect the new event information.
6. Click **Commit changes**.
7. Enter a short description (e.g., `Added new Jan 14 event`) and commit/save.

That's it!
The website [events page](https://mn-area35-d08.github.io/public-website/events/)
will update automatically based on the new information.
Allow about 10 minutes for the change to take effect.

### Events: Add Example

For example, to add a new event.

1. Open [updates/meeting.toml](./updates/meetings.toml).

2. Scroll to Tuesday and find the Orr meeting information:

   ```toml
   [[meeting]]
   day     = "Tuesday"
   time    = "8:00pm"
   name    = "Orr Tuesday Night"
   type    = "Closed"
   venue   = "Holy Cross Church"
   address = "10696 Shady Grove Lane"
   city    = "Orr"
   state   = "MN"
   zip     = "55771"
   ```

3. Change: "8:00pm" to "7:00pm".

---

## Other Website Changes

For other updates, find the corresponding file, click the pencil icon, make your changes, and commit.

GitHub automatically maintains the history of every change. No separate change log is required.
