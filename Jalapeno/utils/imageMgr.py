from Jalapeno import flk
from flask import Blueprint,send_from_directory
import os
from Jalapeno.path import path
from Jalapeno.lib.fileMgr import Mgr 
from Jalapeno.lib.url_for_builder import path_url_builder

image = Blueprint('image',__name__)

image_path = path()+os.sep+'Jalapeno'+os.sep+'source'+os.sep+'image'


image_file_mgr = Mgr(image_path)

@flk.context_processor
def image_mgr():
	images = image_file_mgr.tree_dict()
	images_dict = path_url_builder(images,'image.img')
	return dict(image = images_dict)

@image.route('/image/<path:path>')
def img(path):
	return send_from_directory(flk.config['IMAGE_DIR'],
                               path, as_attachment=True)

flk.register_blueprint(image)