from setuptools import find_packages, setup
from typing import List

def get_requirements(path:str)->List[str]:
    requirements=[]
    with open(path) as p:
        requirements=p.readlines()
        requirements=[req.replace('\n', '')for req in requirements]

    if "-e ." in requirements:
        requirements.remove("-e .")
    return(requirements)



setup(
    name='MLproject',
    version='0.0.1',
    author='Kiran',
    author_email='kanzariyakiran1307@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)