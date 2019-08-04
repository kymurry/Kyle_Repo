import ftplib

def ftp_connect():
    while True:
        site_address = input('Enter site address:')

        try:
            with ftplib.FTP(site_address) as ftp:
                ftp.login()
                print (ftp.getwelcome())
                print ('Current Directory', ftp.pwd())
                ftp.dir()
                ftp_command(ftp)
                break
        except ftplib.all_errors as e:
            print('error', e)

def ftp_command(ftp):
    while True:
        command = input('Enter a Command')
        commands = command.split()

        if commands[0] == 'cd':
            try:
                ftp.cwd(commands[1])
                print('Directory of ', ftp.pwd())
                ftp.dir()

            except ftplib.error_perm as e:
                print('error')

        elif commands[0] == 'get':
            try: 
                ftp.retrbinary('RETR ' + commands[1], open(commands[1],'wb').write)
                print('File Succesfully downloaded')
            except ftplib.error_perm as e:
                print('error',e)


        elif commands[0] == 'ls':
            print('directory of', ftp.pwd())
            ftp.dir()
        elif commands[0] == 'exit':
            ftp.quit()
            print('goodbye')
            break
        else:
            print('invalid command')

ftp_connect()