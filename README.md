# Resolviendo la tarea con Jupyter


Para que ya tengan su ambiente de trabajo preparado, dejo aquí los requerimientos mínimos.

Dado que el repositorio aún no tiene todos los contenidos (ya lo sé, es difícil no procrastinar) y para yo tener una idea de quienes van a participar en el taller. Te pido que completes con tus datos [en este formulario](https://forms.gle/FoUjapWcSmReudHHA)

## Requerimientos

El requerimiento para realizar este taller es tener un ambiente con python3 y las siguientes librerías:

 - JupyterLab o Jupyter Notebook
 - sympy
 - bqplot
 - ipycanvas
 - ipyleaflet

## Instalación

### Si no tenés ningún conocimiento previo

Lo mejor va a ser que te descargues uno de los instaladores que están en la siguiente [Carpeta con instaladores](https://drive.google.com/drive/folders/1XlqXPgZTtoP9VNmnbPFkTyqrMmZEd-47?usp=sharing). Dependiendo de tu computadora y sistema operativo vas a tener que descargarte distintos archivos.

Si usas:

linux: tenes que descargar el archivo con extensión _.sh_
windows >= 7 :  tenes que descargar el archivo *x86_64.exe*
windows xp: tenes que descargar el archivo _x86.exe_

### Si te manejás bien con Conda 

Primero antes que nada, cloná este repositorio. Lo podés hacer descargando el [zip](https://github.com/akielbowicz/pyconar-2019-jupyter-tarea/archive/master.zip) o si tenés instalado _git_ ejecutar en la consola:

```
git clone https://github.com/akielbowicz/pyconar-2019-jupyter-tarea.git
cd pyconar-2019-jupyter-tarea
```

Si no tenés python instalado, te recomiendo bajarte [miniconda](https://conda.io/miniconda.html)

Una vez instalada:

Si estás en Windows, abrí la consola de *miniconda* desde la barra de inicio.

Si estás en un ambiente Unix, abrí la una consola de tu preferencia.
 
En esa consola cambiá de directorio a donde clonaste el repositorio y ejecutá
 
```
conda env create --name jupyter-tarea --file environment.yml
```

Una vez que termine de instalar todo, tenés que activar el ambiente de *conda* ejecutando:

Alguno de estos comandos ( depende del ambiente y la consola ):

```bash
conda activate jupyter-tarea
source activate jupyter-tarea
activate jupyter-tarea
```

Una vez activado hay que abrir Jupyter ejecutando:

`jupyter lab`

Se va a abrir un navegador y ya podemos empezar a probar cosas.


> Para los usuarios de Windows seguramente hay una forma un poco más sencilla ejecutar JupyterLab
> instalando la versión completa de [Anaconda](https://conda.io/docs/user-guide/install/windows.html).


# Versiones Online

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/akielbowicz/pyconar-2019-jupyter-tarea.git/master)