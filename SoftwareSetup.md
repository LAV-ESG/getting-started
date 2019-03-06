# Setting up your computer

In the following, we guide you through setting up your computer for the kind of work we do.
Primarily, this involves setting up Python, specialized tools such as the Gurobi linear programming solver (which we access through Python) and certain support tools such as a Python editor, or GIS visualization software. You may not need all of those tools for your particular project.

## Python
The reason we love Python is not the language itself - although, if you know [how to use it properly](https://inventwithpython.com/blog/2018/08/17/the-zen-of-python-explained/), it can be beautifully elegant and expressive.
It is the many great software packages that come with it, in particular those for data-science and engineering applications.
So your Python installation is not a Python interpreter (a program to run Python code), it is also a collection of useful packages, including tools to add and remove packages.
This is called a distribution.

We recommend [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
Miniconda is a minimal version of another distribution, called Anaconda. 
Aimed at scientific users, it comes with many specialized pacakges that can otherwise be tricky to install.
Miniconda does away with many things you actually do not need; however that makes it slightly more tedious to install.

We recommend using Python 3.6, because certain packages have issues under newer versions of Python.
However, there is no Miniconda for Python 3.6. So you'll have to create what is called an `environment` (see below).
As explained below, you should work with environments anyhow.

### Installing Miniconda

1. Download the installer for your platform from https://docs.conda.io/en/latest/miniconda.html
2. Execute the installer, using the 'Just For Myself' option and chosing NOT to register this as your "default Python" and NOT to add "to the path" (see note blow).
3. Right-click on your Desktop, go to `New`, `Shortcut` and under `Type the location of the item` copy or type: 
```cmd
cmd /K %LOCALAPPDATA%\Continuum\miniconda3\Scripts\activate.bat
```
4. Double-click the shortcut. In the console that just opened, update the package manager `conda` by typing:
```cmd
conda update conda
```
5. The console will open in a Windows system directory. You can (and should) adjust that to something useful by adjusting the `Start in` path in the shortcut's properties (right-click on shortcut).

*Note*: Selecting either option in step 2 makes it easier to execute Python scripts. For instance, you can just double click Python files to execute them. While that certainly comes in handy, it can mess up existing Python installations (for instance that of your GIS or the one that came with your OS). So only do this if you know what you are doing.

*Note*: adjust the path in step 3 if you did not install Miniconda in the default directory proposed by the installer. 


### Creating a new conda environment
Environments are basically parallel installations of Python living in the same directory.
You can switch between them with one simple command (see below) - only one is active at any given time.
This allows you to e.g. work with several versions of Python and/or packages on the same computer.
We recommend using Python 3.6, because certain packages have issues under newer versions of Python.

There is a more practical reason to use environments: packages depend on packages.
So when you install a new package, it may require a newer version of a package that is already installed.
`conda` is smart enough to figure this out and it will update that existing package for you.
However, other existing packages may have depended on the just update package as well.
This `conda` does not always detect; and that can break your entire installation - this is also referred to as dependency hell.
Obviously the risk of this happening grows the older (or the more out-of-date) your environment becomes.
Therefore it is good practice to simply create a new environment for new projects, instead of trying to patch some existing installation.

1. Create a new conda environment, using Python 3.6 and installing the `anaconda` packages:
```cmd
conda env create -n py36 python=3.6 anaconda
```
2. Activate the new environment `py36` by running:
```cmd
conda activate py36
```
3. To have your console-shortcut open with the new environment activated, append `py36` to the shortcut's target field, so that it reads:
```cmd
cmd /K %LOCALAPPDATA%\Continuum\miniconda3\Scripts\activate.bat py36
```

### Installing additional Python packages
The `anaconda` packages we installed when creating the `py36` environment gives you most, but not all packages you will need.
Installing new packages is easy: in the Python console (see above), type:
```cmd
conda install [packagename]
```
Often this will produce a `PackagesNotFoundError`. That may mean you misspelt the name. 
If not, in virtually all cases, the solution is to use the so called `conda-forge` channel, which is basically an alternative package repository:
```cmd
conda install - c conda-forge [packagename]
```
Beware that using conda-forge packages increases the risk of entering 'dependency hell', explained before.

Here is a collection of additional packages you may want to install:

* Database access:
  * `psycopg2`: access to the LAV database server
  * `ipython_pg`: LAV postgres database access module (for now, see https://github.com/LAV-ESG/ipython_psql_extension#installation)
* Data formats:
  * `feather-format`: enables `pandas` to read Apache Feather.
* GIS:
  * `shapely`: working with GIS geometry objects
  * `geopandas`: managing collections of GIS geometry objects
  * `cartopy`: plotting GIS objects
* optimization
  * `gurobi`: linear program solver
* Jupyter Lab:
  * `jupyerlab`: alternative web-interface for Jupyter notebooks
* machine learning:
  * `tensorflow`: neueral network library
  

### Setting up Jupyter notebooks
Jupyter notebooks are a phantastic way to do scientific computing in Python.
They put your code alongside with its results (in particular plots) and documentation.
It is probably the best environment for you to work in, unless you have some very intense development tasks to accomplish.

Jupyter is actually a web-server that runs on your computer and that you view using your browser.
To get a more 'desktop-app' feel, use `JupyterLab` as a Chrome app.
A convenient way of running it is the following batch-script. 
Copy this into a text-file and rename it to 'JupyterLab.bat', or something similar (the `.bat`-bit is important). Then just double-click to launch.
You can adjust: 
* `ANACONDA`: to account for an installation directory other than the default proposed by the installer
* `WORKDIR`: you workdirectory ((generally `C:\Users\[username]` on Windows)
* `ENV`: the conda environment to use (needs jupyter-lab or notebook installed - you can chose a different environment in jupyter later)
* `CHROME`:  the path to your Google Chrome installation

```cmd
@echo off
set ANACONDA=%LOCALAPPDATA%\Continuum\miniconda3
set WORKDIR=%USERPROFILE%
set ENV=py36
set CHROME=%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe

cd /d %WORKDIR%
call %ANACONDA%\Scripts\activate %ENV%
%ANACONDA%\Scripts\jupyter-lab.exe --browser="\"%CHROME%\" --app=%%s"
```

## Installing other tools

### Gurobi
If you are working with linear optimization, you will need to install Gurobi.
Gurobi is a heavy-duty linear program solver.
In principle, it is a commercial product, but you can get a free academic license with your ETH e-mail address.
Simply follow the instructions on the [Gurobi homepage](http://www.gurobi.com/registration/download-reg) and then install the `gurobipy` package:
```cmd
conda install -c http://conda.anaconda.org/gurobi gurobi
```

### Code editor
For your more serious coding needs (talk to your supervisor to determine how serious they really are), you need a good Python editor.
We recommend [Microsoft Visual Code](https://code.visualstudio.com/download), [configured for Python](https://code.visualstudio.com/docs/languages/python) using the official [Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) with [IntelliSense](https://go.microsoft.com/fwlink/?linkid=2006060) enabled.

### Git
Git is a version and configuration management system.
It allows you to track changes made to a document over time, and to share changes among different people.
We use it to co-develop certain bits of software.
[Git for Windows](https://git-scm.com/download/win) gives you a full git client, and in fact throws in a very usable Bash for Windows.

### ConEmu
Once you start working with GitBash and becoming generally more reliant on the Windows console, you may get annoyed by the performance of `cmd.exe`.
[ConEmu](https://conemu.github.io/) gives you a solid alternative.

### QGIS
If you work with GIS data, you may consider [installing QGIS](https://qgis.org/en/site/forusers/download.html). 
While the visualizations capabilities within the Jupyter notebook are adequate, the ability to just pan and scroll a map can save a lot of time.
