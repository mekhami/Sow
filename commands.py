import ConfigParser
from utils import get_int
import os


config = ConfigParser.RawConfigParser()
config.read(os.path.expanduser('~/.harvconfig'))


STATUS_TASK_FORMAT = '''{indicator}   Project:    {entry.project_name}
    Task:       {entry.task_name}
    ID:         {entry.id}
    Notes:      {entry.notes}
    Time:       {hours}:{minutes:02d}
    '''

def add(timesheet, alias, hours=False, note=False):
    today = timesheet.today
    if alias:
        client_id = config.get(alias, 'client')
        task_id = config.get(alias, 'task')
    if not alias:
        if not hours:
            hours = get_int("How many hours to enter? ")
        if not note:
            note = raw_input("Leave a note? (optional) ")
        for key, value in enumerate(today['projects']):
            print key + 1, value['name']

        client_selection = int(get_int("Select a project: "))
        client = today['projects'][client_selection-1]
        client_id = client['id']

        for key, task in enumerate(client['tasks']):
            print key + 1, task['name']

        task_selection = int(get_int("Select a task: "))
        task = client['tasks'][task_selection-1]
        task_id = task['id']

        set_alias(client['name'], client_id, task_id)

    data = {"notes": note, "project_id":client_id, "hours":hours, "task_id":task_id}
    timesheet.add(data)
    print "Added your entry."

def set_alias(client, client_id, task_id):
    print '''Would you like to store this client and project as an alias?
    Storing as an alias lets you easily add entries to this project with:
    harvest add <alias> <hours> <note>
    '''
    if raw_input("Save an alias? ").lower() in 'yes':
        alias = raw_input("Alias word: ")
        config.add_section(alias)
        config.set(alias, 'client', client_id)
        config.set(alias, 'task', task_id)
        with open (os.path.expanduser('~/.harvconfig'), 'wb') as configfile:
                config.write(configfile)

