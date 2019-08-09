# Setting up your computer
The following are step-by-step instructions how to set up your computer for the work we do.

## Python
We love Python and use it for almost everything. We recommend the [Miniconda](https://docs.conda.io/en/latest/miniconda.html) distribution and Python 3.6, because certain packages have issues under 3.7.

### Installing Miniconda

1. Download and run the installer for your platform from https://docs.conda.io/en/latest/miniconda.html
2. On Windows, choose to install for `Just Me`
3. Leave the destination folder as is (unless you already have Miniconda installed).
4. Chose *neither* to 'Add Anaconda to my PATH' nor to 'Register Anaconda as my default Python 3.7'

**Beware**: under no circumstances should you work within the Miniconda installation folder, meaning keep and execute your Python files anywhere else (and have at least two independent [backups]()) . It causes weird problems and - danger of data-loss - the Miniconda uninstaller deletes any file in the Miniconda folder, regardless if it came with Miniconda or not. 

### Setting up a Python 3.6 environment

Miniconda3 comes with Python 3.7.
To get 3.6, you need to create a new conda environment. 
Environments are basically parallel Python installations that you can switch between.
We created a preconfigured environment for you so all you have to do is:

1. Download our pre-configured [environment file](https://anaconda.org/ggeorges/py36-gg/2019.06.20.145805/download/py36-gg.yaml) and leave it in the download folder.
2. Start an [Anaconda Prompt](https://github.com/LAV-ESG/getting-started/blob/master/SoftwareSetup.md#opening-an-anaconda-prompt).
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

1. Open an [Anaconda Prompt](https://github.com/LAV-ESG/getting-started/blob/master/SoftwareSetup.md#opening-an-anaconda-prompt)
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

1. Run the following command in an [Anaconda Prompt](https://github.com/LAV-ESG/getting-started/blob/master/SoftwareSetup.md#opening-an-anaconda-prompt):
```cmd
conda env remove -n py36-gg
```
2. Repeat steps to [set up Python 3.6 environment](https://github.com/LAV-ESG/getting-started/blob/master/SoftwareSetup.md#setting-up-a-python-36-environment)

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

#### Things you should know:
 * If you prefer plain `Jupyter Notebook`, just replace the call in the last line of the script from `juypter-lab` to `jupyter-notebook`.
 * The only issue we found with `JupyterLab` so far is that the `Interrupt` command does sometimes not work, in particular with our  [LAV-ESG ipython-pg extension](https://github.com/LAV-ESG/ipython_psql_extension).
 * If the script complains about not finding some paths, you may have to adjust: 
    * `ANACONDA`: to account for an installation directory other than the default proposed by the installer
    * `WORKDIR`: you workdirectory (`C:\Users\[username]` on Windows, `/home/[username]` on Unix)
    * `ENV`: the conda environment to use (needs jupyter-lab installed)
    * `CHROME`:  the path to your Google Chrome executable

## Other things you might need

### Polybox
We recommend mirroring your files to [polybox](https://polybox.ethz.ch):

*Note to LAV employees: use the fileserver (never local storage, there is no back up).*

1. Log in to [polybox](https://polybox.ethz.ch), click your name in the top right and click `Settings`
2. Download the client for your platform and set it up.
3. Chose a folder within the polybox-folder as your working directory (where you keep and execute all your code)

**Why you should do it**:
  - sleep better knowing your work is safely backed up in ETH's datacenter
  - be more flexible having access to your files anywhere and any time
  - easily share your work with your supervisor
  
 **Things to consider**:
   - as per ETH regulations, you should not use non-ETH servers to store or transfer data (meaning use nothing else than [polybox](https://polybox.ethz.ch))
   - even if [polybox](https://polybox.ethz.ch) gives you a semi-automatic backup, it is wise to be paranoid and regularily copy your material e.g. to an external drive at home
   - if you work with data subject to a restrictive license, do not store it anywhere, includig polybox.
   
### Working with the LAV-ESG database server
If you need access to the server, follow [these instructions](https://github.com/LAV-ESG/getting-started/blob/master/LAV-ESG_gettingStarted.pdf). Note: you no longer need to install the `ipython_pg` module as it comes with the environment you installed above.

### Gurobi
Gurobi is a commercial software. 
You can get a free academic licence with your ETH e-mail address.

1. Head over to the [Gurobi homepage](http://www.gurobi.com/registration/download-reg) and fill out the registration form.
2. Contrary to what is suggested, do not download Gurobi. Go further down and click `Your Gurobi Licenses`
3. Click on what should be only one license number displayd in the table.
4. Scroll down to 'Installation' (below the table)
5. Copy the line `grbgetkey xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` (where `x` are some numbers and letters)
6. Open an [Anaconda Prompt](https://github.com/LAV-ESG/getting-started/blob/master/SoftwareSetup.md#opening-an-anaconda-prompt)
7. Paste the line you copied into the prompt (on Windows, right-click the black background of the window) and execute.

### Code editor
For more serious coding needs you need a good Python editor.
We recommend [Microsoft Visual Code](https://code.visualstudio.com/download), [configured for Python](https://code.visualstudio.com/docs/languages/python) using the official [Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) with [IntelliSense](https://go.microsoft.com/fwlink/?linkid=2006060) enabled.

### Git
Git comes preinstalled on Unix. For Windows, use [Git for Windows](https://git-scm.com/download/win). It also gives you a very usable Bash command line for Windows.

### ConEmu
If you need to work in the console on Windows (e.g. using GitBash), get [ConEmu](https://conemu.github.io/). It looks better, is more robust and offers tons of handy features (such as killing the active processes using `Ctrl+Break`).

### QGIS
If you work a lot with GIS data, consider [installing QGIS](https://qgis.org/en/site/forusers/download.html).
Panning and scrolling makes exlporing large datasets easier.
