import config

config = ConfigParser.RawConfigParser()
config.read('~/.harvconfig')

def add(timesheet, alias, hours=False, note=False):
    today = timesheet.today
    if alias:
        client_id = config.get(alias, 'Client')
        task_id = config.get(alias, 'Task')
    if not alias:
        if not hours:
            try:
                hours = int(raw_input("How many hours for this entry? "))
            except:
                hours = int(raw_input( "Didn't get that - input the number of hours: ")
        if not note:
            note = raw_input("Leave a note? (optional) ")
        for key, value in enumerate(today['projects']):
            print key + 1, value['name']

        try:
            client = today['projects'][int(raw_input("Select a project: "))-1]
        except:
            client = today['projects'][int(raw_input("Didn't get that - select the number next to the project name: "))-1]

        client_id = client['id']
        for key, task in enumerate(client['tasks']):
            print key + 1, task['name']

        try:
            task = client['tasks'][int(raw_input("Select a task: "))-1]
        except:
            task = client['tasks'][int(raw_input("Didn't get that - select the number next to the project name: "))-1]

        task_id = task['id']

        #set_alias()

    data = {"notes": note, "project_id":client_id, "hours":hours, "task_id":task_id}
    timesheet.add(data)
    print "Added your entry."


