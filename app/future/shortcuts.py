import os
'''
        This file is build for future post-installation parts
        Help user get a shortcut at user's home dir
'''
source = os.getcwd()+os.sep+'app'
home = os.path.expanduser("~")
base = home+os.sep+'Jalapeno'

page_source = source+os.sep+'page'
page = base+os.sep+'page'

build_source = source+os.sep+'build'
build = source + os.sep + 'build'
os.symlink(source,base)

