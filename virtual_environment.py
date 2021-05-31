"""
pip: pypi (python package index) package management tool
Package Loading:
§ from PyPI: pip install requests
§ from a local wheel file: pip install requests-2.22.0-py2.py3-none-any.whl
§ from a Git repository: pip install git+https://github.com/psf/requests.git
§ from a directory: pip install /home/user/src/requests
Package Installation by Versions:
§ Install specific version: pip install requests==2.22.0
§ Install most recent version in a range: pip install requests>=2.22.0,<3
§ Install package, avoid a specific version: pip install requests!=2.21.0
Exporting Versions of Packages in Current Environment:
§ pip freeze > requirements.txt
Importing the Package Versions Saved to the Environment:
§ pip install -r requirements.txt

conda: package and venv management tool (anaconda repository)
§ Install package:
conda install numpy
§ Install packages:
conda install numpy scipy pandas
§ Install package with specific version:
conda install numpy=1.10
§ Remove package:
conda remove package_name
§ Listing installed packages:
conda list
§ Upgrade package:
conda upgrade conda
§ Upgrade all packages:
conda upgrade –all
§ Update current package:
conda update package_name
§ Update all current package:
conda update –all
§ Search package:
conda search *search_term*
§ Entering an environment:
conda activate my_env
§ Deactivate an environment:
conda deactivate
§ listing environments
conda env list
§ Creating environment with specific version of python:
conda create -n py3 python = 3
§ Creating environment with specific Python version and packages:
conda create -n mvk python=3 pandas numpy
§ Creating environment with packages:
conda create -n env_name list of packages
§ To list all of the packages in a deactivated environment:
conda list -n myenv
§ Removing environments
conda env remove -n env_name
§ Saving the packages to a YAML file
conda env export> environment.yaml
§ Loading yaml file
conda env create -f environment.yaml

Application
§ conda env list
§ conda create -n my-env
§ conda activate my-env
§ conda list
§ conda install numpy
§ conda list
§ pip install pandas
§ conda list
§ conda deactivate
§ conda env remove -n myenv
§ conda env list
"""