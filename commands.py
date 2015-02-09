from utils import get_int, config_write
import os


STATUS_TASK_FORMAT = '''{indicator}   Project:    {client}
    Task:       {task}
    Notes:      {note}
    Time:       {hours}
    '''

def add(args, config, timesheet):
    today = timesheet.today

    if args['<alias>']:
        client_id = config.get(args['<alias>'], 'client')
        client_name = config.get(args['<alias>'], 'clientname')
        task_id = config.get(['<alias>'], 'task')
        task_name = config.get(['<alias>'], 'taskname')
        data = {"notes": args['<note>'], "project_id": client_id, "hours": args['<hours>'], "task_id": task_id}

    if not args['<alias>']:
        #Get the number of hours
        if not args['<hours>']:
            hours = get_int("How many hours to enter? ")

        #User selects a client from the list
        for key, value in enumerate(today['projects']):
            print key + 1, value['name']
        client_selection = int(get_int("Select a project: "))
        client = today['projects'][client_selection-1]
        client_name = client['name']

        #User selects a task from the client task list
        for key, task in enumerate(client['tasks']):
            print key + 1, task['name']
        task_selection = int(get_int("Select a task: "))
        task = client['tasks'][task_selection-1]
        task_name = task['name']

        #User adds a note to the entry
        if not args['<note>']:
            note = raw_input("Leave a note (Skip with enter): ")

        #Prompt the user to set an alias.
        set_alias(client['name'], client['id'], task['name'], task['id'])

        data = {"notes": note, "project_id":client['id'], "hours":hours, "task_id":task['id']}

    timesheet.add(data)
    print "Your entry has been saved."
    print str.format(
            STATUS_TASK_FORMAT,
            client = client_name,
            task = task_name,
            note = note,
            hours = hours,
            indicator = '+'
        )

def set_alias(client, client_id, task, task_id):
    print '''Would you like to store this client and project as an alias?
    Storing as an alias lets you easily add entries to this project with:
    harvest add <alias> <hours> <note>
    '''
    if raw_input("Save an alias? ").lower() in 'yes':
        alias = raw_input("Alias word: ")

        configdata = {'client': client_id, 'task': task_id, 'clientname': client, 'taskname': task}
        config_write(alias, configdata)

