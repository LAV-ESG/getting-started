# Getting-started
Here are some steps you should take to get your computer ready for your project:

## Install Python
We try to do everything in [Python](http://python.org). So the first thing you should get is a Python installation.
We recommend [Anaconda](https://www.continuum.io/anaconda-overview), as comes with everything you need to get started - except a good editor (more on that later). 
All you need to do is download and run the installer from [the download page](https://www.continuum.io/downloads).

## Access the LAV-ESG database
If you need access to data on our database server, follow the instructions in [this document](LAV-ESG_gettingStarted.pdf)

## Learn to write decent Python code
Python is known for its beautiful syntax; but that doesn't mean that it is impossible to write ugly code in Python.
What makes code beautifiul? Readability!
Readable code is code that people other than you (or you, a year after finishing your project) understand without having to go through every line to figure out what happens.
There is nothing magical about this: don't write code for machines, write code for humans.

The Python community has its own definition of what they consider good or "Pythonic" code: it is code that follows the "[The Zen of Python](https://www.python.org/dev/peps/pep-0020/)" (a.k.a. PEP20).
You should read and follow them - it will improve your progamming.

How do you implement this practically?
Well, the first thing you should do is follow the Python coding-style "[PEP8](https://www.python.org/dev/peps/pep-0008/)".
Just activate the PEP8-checking mode of your editor; it will then highlight styling errors for you - and of course you should remove them.
It may be a bit cumbersome at the beginning, but you'll quickly get the hang of it.

One of the most important rules is to add docstrings to every function and method.
Write a sentence about what the function does, what arguments it accepts and what type they should be.

Then you should study the [style-guide of the Hitchhiker's guide to Python](http://python-guide-pt-br.readthedocs.io/en/latest/writing/style/).
It lists the most important Python "idioms" that you should know and apply. Just try to remember them...

## Get to know your toolbox
Unfortunately, Python is not what you call high-performance: algorithms written in C or Fortran are typically orders of magnitude faster than their Python equivalent - assuming a skilled programmer.
Fortunately, you can call libraries, written in C and Fortran from Python.
So you can get the speed of C, with the ease-of-use of Python.
For scientific computing, speed is obviously an issue.
This is why people wrote the wondeful [SciPy stack](http://scipy.org), which provides high-performance tools for anything from vector-algebra to plotting.
You should know at least the following packages:

1. NumPy for vector-based math (have a look at the [quickstart tutorial](https://docs.scipy.org/doc/numpy/user/quickstart.html)
2. matplotlib for plotting (see the [pyplot tutorial](http://matplotlib.org/users/pyplot_tutorial.html))
3. the [scipy library](https://docs.scipy.org/doc/scipy/reference/) for common tasks such as numeric optimization, root-finding or interpolation
4. pandas for data-analysis (see [10 Minutes to pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html))

NumPy is the most important one, as it is the basis for all others.
It works in much the same as vectors and matrices in MATLAB.
Everything you can do using vector-operations in NumPy, you can also do using for-loops in Python.
However, you should prefer the vector operations whenever possible, because they are much faster than Python (since NumPy does them with optimized linear algebra C-code behind the scenes).

## Where and how to write and run code

### Jupyter Notebooks
Generally, we recommend Jupyter IPython notebooks for all data-analysis work (anything that entails plotting and viewing data a lot). 
Notebooks allow you to mix code, documentation (with LaTeX equations) and plotting into one greate way of documenting your progress.
Have a look at [this blog-post](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/) to see what it can do.
If you got Anaconda, then it is already pre-installed - see the [documentation](http://jupyter.org/install.html) for instructions on how to launch it.

*Hint for Windows users*: create a shortcut, say on the Desktop, to "jupyter-notebook.exe" - you'll find it in the "Scripts" folder of your Anaconda installation folder. By adjusting the "Start in" property of your shortcut, you can make the initial overview over your files start in any directory you like.

### Writing your own library
If you have cells with codes exceeding some 30 lines, in particular if they contain function or class definitions, then you are probably no longer pure data-analysis - you are creating a piece of software.
Jupyter notebooks are not the best choice for that, for various reasons.
Instead, you should this growing bit of code out into a ".py"-File, and consider it an external library.

For one, you now get to use real developer tools - we recommend PyCharm, for which students get free licenses, or Sublime with the "Anaconda IDE plugin" installed.
With outlining and advanced search capabilities, they make it is much easier to navigate a growing code-basis.
Also you can activate PEP8-checking, which improves your coding style.
This is important since, when writing a library, it is all about the code and people reusing it; data-analysis in the jupyter notebook on the other hand is all about the results.

Consider [unittesting](https://cgoldberg.github.io/python-unittest-tutorial/) while developping.
Also, whenever possible, try to "tool" your library by providing a command-line interface (CLI).
That way, people (and you) can use it from the console to generate data - which you can then analyze in a notebook again.
"docopt" is a fantastic little tool to generate CLIs.









