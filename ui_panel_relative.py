import bpy


class RelativePositionPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Mi paneluku"
    bl_idname = "OBJECT_My_Rel_pos"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Show parent relative position", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")
        
        vector = obj.matrix_world.translation - obj.parent.matrix_world.translation
        
        row = layout.row()
        row.label(text="X: " + str(vector.x))
        row.label(text="Y: " + str(vector.y))
        row.label(text="Z: " + str(vector.z))
        

        row = layout.row()
        row.operator("mesh.primitive_cube_add")


def register():
    bpy.utils.register_class(RelativePositionPanel)


def unregister():
    bpy.utils.unregister_class(RelativePositionPanel)


if __name__ == "__main__":
    register()
