from utils import get_int, config_write, get_week
from dateutil.parser import parse
from harvest import HarvestError
from datetime import *
import ConfigParser
import sys


STATUS_TASK_FORMAT = '''{indicator}   Project:    {client}
    Task:       {task}
    Notes:      {note}
    Date:       {date}
    Time:       {hours}
    '''

def add(args, config, timesheet):
    today = timesheet.today

    if args['<alias>']:
        try:
            client_id = config.get(args['<alias>'], 'client')
            client_name = config.get(args['<alias>'], 'clientname')
            task_id = config.get(args['<alias>'], 'task')
            task_name = config.get(args['<alias>'], 'taskname')
            note = args['<note>']
            hours = args['<hours>']

            data = {"notes": args['<note>'], "project_id": client_id, "hours": args['<hours>'], "task_id": task_id}
        except ConfigParser.NoSectionError:
            print "No alias named " + args['<alias>'] + " found."
            sys.exit()

    if not args['<alias>']:
        #Get the number of hours
        if not args['<hours>']:
            hours = get_int("How many hours to enter? ")

        #User selects a client from the list
        for key, value in enumerate(today['projects']):
            print key + 1, value['name']
        client_selection = get_int("Select a project: ")
        client = today['projects'][client_selection-1]
        client_name = client['name']

        #User selects a task from the client task list
        for key, task in enumerate(client['tasks']):
            print key + 1, task['name']
        task_selection = get_int("Select a task: ")
        task = client['tasks'][task_selection-1]
        task_name = task['name']

        #User adds a note to the entry
        if not args['<note>']:
            note = raw_input("Leave a note (Skip with enter): ")

        #Prompt the user to set an alias.
        set_alias(client['name'], client['id'], task['name'], task['id'])

        data = {"notes": note, "project_id":client['id'], "hours":hours, "task_id":task['id']}

    if args['--date'] or args['-d']:
        date = {'spent_at': parse(args['<date>'])}
        data.update(date)
    else:
        date = datetime.today()

    timesheet.add(data)
    print "Your entry has been saved."
    print str.format(
            STATUS_TASK_FORMAT,
            client = client_name,
            task = task_name,
            note = note,
            hours = hours,
            date = date,
            indicator = '+'
        )

def show(args, timesheet):
    today = datetime.today()
    if args['today']:
        day = datetime.timetuple(today)
        today_response = timesheet.get_day(day[7], day[0])
        data = [today_response['day_entries']]

    if args['yesterday']:
        yesterday = datetime.timetuple(today - timedelta(1))
        yesterday_response = timesheet.get_day(yesterday[7], yesterday[0])
        data = [yesterday_response['day_entries']]

    if args['week']:
        data = []
        day = datetime.timetuple(today)
        for i in range(get_week(), day[7]+1):
            daily_response = timesheet.get_day(i, day[0])
            data.append(daily_response['day_entries'])

    if args['--date']:
        date = datetime.timetuple(parse(args['<date>']))
        date_response = timesheet.get_day(date[7], date[0])
        data = [date_response['day_entries']]

    for sublist in data:
        for entry in sublist:
            print str.format(
                STATUS_TASK_FORMAT,
                task = entry['task'],
                client = entry['client'],
                note = entry['notes'],
                hours = entry['hours'],
                date = entry['spent_at'],
                indicator = '='
            )

def delete(args, timesheet):
    if args['<date>']:
        day = datetime.timetuple(parse(args['<date>']))
        date_response = timesheet.get_day(day[7], day[0])
        data = [date_response['day_entries']]

        for sublist in data:
            for k, entry in enumerate(sublist):
                print str.format(
                    STATUS_TASK_FORMAT,
                    task = entry['task'],
                    client = entry['client'],
                    note = entry['notes'],
                    hours = entry['hours'],
                    date = entry['spent_at'],
                    indicator = k+1
                )

        if args['-a'] or args['--all']:
            if raw_input("Confirm: Delete all entries for this date? ").lower() in 'yes':
                for sublist in data:
                    for entry in sublist:
                        timesheet.delete(entry['id'])
        else:
            selection = get_int('Delete which entry? ') - 1
            print str.format(
                STATUS_TASK_FORMAT,
                task = data[0][selection]['task'],
                client = data[0][selection]['client'],
                note = data[0][selection]['notes'],
                hours = data[0][selection]['hours'],
                date = data[0][selection]['spent_at'],
                indicator = '-'
            )
            if raw_input("Confirm: Delete this entry? ").lower() in 'yes':
                try:
                    timesheet.delete(data[0][selection]['id'])
                except:
                    print 'Entry deleted.'
            else:
                print 'Deletion aborted.'


def set_alias(client, client_id, task, task_id):
    print '''Would you like to store this client and project as an alias?
    Storing as an alias lets you easily add entries to this project with:
    harvest add <alias> <hours> <note>
    '''
    if raw_input("Save an alias? ").lower() in 'yes':
        alias = raw_input("Alias word: ")

        configdata = {'client': client_id, 'task': task_id, 'clientname': client, 'taskname': task}
        config_write(alias, configdata)

