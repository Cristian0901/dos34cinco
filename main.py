from colorama import Fore
from os import remove #eliminar archivos
import shutil

def comandos():
    com = input(Fore.RED + '>> ' + Fore.RESET)
    if com.startswith('move '):#Mover un archivo
        rut = com.replace('move ','')
        if rut == '':#Aviso
            print(Fore.YELLOW + 'Agregar nombre del archivo' + Fore.RESET)
        else:
            dest = input(Fore.LIGHTYELLOW_EX +'Agregue el destino para el archivo: ' + Fore.RESET)
            try:#Mover el archivo
               shutil.move(rut,dest)
               print(Fore.GREEN + 'Accion completada con exito' + Fore.RESET)
            except shutil.SameFileError:#Ruta y destino igual
                print(Fore.RED + '[ERROR]:' + Fore.RESET + 'La ruta del archivo y el destino son los mismos')
            except FileNotFoundError:#archivo no encontrado
                print(Fore.RED + '[ERROR]:' + Fore.RESET + 'No se pudo encontrar el archivo')
            except PermissionError:#Permisos invalidos
                print(Fore.RED + '[ERROR]:' + Fore.RESET + 'No tienes los permisos del sistema para ejecutar esta accion')
            except OSError:#Argumentos invalidos
                print(Fore.RED + '[ERROR]:' + Fore.RESET + 'Argumento invalido')
    
    elif com.startswith('copy '):#Copiar un archivo
        rut = com.replace('copy ','')
        if rut == '':#Aviso
            print(Fore.YELLOW + '[AVISO]:' + Fore.RESET + 'Agregar nombre del archivo')
        else:
            dest = input(Fore.LIGHTYELLOW_EX +'Agregue el destino para el archivo: ' + Fore.RESET)
            try:#copiar el aviso
               shutil.copy(rut,dest)
               print(Fore.GREEN + 'Accion completada con exito' + Fore.RESET)
            except shutil.SameFileError:#Ruta y destino igual
                print(Fore.RED + '[ERROR]:' + Fore.RESET + 'La ruta del archivo y el destino son los mismos')
            except FileNotFoundError:#archivo no encontrado
                print(Fore.RED + '[ERROR]:' + Fore.RESET + 'No se pudo encontrar el archivo')
            except PermissionError:#Permisos invalidos
                print(Fore.RED + '[ERROR]:' + Fore.RESET + 'No tienes los permisos del sistema para ejecutar esta accion')
            except OSError:#Argumentos invalidos
                print(Fore.RED + '[ERROR]:' + Fore.RESET + 'Argumento invalido')
            
    elif com.startswith('del '):#Eleminar un archivo
        rut = com.replace('del ','')
        if rut == '':#Aviso
            print(Fore.YELLOW + 'Agregar nombre del archivo' + Fore.RESET)
        else:
            try:#eliminar el archivo
                remove(rut)
                print(Fore.GREEN + 'Accion completada con exito' + Fore.RESET)
            except FileNotFoundError:#archivo no encontrado
                print(Fore.RED + '[ERROR]:' + Fore.RESET + 'No se pudo encontrar el archivo')
    
    elif com.startswith('mk '):
        rut = com.replace('mk ','')
        if rut == '':#Aviso
            print(Fore.YELLOW + 'Agregar nombre del archivo' + Fore.RESET)
        else:#crear el archivo
            file = open(rut,'w')
            file.close()
            print(Fore.GREEN + 'Accion completada con exito' + Fore.RESET)

    elif com.startswith('help'):
        print(Fore.LIGHTGREEN_EX + '##############################')
        print('#    move = Mover archivos   #')
        print('#    copy = Copiar archivos  #')
        print('#    del = Eliminar archivos #')
        print('#    mk = Crear archivos     #')
        print('##############################' + Fore.RESET)

    else:#Comando invalido
        print(Fore.RED + '[ERROR]:'  + Fore.RESET + 'No es un comando valido')

while True:#Bucle principal
    comandos()