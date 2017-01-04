from Jalapeno.utils.flatpage import articles
from flask import render_template_string
from markupsafe import Markup
from flask_flatpages import pygmented_markdown


def Jalop_markdown(text,flatpages=articles):

	'''pygments requires a flatpages parameter
	'''
	

	return Markup(pygmented_markdown(render_template_string(text),flatpages))