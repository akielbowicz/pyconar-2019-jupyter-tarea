# Resolviendo la tarea con Jupyter



Para que ya tengan su ambiente de trabajo preparado, dejo aquí los requerimientos mínimos.


## Requerimientos

El requerimiento para realizar este taller es tener un ambiente con python3 y las siguientes librerías:

 - JupyterLab o Jupyter Notebook
 - sympy
 - bqplot
 - ipycanvas
 - ipyleaflet

### Instalación

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

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/akielbowicz/pyconar-2019-jupyter-tarea.git)

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/akielbowicz/pyconar-2019-jupyter-tarea/blob/master/notebooks/Indice.ipynb)