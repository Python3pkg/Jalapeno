from app import app
from flask import Blueprint,url_for
asset = Blueprint("asset", __name__, template_folder='templates')
import os
import pickle
current_path= os.getcwd()+'/app/static'



@app.context_processor
def utility_processor():
        asset_mgr=Mgr(current_path)

        return dict(asset=asset_mgr.tree(asset_mgr.tree_dict()))


class Mgr(object):

        def __init__(self,path):
                self.path = path
                self.name = 'theme_static'
        def dir(self):
                return self.path
        def tree_dict(self):    
                return self.tree(self.dir())
        def tree(self,path,relative_path=''):
                L={}
                content=os.listdir(path)
                for each in content:
                        each_path = path+os.sep+each                                    
                        record = relative_path + each + os.sep
                        if each[0]=='.' or 'img' in each:
                                continue
                        elif os.path.isdir(each_path):
                                L[each]=self.tree(path=each_path,relative_path=record)
                        else:
                                L[each.split('.',1)[0]] = relative_path+each
                return L
                
