# Lapis Bot Rewrite
* Developed by Fire

## Purpose
This bot aids us on our server Valdrea doing whatever we need it to, if you want to self host, be my guest. =D

### Current features
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
* `cogs.playerdata'
  * Pulls data from our Player Data spreadsheet, displaying what is requested depending on the requesting user's permissions.
* Weather API tie-in
  * Let people request a weather report for an input area
* Google API tie-in
  * Google search from bot?
  * Could also allow us to search for locations directly from the Address Book.
* Dictionary.com API tie-in
  * Define word from search
  * Get synonyms or antonyms from search
* Improve Maths
  * Using Sympy, process math stuffs
___
### Current Priorities
* Optimize code, make more functional, sub commands
* Bug Fixing
* Data system upgrades
  * Finish functionalizing: deldir()
  * Possibly make tree creation by step instead of by folder.
    * Split at '/', check existence, make if necessary, go to next. More fluid and adaptable, compressable.
  * Let lapislords send/request files from Bot's Data.
    * Possible uses:
      * recipe interpretation
      * Add-On hosting
    * Possibly instead link to Google Drive
* Logging and Debug system upgrades
  * Save variable states to file
  * Change channel output to subscription based, sending to a list of channels who opt-in, instead of only one.
* Use git python package instead of hardwired console commands
* Rewrite cogs.system
  * Subcommand it
  * Fix lapislords
* Rewrite bot.py
  * Improve old code
___
### Contributing
If you're feeling kind and you see a bug or issue that you can fix, feel free to make modifications and submit a pull request!
