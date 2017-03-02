import os
import pickle

APP_DIR = os.path.join(os.path.join(os.path.dirname(__file__),os.path.pardir),os.path.pardir)
SITES_FOLDER = APP_DIR+os.sep+'Jalapeno_data'+os.sep+'Sites'
print(APP_DIR,'+_+_')
class Site():

	def __init__(self,sitename):
		self.sitename = sitename

	@staticmethod
	def site_create(sitename):

		base_dir = APP_DIR + os.sep+'Jalapeno'+os.sep+'Sites'
		sitefolder = os.path.join(base_dir,sitename)
		subdir = {'Pages':None,
				  'build':None,
				  '_config':['_config.yaml','flask_settings.py','profile.yaml'],
				  'source':['image','extension']}
		if not os.path.exists(sitefolder):
			print("creating \'%s\' site folder"%sitename)
			os.mkdir(sitefolder)

			os.mkdir(sitefolder+os.sep+'Pages')

			os.mkdir(sitefolder+os.sep+'build')

			os.mkdir(sitefolder+os.sep+'source')
			os.mkdir(sitefolder+os.sep+'source'+os.sep+'image')
			os.mkdir(sitefolder+os.sep+'source'+os.sep+'extension')

			os.mkdir(sitefolder+os.sep+'_config')
			config_folder = sitefolder+os.sep+'_config'+os.sep
			for each in subdir['_config']:
				f = open(config_folder+each,'w')
				f.close()

		else:
			pass
	@staticmethod
	def site_switch(sitename):
		g=open(SITES_FOLDER+os.sep+'.siterc','rb')
		sitename,sitelist = pickle.load(g)
		if sitename not in sitelist:
			print('Site not exist')
			return
		f = open(SITES_FOLDER+os.sep+'.siterc','wb')
		pickle.dump((sitename,sitelist),f)
		f.close()
		print("Current site is '%s'"%sitename)
	@staticmethod
	def site_list_add(sitename):
		try:
			g=open(SITES_FOLDER+os.sep+'.siterc','rb')
			sitename,sitelist = pickle.load(g)
			sitelist.append(sitename)
			g.close()
		except:
			print('site_list_add Wrong')
	@staticmethod
	def get_site():
		g=open(SITES_FOLDER+os.sep+'.siterc','rb')
		sitename,sitelist = pickle.load(g)
		print(sitename,'++++')
		if sitename not in sitelist:
			print('Site not exist')
			return
		return sitename



SITE_DIR=SITES_FOLDER+os.sep+Site.get_site()





