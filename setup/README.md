## Setup
To run the code on a local or remote machine, you can follow the recommendation below.
We use `pip` and `venv`, which are the default Python environment management system and are effective for that purpose.
### Prerequisite
* The code was tested using `Python` 3.10.9, and the environment was set up using `pip` and `venv` (rather than `conda`). The instructors use `vscode` as the IDE.
* Make sure you have a compatible version of Python (3.7.x-3.10.x) and the necessary tools `pip` and `git` installed. You can check if they are installed and see their versions by running `python --version` (or `python3 --version` depending on your setup), `pip --version` (or `pip3 --version`), and `git --version` in the command line. If any of these are missing, please install them according to the official guides: [python](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/installation/) and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
### Steps
1. To get a local copy of this repository, run `git clone https://github.com/RanFeldesh/aasd4011-2023-winter-nb` in the command line. This will create a new sub-folder with a local copy of the repository. Note that if you encounter any issues during the setup process below, you can delete this folder and start fresh by cloning again. The changes made during the setup should only affect files within this folder, so deleting it will give you a clean slate to work from.
2. The goal of the setup process is to create _two_ virtual environments, one for `PyTorch` and one for `Tensorflow`, both of which will be CPU-only and without GPU support. This works well for part 1 of the course, and simplifies the setup. The required packages as defined in the `requirements.txt` files will be installed in each environment, and `ipykernel` will be installed for each. There are two ways to accomplish this, so you can choose the method that works best for you:
    1. **Semi-automatically using the `setup.py` script**: From the repository root folder, run `python ./setup/setup.py`. This should complete all required steps for you. If you get no error, the setup should be completed, and you could verify it by testing it as described below. This script was tested on Windows and Ubuntu, but not Mac (although it is likely to work). If it does not work and you are unable to quickly debug the issue, simply delete the folder, go back to step 1, and try the manual version instead. Deleting the folder will revert any changes made. It may also be helpful to spend a few minutes reviewing `setup.py` to see how it implements the manual steps below.
    2. **Manually** - following the steps below in the command line:
        1. Create a subfolder named `venv` within the local repository folder, i.e. by `mkdir venv`
        2. `cd` into `venv` and initialize two environments by running (you will need to use `python3` instead of `python`, if that's your installed executable):
            * `python -m venv pytorch_cpu`
            * `python -m venv tensorflow_cpu`
        3. `cd` out back to the repository root folder, and activate the `PyTorch` virtual environment by running:
            * Linux or Mac: `source ./venv/pytorch_cpu/bin/activate` 
            * Windows CMD: `.\venv\pytorch_cpu\Scripts\activate.bat`
            * Windows Powershell: `.\venv\pytorch_cpu\Scripts\Activate.ps1`
         4. Install the packages: `pip install -r requirements_pytorch_cpu.txt`
         5. Install `ipykernel`: `python -m ipykernel install --user --name=pytorch_cpu --display-name=pytorch_cpu`
         6. Deactivate the environment by: `deactivate`
         6. Repeat steps c-f to set up the `Tensorflow` virtual environment. _Modify any mention of 'pytorch' to 'tensorflow' in the commands_.
#### Notes
* For a good context about Python's `venv` module, see its (well-written) [official doc](https://docs.python.org/3/tutorial/venv.html))
* The reason we create two vitrual environments, and not simply one environment containing both `PyTorch` and `Tensorflow`, is due to a conflict with running `Tensorboard` on `PyTorch` while `Tensorflow` is installed  ([Github Issue](https://github.com/pytorch/pytorch/issues/30966#issuecomment-576261087), with a potential [patch](https://github.com/pytorch/pytorch/issues/30966#issuecomment-582747929) that we're not following).

### Setting Up `vscode` to work with Notebooks and Virtual Environments
* `vscode` needs to be restarted after setting up the virtual environments for the first time. Otherwise, the environments will not be visible in `vscode`.
* To run Python notebooks in `vscode`, you first need to install the `Python` extension by Microsoft (done via the Extensions menu on the left sidebar).
* Then, open a notebook and set the right kernel (either `python_cpu` or `tensorflow_cpu`, depending of what the notebook is using). Setting the kernel is done on the top right side in `vscode`. 
* Note that if you see wiggly orange lines below the package names in the import statement, change the interpreter to that of the virtual environment by typing in the command-palette `Python: Select Interpreter` ([stackoverflow](https://stackoverflow.com/a/72721797/10006823)).

### Testing the Setup
To make sure that the `PyTorch` and `Tensorflow` environments, and the `vscode` integration were all set up correctly - open the files `setup/test_pytorch.ipynb` and `setup/test_tensorflow.ipynb` in `vscode`, set the right kernel for each (either `pytorch_cpu` or `tensorflow_cpu`), and run. If you get a `succeeded` message - these modules are working fine. 
