from flask import Flask
import os


#Flask init
flk = Flask(__name__)
from Jalapeno.utils.flatpage import articles
from Jalapeno.utils import configuration
from Jalapeno.utils import excerpt
from Jalapeno.utils import theme
from Jalapeno.utils import viewer
from Jalapeno.utils import shortcut
from Jalapeno.utils import articleimg
from Jalapeno.utils.flaskfroze import freezer
