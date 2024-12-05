from setuptools import find_packages, setup # find packages will find all the packages in the directory and setup will help in setting up the package
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
    
    requirements = [req.replace("\n", "") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name='mlproject', 
version='0.0.1',
author='Fiza',
author_email='fizarazvi10@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)