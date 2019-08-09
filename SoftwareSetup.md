# Setting up your computer
The following are step-by-step instructions how to set up your computer for the work we do.

## Python
We love Python and use it for almost everything. We recommend the [Miniconda](https://docs.conda.io/en/latest/miniconda.html) distribution and Python 3.6, because certain packages have issues under 3.7.

### Installing Miniconda

1. Download and run the installer for your platform from https://docs.conda.io/en/latest/miniconda.html
2. On Windows, chose to install for `Just Me`
3. Leave the destination folger as is (unless you already have Miniconda installed).
4. Chose *neither* to 'Add Anaconda to my PATH' nor to 'Register Anaconda as my default Python 3.7'

### Setting up a Python 3.6 environment

Miniconda3 comes with Python 3.7.
To get 3.6, you need to create a new conda environment. 
Environments are basically parallel Python installations that you can switch between.
We created a preconfigured environment for you so all you have to do is:

1. Download our pre-configured [environment file](https://anaconda.org/ggeorges/py36-gg/2019.06.20.145805/download/py36-gg.yaml) and leave it in the download folder.
2. Start a miniconda prompt (see above)
3. Make sure your `conda` package manager is up to date:
```cmd
conda update conda
```
4. Change directory to your download-folder. On my Windows machine, that would be:
```cmd
cd Downloads
```
5. Install our environment from the file you downloaded:
```cmd
conda env create -f py36-gg.yaml
```
6. When everything is done (which may take a few minutes), type `exit` to close the prompt.

## Working with your Miniconda environment

### Opening an Anaconda Prompt:
- On Windows:
    - Open the start menu and type `py36` and select the `Anaconda Prompt (py36-gg)` 'App'
    - Open the start menu, type run, select the `Run` 'Desktop App' and execute the following command:
```cmd
cmd /K %LocalAppData%\Continuum\miniconda3\condabin\activate.bat py36-gg
```
- On MacOS / Linux:
    - Open a `Terminal` and run the `activate` script like so:
```bash
source $HOME/miniconda/bin/activate py36-gg
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
### Resetting a broken environment
Sometimes, when you install a new package, things that worked fine before break.
This happens if the package manager (`conda`) updates other packages while installing the new one.
Sometimes, it misses that a third package depended on one of the updated packages and is now incompatible with it.
Unfortunately, there is not much you can do except remove your environment (see command below) and set it up anew. If you install new packages immediately afterwards, there is a better chance (but no guarantee) of success. The fresh set up brings all packages to their latest version. The risk of failure increases with the age of your installation and each time you install a `conda-forge` package.

1. Run the following command in an Anaconda Prompt:
```cmd
conda env remove -n py36-gg
```
2. Repeat steps to set up your Python 3.6 environment 

## Jupyter notebooks
Jupyter notebooks are great. Use them for everything (unless instructed otherwise) and benefit of their [many features](https://www.youtube.com/watch?v=ctOM-Gza04Y), including documentation.

### Start a Jupyter notebook server
 - On Windows: type `py36-gg` and select the `Jupyter Notebook (py36-gg)` 'App'
 
### The way cool kids to it: `JupyterLab`
`JupyterLab` is an alternative look for `Jupyter`, which feels more like a desktop app.
You can run it as a Chrome App and avoid confusion with browser tabs and waht window to open.
Here is a script to do that conveniently - obviously, you'll need Google Chrome installed.

On Windows, put the following on your Desktop (or wherever you like) in a file named `JupyterLab.bat` (or anything you like, as long as there is a `.bat` extension)
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

If it complains about not finding some paths, you may have to adjust: 
* `ANACONDA`: to account for an installation directory other than the default proposed by the installer
* `WORKDIR`: you workdirectory (generally `C:\Users\[username]` on Windows)
* `ENV`: the conda environment to use (needs jupyter-lab or notebook installed - you can chose a different environment in jupyter later)
* `CHROME`:  the path to your Google Chrome installation

## Other toosl

### Gurobi
If you are working with linear optimization, you will need to install Gurobi.
Gurobi is a heavy-duty linear program solver.
You can get a free academic license with your ETH e-mail address.
Simply follow the instructions on the [Gurobi homepage](http://www.gurobi.com/registration/download-reg) and then install the 

### Code editor
For more serious coding needs you need a good Python editor.
We recommend [Microsoft Visual Code](https://code.visualstudio.com/download), [configured for Python](https://code.visualstudio.com/docs/languages/python) using the official [Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) with [IntelliSense](https://go.microsoft.com/fwlink/?linkid=2006060) enabled.

### Git
Git is a version management tool to trace changes to your document.
[Git for Windows](https://git-scm.com/download/win) gives you a full git client and in fact throws in a very usable Bash for Windows.

### ConEmu
If you need to work in the console on Windows (using GitBash), you may prefer the look and robustness of
[ConEmu](https://conemu.github.io/).

### QGIS
If you work a lot with GIS data, consider [installing QGIS](https://qgis.org/en/site/forusers/download.html).
It is a desktop GIS app and makes exploring GIS data easier than in `Jupyter`.
