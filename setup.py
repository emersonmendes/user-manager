from setuptools import setup, find_packages  
from setuptools.command.install import install 
from setuptools.command.sdist import sdist    
import os
import db                
import compileall


class PostInstallCommand(install):
    def run(self):
        os.system("./install.sh")
        install.run(self)


class PostSDistCommand(sdist):
    def run(self):
        compileall.compile_dir(".") 
        sdist.run(self)


setup(                                                                          
    name="user-manager",                                                             
    version="0.1",                                                              
    description="User Manager API",                                               
    author="Emerson Mendes",                                                   
    author_email="emerson.emendes@gmail.com",                               
    url="https://github.com/emersonmendes",                                     
    packages=find_packages(exclude=['*.md','*.py' ]),
    install_requires=['Flask==0.12.2'],
    license="MIT",
    cmdclass={
        'install': PostInstallCommand,
        'sdist': PostSDistCommand
    }                                     
)     