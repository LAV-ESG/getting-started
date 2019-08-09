# Setting up your computer
The following are step-by-step instructions how to set up your computer for the work we do.

## Python
We love Python and use it for almost everything. We recommend the [Miniconda](https://docs.conda.io/en/latest/miniconda.html) distribution and Python 3.6, because certain packages have issues under 3.7.

### Installing Miniconda

1. Download and run the installer for your platform from https://docs.conda.io/en/latest/miniconda.html
2. Chose to install for `Just Me`
3. Leave the destination folger as is (unless you already have Miniconda installed).
4. Chose *neither* advanced option (neither 'Add Anaconda to my PATH', nor 'Register Anaconda as my default Python 3.7')
5. Wait for install to complete and uncheck both checkboxes that want to give you more information.

### Setting up a Python 3.6 environment

Miniconda3 is only available with Python 3.7. To get version 3.6, we need to create a new conda environment. Conda environments are a confusing thing that allow you to basically have parallel Python installations and switch between them. We created a preconfigured environment for you so all you have to do is:

1. Download our pre-configured [environment file](https://anaconda.org/ggeorges/py36-gg/2019.06.20.145805/download/py36-gg.yaml) and leave in your download folder.
2. Start a miniconda prompt (see above)
3. Make sure your base installation is up to date by updating it:
```cmd
conda update --all
```
4. Change directory to your download-folder. On my Windows machine, that would be:
```cmd
cd Downloads
```
5. Install our pre-configured environment using:
```cmd
conda env create -f py36-gg.yaml
```
6. When everything is done (which may take a few minutes), type `exit` to close the prompt.

## Working with your Miniconda environment

### Opening an Anaconda Prompt:
- On Windows:
    - Open the start menu and type `py36` and select the `Anaconda Prompt (py36-gg)` 'App'
    - If that does not work, right-click your Desktop (or some other convenient location in Explorer), click `New` and then `Shortcut`. As Target type:
```cmd
cmd /K %LocalAppData%\Continuum\miniconda3\condabin\activate.bat py36-gg
```
### Installing new packages

1. Open an Anaconda Prompt (see above)
2. Then run the following command, where `packagename` is the name of the package you need:
```cmd
conda install packagename
```
3. For more specialized packages, you might have to turn to `conda-forge`:
```cmd
conda install -c conda-forge packagename
```
### When things go wrong
Sometimes, when you install a new package, things that worked fine before suddenly break.
This can happen if the package manager updates other packages while installing the new one.
Sometimes, the package manager simply does not detect that a third package depended on one of those updated packages and should have been updated as well.
Unfortunately, there is not much you can do except remove your environment (see command below) and set it up anew. If you install the missing new package immediately afterwards, there is a decent chance of success, as the fresh set up brings all packages to their latest version. The risk of failure increases with the age of your installation and each time you install a `conda-forge` package.
```cmd
conda env remove -n py36-gg
```

## Jupyter notebooks
We love Jupyter notebooks and stronlgy urge you to use them as your primary work environment. They allow you to put your code alongside its results and easily document it in prose.

### Start a Jupyter notebook server
 - On Windows: type `py36-gg` and select the `Jupyter Notebook (py36-gg)` 'App'
 
### The way cool kids to it: `JupyterLab`
`JupyterLab` is an alternative frontend to `Jupyter` which gives you more the feel of a desktop-app.
Here is a nifty little trick to run it as a Chrome App - obviously, you'll need Google Chrome installed.

On Windows, put the following on your Desktop (or wherever you like) in a file named `JupyterLab.bat` (or anything you like, as long as there is a `.bat` extension)
You can adjust: 
* `ANACONDA`: to account for an installation directory other than the default proposed by the installer
* `WORKDIR`: you workdirectory (generally `C:\Users\[username]` on Windows)
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
You can get a free academic license with your ETH e-mail address.
Simply follow the instructions on the [Gurobi homepage](http://www.gurobi.com/registration/download-reg) and then install the 

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
