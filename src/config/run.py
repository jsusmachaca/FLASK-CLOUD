
def run(app, argv, Path, path):
    if len(argv) < 2:
        print('\033[31mError, no se dieron los parametros esperados\033[0m')
    else:
        if argv[1] == '-d' and len(argv) == 2:
            Path.dir_path = path.expanduser('~')
            print(f'\033[34mEl sirvidor de archivos se creó en => {Path.dir_path}\033[0m\n')
            app.run(host='0.0.0.0')
        
        elif argv[1] == '-f' and len(argv) == 3:
            Path.dir_path = argv[2]
            print(f'\033[34mEl sirvidor de archivos se creó en => {Path.dir_path}\033[0m\n')
            app.run('0.0.0.0')

        elif argv[1] == '--help':
            print('\033[33mUsa\033[0m \n\tapp [OPTION]')
            print('\033[33mOPCIONES:\033[0m')
            print("\t\033[32m-d\033[0m\n\t\tModo por defecto usa la carpeta home de su sitema\n\t\tpara crear el servidor de archivos.")
            print("\t\033[32m-f\033[0m\n\t\tUsa el directorio indicado para crear el servidor de archivos.\n\t\tpara crear el servidor de archivos.\n\n")
        else:
            print('\033[31mError, no se dieron los parametros esperados\033[0m')

