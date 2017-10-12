bl_info = {
  'name': 'Test Addon',
  'author': 'Botmasher (Josh R)',
  'category': 'Object'
}

# consider module loading process in the following __init__ from Blender:
# https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_ui/__init__.py;420d4a70b8febfdfdab253c5d814aef5bb57dda0$26

from . import gui
modules = [gui]

import bpy
import os
import inspect

# register/unregister all classes
def register():
	from bpy.utils import register_class
	for module in modules:
		for member in inspect.getmembers(module, inspect.isclass):
			try:
				register_class(member[1]) 	# member is tuple ('className', <class>)
			except RuntimeError: 					# missing bl_rna; skip non-Blender classes 
				pass

def unregister():
	from bpy.utils import unregister_class
	for module in reversed(modules):
		for member in inspect.getmembers(module, inspect.isclass):
			try:
				unregister_class(member[1])
			except RuntimeError:
				pass

#if __name__ == '__main__':
#  register()