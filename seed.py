import mysql.connector

cnx = mysql.connector.connect(user='root', password='Panzer_7', host='localhost')
cursor = cnx.cursor()

def executeScriptsFromFile(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
          if command.rstrip() != '':
            cursor.execute(command)
        except ValueError as msg:
            print("Command skipped: ", msg)


executeScriptsFromFile('./Database/insert_value.sql')
cnx.commit()