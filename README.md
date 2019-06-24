# Lapis Bot Rewrite
* Developed by Fire and WWMB

## Purpose
This bot aids us on our server Valdrea doing whatever we need it to, if you want to self host, be my guest. =D

### Current features
* Scheduled Event Announcements (WIP)
  * Send announcements at a specific time (Done)
  * Allow for custom event messages (Done)
  * Command for adding/removing events from Discord (Done)
  * Command to reload the events.cfg file without a reboot (Done)
* Convert Overworld coordinates to Nether coordinates
* Convert temperature units
* Check the time in specific timezones
* Various Math functions
* Easily update bot with the github repository from inside Discord.
* Lapis Lord permission system
  * only people designated as Lapis Lords can run administrative commands
___
### Planned Additions
* Server activity tracking
  * Needs to be server specific, organizing data depending on the server
  * Track server, channel, and player stats, implemented in that order of priority
* Allow players to set their own time zone, and others to query it.
* Create `cogs.minecraft` to hold all minecraft related functions
  * Move the `+nether` command here
  * Add `+wiki` command to search the Minecraft Wiki and show any results (URL)
  * Add `+recipe` command, would be able to load the recipe files supplied by Mojang starting in the 1.12 behavior pack.
    * Modes:
      * `lookup`: The default, just shows the recipe and its output
      * `count`: If the recipe is given with a number in count mode, it will supply how many resources you'd need for that many recipes of that item, along with how many items you'll get
      * `items`: Kind of a reverse count, supply how many items you'd want and it'd give you how many recipes you'd need to make, along with the needed resources
      * `update`: Updates the recipes using the command's attached file (.zip) [Lapis Lord only]
___
### Planned Changes
* Rename `cogs.update` to `cogs.system`
  * Add `restart` command for restarting the bot [Lapis Lord only command]
  * Add `+restartpi` command for restarting the pi [Owner only command]
  * Add `+info` command that shows pi info, such as the uptime, the IP address, and CPU usage [Owner only command]
  * Add `+branch` command allowing us to switch the loaded branch
  * Add `+github` command that links to the Github repository.
___
### Current Priorities
* `cogs.system` commands completed
* Server Activity Tracking
* Decent Logging system
___
### Contributing
If you're feeling kind and you see a bug or issue that you can fix, feel free to make modifications and submit a pull request!
