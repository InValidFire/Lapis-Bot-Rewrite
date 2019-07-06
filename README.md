# Lapis Bot Rewrite
* Developed by Fire and WWMB

## Purpose
This bot aids us on our server Valdrea doing whatever we need it to, if you want to self host, be my guest. =D

### Current features
* Scheduled Event Announcements
  * Send announcements at a specific time
  * Allow for custom event messages
  * Command for easily adding/removing events from Discord
* Convert Overworld coordinates to Nether coordinates and vice versa
* Map our custom Nether Grid system to any set of coordinates, and look up each location.
* Easily look up pages from the Minecraft Wiki
* Convert temperature units
* Check the time in specific timezones
* Various Math functions
* Easily update bot with the github repository from inside Discord.
* Lapis Lord permission system
  * only people designated as Lapis Lords can run administrative commands
___
### Planned Additions
* Expand `cogs.events` to enable creation of daily, monthly, and yearly events.
* Expand `cogs.data` to allow us to request and send files to and from the bot. [LL Only]
* `cogs.profile` to allow users to set things like their preferred nickname, time zone (from pytz), Xbox Gamertag, Steam Name, NNID, B-Day, the likes
  * Global or server specific?
  * Allow users to query other users profiles to see current time, and shown accounts
* `cogs.minecraft`
  * Add `+recipe` command, would be able to load the recipe files supplied by Mojang starting in the 1.12 behavior pack.
    * Modes:
      * `lookup`: The default, just shows the recipe and its output
      * `count`: If the recipe is given with a number in count mode, it will supply how many resources you'd need for that many recipes of that item, along with how many items you'll get
      * `items`: Kind of a reverse count, supply how many items you'd want and it'd give you how many recipes you'd need to make, along with the needed resources
      * `update`: Updates the recipes using the command's attached file (.zip) [Lapis Lord only]
* Weather API tie-in
  * Let people request a weather report for an input area
* Google API tie-in
  * Google search from bot?
  * Also potentially move the events stuff to a google sheet
  * Could also allow us to search for locations directly from the Address Book.
* Dictionary.com API tie-in
  * Define word from search
  * Get synonyms or antonyms from search
* PEMDAS command
  * Processes the given string with the order of operations
## Planned Changes
* Replace old timer.py with a more flexible system
* Load debug and logging variable states from file (saving state across reboot)
___
### Current Priorities
* Recipe Interpreter
  * Need to expand `cogs.data`
* Optimize code, make more functional
* Bug Fixing
* Logging and Debug system upgrades
___
### Contributing
If you're feeling kind and you see a bug or issue that you can fix, feel free to make modifications and submit a pull request!
