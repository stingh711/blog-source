Title: How to make company's auto complete work for python on emacs
Date: 2014-11-13 17:04
Category: emacs
Tags: python, emacs
Author: Sting
Slug: how-to-setup-python-autocomplete-in-emacs
Summary: How to make company work for python in emacs

There are a lot ways to setup emacs as a python IDE. I tried some of them and still failed to setup my own. (I'm an emacs newbie) After some google works, I finally find a way to make auto complete and virtualenvs work.
## Install el-get

Elpa and melpa are really slow in China. So I use el-get because it uses github to install most of packages.
## Install company mode

`M-x el-get-install<RET>company-mode<RET>`
## Install company-anaconda

`M-x el-get-install<RET>company-anaconda<RET>`

## Install python dependencies of anaconda-mode

company-anaconda will install anaconda automatically. However, it seems doesn't install the python dependencies. To install it, cd to ~/.emacs.d/el-get/anaconda-mode and run command `pip install -r requirements.txt -t .` But I got following error on my mac: `error: must supply either home or prefix/exec-prefix -- not both`. I googled the error and got the solution on StackOverFlow. The link is [here](http://stackoverflow.com/questions/24257803/distutilsoptionerror-must-supply-either-home-or-prefix-exec-prefix-not-both).

Sofar, auto completion for python should work.
After this step, I found pip doesn't work. Please delete .pydistutils.cfg...

## Install pyvenv

`M-x el-get-install<RET>pyvenv<RET>`

## Make ipython the default python interpreter

Emacswiki has the configuration to use ipython in python.el. [Link](http://www.emacswiki.org/PythonProgrammingInEmacs)

