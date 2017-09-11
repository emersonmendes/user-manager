from setuptools import setup, find_packages  
from setuptools.command.install import install     
import os
import db                                            

class PostInstallCommand(install):
    def run(self):
        os.system("./install.sh")


setup(                                                                          
    name="UserManager",                                                             
    version="0.1",                                                              
    description="User Manager API",                                               
    author="Emerson Mendes",                                                   
    author_email="emerson.emendes@gmail.com",                               
    url="https://github.com/emersonmendes",                                     
    packages=find_packages(exclude=['*.md', ]),
    install_requires=['Flask==0.12.2'],
    license="MIT",
    cmdclass={
        'install': PostInstallCommand
    }                                     
)     