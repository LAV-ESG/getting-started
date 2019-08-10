# Getting-started
Here are some steps you should take to get your computer ready for your project.

## Set up your computer to work on your project
We put up [detailed instructions](https://github.com/LAV-ESG/getting-started/blob/master/SoftwareSetup.md) helping you to make getting started as easy as possible. When you are done, the following gives you some pointers how to start using Python:
## Learning to work with Python

### Python for scientific computing
Python is known for being [easy learn](https://www.quora.com/Is-Python-an-easy-language-to-learn), but slow compared to C or Fortran.
It owes its popularity in scientific computing due to the many great libraries, themselves often written in fast C and Fortran.
This gives you heavy-duty computing with the easy-of-use of Python.

The downside is, you need to 'learn' those libraries.
For example, this is slow:
```python
N = 100000
a = np.random.rand(N)  # creates a very long array of random numbers
result = 0
for i in range(N):  # iterate from 0 to the length o
    results = result + a[i]
 ```
 This does the same but much faster (because in C, in the background):
 ```python
 N = 100000
 a = np.random.rand(N)
 result = a.sum()
 ```
 As a guideline to get you started, if you find yourself using `for`-loops like the one above (with an increasing integer variable `i` that you use to access the array), you are doing something wrong.
 Check the documentation: there probably is a function that can do what you need much faster (and without you having to implement it).
 
The libraries you should know are:

1. **Pandas** to analyze tabular datasets, which most of them are (see [10 Minutes to pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html))
2. **seaborn**, a tool that greatly simplies plotting tabular data
3. **NumPy** for vector-based math, similar to Matlab (have a look at the [quickstart tutorial](https://docs.scipy.org/doc/numpy/user/quickstart.html)
4. the [scipy library](https://docs.scipy.org/doc/scipy/reference/) provides various tools for  tasks such as numeric optimization, root-finding or interpolation

## Where and how to write and run code
Your code does not just have to be understood by the machine, but also other humans.
Most importantly, this includes youself in a few months.
Here some hints to better use the available tools:

### Jupyter Notebooks
Use Jupyter notebooks for all data-analysis (anything that entails plotting and viewing data a lot).
Notebooks allow you to mix code, documentation (with LaTeX equations) and plotting and are the perfect way of documenting your progress.
To document, put the cell mode to `Markdown`. 
Alternatively, when in a cell, hit `Escape` to enter [command mode](https://medium.com/ibm-data-science-experience/back-to-basics-jupyter-notebooks-dfcdc19c54bc), and then hit `M`.
Two other handy command-mode shortcuts are `A` and `B` to add a cell above resp. below the current cell.

Get used to documenting your thoughts when performing an analysis: why do you do something, what do you see?
And most importantly, write down your sources. Wher did you get the data from? 
You can easily put hyperlinks in markdown, e.g. to remember an interesting paper:
```Markdown
Results are based on the paper of [Küng et al.](https://doi.org/10.1016/j.trc.2018.09.003)
```

Have a look at [this blog-post](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/) for a full feature review.

### Scripting vs. programming
If you have notebook-cells with code in excess of 10-20 lines, then you are probably not just doing data-analysis anymore - you are creating a piece of software.
Jupyter notebooks are not the best choice for that, for various reasons.
You should be using a ".py"-File instead and run it as a program.

## A note on how to write code
Good code is code that people other than you (or future you) understand, without having to go through it line by line to figure out what happens.
Don't write code for machines, write code for humans.

Python actually has some conventions for this.
A good introduction is the [style-guide of the Hitchhiker's guide to Python](http://python-guide-pt-br.readthedocs.io/en/latest/writing/style/).

To make your life a little easier, here a few tricks:

### Avoid more than 2 levels of indentation
Indentation is whenever you have empty space at the beginning of a line.
More than 2 or three levels is ugly - here we have 6:
```Python
for a in A:
    if a > 3:
        for b in B:
            if b > 4:
                for c in  C:
                    if c > 7:
                         do_something(a, b, c)
```
Now we bring that down to four:
```Python
for a in A:
    for b in B:
        for c in C:
            if a <= 3 or b <= 4 or c <= 7:
                continue
            do_something(a, b, c)
 ```
A much better way would be to use [itertools.product](https://docs.python.org/3.6/library/itertools.html#itertools.product):
 ```Python
 import itertools
 for a, b, c in itertools.product(A, B, C):
     if a <= 3 or b <= 4 or c <= 7:
         continue
     do_something(a, b, c)
```

### Avoid hard-coding things:
You can use default arguments in a function to turn this:
```Python
def F_aero(v):
    return 0.5 * 1.2 * 0.3 * 2 * v**2
    
F_aero(13)
```
into the equivalent but much more flexible:
```Python
def F_aero2(v, rho=1.2, c_D=0.3, A_f=2.0):
    return 0.5 * rho * c_D * A_f * v**2
    
F_aero2(13) == F_aero(13)
F_aero2(13, c_D=0.4) > F_aero(13)
```

An other example of extreme hard-coding is:
```Python
age_bracket0 = 0
age_bracket1 = 0
age_bracket2 = 0
age_bracket3 = 0
age_bracket4 = 0
age_bracket5 = 0
for age in age_of_people_in_population:
    if age > 0 and age <= 10:
        age_pracket0 += 1
    elif age > 10 and age <= 20:
        age_pracket1 += 1
    elif age > 20 and age <= 30:
        age_pracket2 += 1
    elif age > 40 and age <= 50:
        age_pracket3 += 1
    elif age > 50 and age <= 60:
        age_bracket4 += 1
    elif age > 60
        age_bracket5 += 1
age_count = {0: age_bracket0, 10: age_bracket1, 20: age_bracket2, ...}
```
Compare this to, and think about what happens if you ever decide to have 5-year age brackets:
```Python
age_count = {a: 0 for a in range(0, 51, 10)}
for age in age_of_people_in_population:
    for lower in age_count.keys():
        if age <= lower:
            continue
        age_count[lower] += 1
```
And finally the smart way of doing this:
```Python
np.digitize(age_of_people_in_population, np.arange(0, 61, 10))
```
