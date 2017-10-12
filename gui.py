import bpy
from bpy.props import *
from .functions import HappyShouter

class TestPanel(bpy.types.Panel):
  bl_idname = 'VIEW_3D_Test'
  bl_label = 'Test Panel'
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'TOOLS'
  
  def draw(self, ctx):
    messenger = HappyShouter('Got this working')
    self.layout.label(messenger.exclaim())