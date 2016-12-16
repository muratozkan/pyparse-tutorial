Installing PyParsing
====================

 -  Install Python3 and pip 

        brew install python3

 - *Optional* Install and configure `virtualenv` and `virtualenvwrapper`

        pip install virtualenvwrapper
 
   Then add the following to your console startup script (usually `.bash_profile` for bash on OSX) 

        # Python
        # from https://gist.github.com/pithyless/1208841
        export WORKON_HOME=$HOME/.virtualenvs
        export PIP_VIRTUALENV_BASE=$WORKON_HOME
        export PIP_RESPECT_VIRTUALENV=true
        
        . /usr/local/bin/virtualenvwrapper.sh
        
   Restart your terminal now. 

 - Create a virtual environment to work on
 
        mkvirtualenv --python=python3 pyparse-tutorial
 
 - Install pyparsing form PyPI

        pip install pyparsing

 You can deactivate the current environment with: 
 
     deactivate

 and resume your work with this command 
 
     workon pyparse-tutorial 