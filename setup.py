from setuptools import find_packages,setup
from typing import List

def get_requirments(file_path:str)->List[str]: 
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments] 
        return requirments
    
    
setup(
    
    name='DiamondPricePrediction',
    version="0.0.1",
    author="garvit",
    author_email="example@gmail.com",
    install_reqires=get_requirments('requirments.txt'),
    packages=find_packages()
)

