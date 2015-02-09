<h1>Sow</h1>
<h2>A Harvest Command Line Application</h2>
Sow is a command-line application for use with the Harvest Time Tracking API. It relies on the <a href="https://github.com/lionheart/python-harvest">Python Harvest API</a> by the folks over at Lionheart.

<h2>Add a Timesheet Entry</h2>
There are two ways to add an entry to Harvest. The first, before you make your first entry and are able to save an alias, is:
```
sow add
```

Simple as that, the application will guide you through the few steps required to make your timesheet entry. At the end of this process, it will prompt you to save an alias (more on that later).

<h2>Show your Timesheet Entries</h2>
To display an entry for today, type:
```
sow show today
```
For yesterday's entries:
```
sow show yesterday
```
For all of this week's entries:
```
sow show week
```
And finally, to see the entries on a specific date:
```
sow show --date <date>
```
(Dates should be entered in MM/DD/YYYY format.)

<h3>Aliases</h3>
When you make an entry, you are prompted to save an alias for easily adding future entries. The alias name becomes part of your command line arguments. This saves the Client and Task ID values to a configfile, which the application reads later.
```
sow add <alias> <hours> <note>
```
For example:
```
sow add myclient 8 'i worked for myclient today!'
```

<h1>In Development:</h1>
1. Deleting Entries
2. Submitting Timesheets for Verification (Reliant on Harvest's API)
3. Using Timers for entries.
4. Administration tasks (managing clients, projects, etc)

<h1>Questions? Concerns? Want to Contribute?</h1>
Feel free to open an issue for any questions, concerns, ideas, or suggestions. Contribution is as easy as opening a pull request. Make sure you explain your changes and provide documentation in your code.
