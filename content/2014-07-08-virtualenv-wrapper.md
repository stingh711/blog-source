Title: Virtualenv wrapper
Date: 2014-07-08 13:00
Category: python
Tags: python mac
Slug: virtualenv-wrapper
Author: Sting
Summary: Virtualenv wrapper

Virtualenvwrapper is a set of extensions to easy the use of virtualenv tool. I only use its `workon` command to active or switch different virtualenvs.

To install it, use command `pip install virtualenvwrapper`. Then `export WORKON_HOME=~/Virtualenvs`. I put it in my .zshrc. Then `source /usr/local/bin/virtualenvwrapper.sh`.

Now you can active or switch a virtualenv use command `workon myenv` if it is in your WORKON_HOME. To create a new virtualenv, use command `mkvirtualenv env1`.

Here is its website: http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html
