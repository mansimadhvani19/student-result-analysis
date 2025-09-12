from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_part:str)->List[str]:
    '''
    This function returns the list of requirements.
    '''

    requirements = []
    with open(file_part) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements

setup(
    name='student-result-analysis',
    version='0.0.1',
    author='Mansi Madhvani',
    author_email='mansi.madhvani19@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'), 

)