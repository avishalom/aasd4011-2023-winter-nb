## Setup
To run the code on a local or remote machine, you can follow the suggestion below.
We use `pip` and `venv`, as these are the default Python environment management system (and they do that well, we find). 
### Prerequisite
* The code was tested using `Python` 3.10.9, and the environment was set up using `pip` and `venv` (rather than `conda`). The IDE the instructors work with is `vscode`.
* Make sure that you have a valid `Python` version installed (could be: 3.7.x-3.10.x), as well as `pip` and `git`. From the command line, run: `python --version`, `pip --version` and `git --version` to check for their versions. If either is missing, install it according to the official guides: [python](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/installation/) and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
### Steps
1. Clone this repository. From the command line, run: `git clone https://github.com/RanFeldesh/aasd4011-2023-winter-nb`. This will create a new sub-folder containing a local copy of the repository. (note: if something doesn't go well during the setup, you can delete this folder, and start fresh by cloning again. Changes during the setup are supposed to effect files only within this folder, so deleting it provides a fresh start).
2. The aim is to (a) create *two* virtual environments, one for `PyTorch` and one for `Tensorflow` (both CPU-only, without GPU support), (b) install the packages in the requirements files into each, and (c) install `ipykernel` for each. This can be done in two ways:
    - Semi-automatically - using the `setup.py` script: from the repository root folder run: `python ./setup/setup.py`. This was tested on Windows and Ubuntu (but not Mac, although it is likely to work). This should complete all required steps for you. In case it doesn't, and you can't quickly debug, simply delete the folder, go back to step 1, and try the manual version. Deleting the folder reverts any changes. By the way, you might find it useful to spend a few minutes reading `setup.py`, to see how it implements the manual steps below as a (semi) Python code. 
    - Manually - following the steps below:
        A. Within the folder of the local repository, create a subfolder named `venv`.
        B. `cd` into `venv` and craete two environment by running (note that you might need to use `python3` instead of `python`, to know which, run `which python` on Linux/Mac or `where python` on Windows. If the path include `python3`, then that's your interpreter):
            * `python -m venv pytorch_cpu`
            * `python -m venv tensorflow_cpu`
        C. Activate the `PyTorch` virtual environment by running from the repository root folder:
            * Linux or Mac: `source ./venv/pytorch_cpu/bin/activate` 
            * Windows CMD: `.\venv\pytorch_cpu\Scripts\activate.bat`
            * Windows Powershell: `.\venv\pytorch_cpu\Scripts\Activate.ps1`
         D. Install the packages: `pip install -r requirements_pytorch_cpu.txt`
         E. Install `ipykernel`: `python -m ipykernel install --user --name=pytorch_cpu --display-name=pytorch_cpu`
         F. Repeat steps C-E for the `Tensorflow` virtual environment. Notice to modify any mention of 'pytorch' to 'tensorflow' in the commands. 
#### Notes
* For good context about Python's default `venv` module, see its (well-written) [official doc](https://docs.python.org/3/tutorial/venv.html))
* The reason we create two vitrual environments, and not simply one contining both, is due to a conflict with running `Tensorboard` on `PyTorch` while `Tensorflow` is installed within the same virtual environment ([Github Issue](https://github.com/pytorch/pytorch/issues/30966#issuecomment-576261087), with a potential [patch](https://github.com/pytorch/pytorch/issues/30966#issuecomment-582747929) that we're not following).

### Setting Up `vscode` to work with Notebooks and Virtual Environments
* To run Python notebooks in `vscode`, you first need to install the `Python` extension by Microsoft (done via the Extensions menu on the left sidebar).
* Then, open a notebook and set the right kernel (either `python_cpu` or `tensorflow_cpu`, depending of what the notebook is using). Setting the kernel is done on the top right side. 
* Note that if you see wiggly orange lines below the package names in the import statement, change the interpreter to that of the virtual environment ([stackoverflow](https://stackoverflow.com/a/72721797/10006823)).

### Testing the Setup
This is an important last step :) - to make sure that PyTorch, Tensorflow, the environments and the vscode integration were all set up correctly - open `setup/test_pytorch.py` and `setup/test_tensorflow.py` in `vscode`, set the right kernel for each, and run. If you get a `succeeded` message - these modules are working fine. 
