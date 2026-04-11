#!/bin/bash
instalacion_software() {
    sudo apt update && sudo apt upgrade
    sudo apt install python3 mysql psql python3-pip python3-venv
    sudo apt-get update
    sudo apt-get install libjpeg-dev zlib1g-dev # para la creacion de pdfs en python
}
buscar_proyecto_y_instalar() {
    repositorio_remoto=$1
    nombre_directorio_local=$2
    directorio=$(find $HOME -name Tp2-Ids -type d | head -n 1)
    if [[ -d $directorio ]]; then
        read -p "Ya existe el directorio $directorio quiere eliminaro y/n:" eliminar
        if [[ $eliminar == "y" || $eliminar == "yes" ]]; then
            rm -rf $directorio
            echo "Se elimino el directorio $directorio"
        else
            echo "Si no lo elimina o lo mueve el directorio: $directorio no podemos continuar, Gracias por tu tiempo"
            exit 0
        fi
    fi
    if [[ -d "$HOME/.ssh" ]]; then
        echo "Clonando repositorio ..."
        git clone $repositorio_remoto $nombre_directorio_local
        echo "Directorio clonado con exito2"
    else 
        echo "no tienes configurada clave ssh publica puedes venir y leer aqui este script es seguro tus datos no se comparten!"
        read -p "Quiere crear su clave ssh esto es privado: y/n" crear_clave_ssh
        if [[ $crear_clave_ssh == "y" || $crear_clave_ssh == "yes" ]];then
            echo "vamos ha crear tu clave ssh con un solo comando"
            read -p "Por favor indicame tu correo" email
            read -p "Vamos ha generar tu clave ssh con el algoritmo ed25519 es el mas seguro hasta el momento y/n:" algoritmo
            if [[ $algoritmo == "y" || $algoritmo == "yes" ]];then
                echo "Generando clave ssh ..."
                echo "Si queres podes darle a todo enter y mas adelante con otra clave ssh intentas"
                ssh-keygen  -t ed25519 -C $email
                echo "Ahora copia tu clave ssh publica en un repositorio publico"
                echo "github -> settings -> SSH and GPG keys -> new key ssh"
                echo "Copia (ctrl +shift + C) y Pega(ctrl +shift + V) esto:"
                cat "$HOME/.ssh/id_ed25519.pub"
                read "Presione enter para continuar ..."
            else
                echo "No podemos continuar, lo siento"
                exit 0
            fi
        else
            echo "No podemos continuar lo siento"
            exit 0
        fi
    fi
    code 
}
activar_virtual_enviroment_descarguar_dependencys() {
    directorio=$1
    cd $directorio
    python3 -m venv .venv 
    source .venv/bin/activate
    pip install -r requirements.txt
    flask run
    firefox localhost:8000 || chrome localhost:8000 || edge localhost:8000 || brave localhost:8000
}
main() {
    dir_remoto="git@github.com:elimenit/Tp2-Ids.git"
    nombre_local="Tp2-Ids"
    instalacion_software
    buscar_proyecto_y_instalar $dir_remoto $nombre_local
    activar_virtual_enviroment_descarguar_dependencys "$HOME/Tp2-Ids"
    echo "Termino el proyecto exitosamente"
}
main