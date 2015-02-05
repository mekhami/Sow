import ConfigParser
from utils import get_int
config = ConfigParser.RawConfigParser()
config.read('~/.harvconfig')

def add(timesheet, alias, hours=False, note=False):
    today = timesheet.today
    if alias:
        client_id = config.get(alias, 'Client')
        task_id = config.get(alias, 'Task')
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

        #set_alias()

    data = {"notes": note, "project_id":client_id, "hours":hours, "task_id":task_id}
    timesheet.add(data)
    print "Added your entry."


