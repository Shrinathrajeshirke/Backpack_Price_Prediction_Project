from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    try:
        with open(file_path,"r") as file_obj:
            requirements=file_obj.readlines()
            for req in requirements:
                requirement = req.strip()
                if requirement and requirement != '-e .':
                    requirements.append(requirement)
    except FileNotFoundError:
        print("requirement.txt file not found")
    return requirements

setup(
    name="Backpack price prediction project",
    version=0.0.1,
    author="Shrinath",
    author_email="shrinathrajeshirke@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
