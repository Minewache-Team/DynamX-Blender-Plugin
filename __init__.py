bl_info = {
    "name": "BlenderDynamXAddon",
    "author": "Sarocesch",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "Properties > DynamX",
    "description": "DynamX Copy",
    "category": "Object",
}

import bpy

class DYNAMX_PT_MainPanel(bpy.types.Panel):
    bl_label = "DynamX"
    bl_idname = "DYNAMX_PT_main_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    bl_category = "DynamX"

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        obj = context.object

        layout.label(text="DynamX Copy:")
        layout.prop(obj, "name", text="Objektname")

        layout.separator()

        layout.operator("dynamx.copy_wheel", text="Copy Wheel")
        layout.operator("dynamx.copy_steeringwheel", text="Copy Steeringwheel")
        layout.operator("dynamx.copy_hitbox", text="Copy Hitbox")
        layout.operator("dynamx.copy_seat", text="Copy Seat")

# Operatoren für spezifische JSON-Kopien
class DYNAMX_OT_CopyWheel(bpy.types.Operator):
    bl_idname = "dynamx.copy_wheel"
    bl_label = "Copy Wheel JSON"

    def execute(self, context):
        obj = context.object
        if not obj:
            self.report({'WARNING'}, "No Object")
            return {'CANCELLED'}

        data = (
            f"{obj.name}{{\n"
            f"    AttachedWheel: Saros-DynamX-Car-Pack-V3.wheel_bmw\n"
            f"    IsRight: false\n"
            f"    Position: {obj.location.x:.3f} {obj.location.y:.3f} {obj.location.z:.3f}\n"
            f"    IsSteerable: true\n"
            f"    MaxTurn: 0.7\n"
            f"    DrivingWheel: false\n"
            f"}}"
        )
        context.window_manager.clipboard = data
        self.report({'INFO'}, "Wheel JSON in Clipboard!")
        return {'FINISHED'}

class DYNAMX_OT_CopySteeringWheel(bpy.types.Operator):
    bl_idname = "dynamx.copy_steeringwheel"
    bl_label = "Copy Steeringwheel JSON"

    def execute(self, context):
        obj = context.object
        if not obj:
            self.report({'WARNING'}, "No Object")
            return {'CANCELLED'}

        data = (
            f"SteeringWheel{{\n"
            f"    PartName: {obj.name}\n"
            f"    BaseRotationQuat: 0.0 0.0 0.0 0.0\n"
            f"    Position: {obj.location.x:.3f} {obj.location.y:.3f} {obj.location.z:.3f}\n"
            f"}}"
        )
        context.window_manager.clipboard = data
        self.report({'INFO'}, "SteeringWheel JSON in Clipboard!")
        return {'FINISHED'}

class DYNAMX_OT_CopyHitbox(bpy.types.Operator):
    bl_idname = "dynamx.copy_hitbox"
    bl_label = "Copy Hitbox JSON"

    def execute(self, context):
        obj = context.object
        if not obj:
            self.report({'WARNING'}, "No Object")
            return {'CANCELLED'}

        data = (
            f"Shape_{obj.name}{{\n"
            f"    Scale: {obj.scale.x:.3f} {obj.scale.y:.3f} {obj.scale.z:.3f}\n"
            f"    Position: {obj.location.x:.3f} {obj.location.y:.3f} {obj.location.z:.3f}\n"
            f"}}"
        )
        context.window_manager.clipboard = data
        self.report({'INFO'}, "Hitbox JSON in Clipboard!")
        return {'FINISHED'}

class DYNAMX_OT_CopySeat(bpy.types.Operator):
    bl_idname = "dynamx.copy_seat"
    bl_label = "Copy Seat JSON"

    def execute(self, context):
        obj = context.object
        if not obj:
            self.report({'WARNING'}, "No Object")
            return {'CANCELLED'}

        data = (
            f"Seat_{obj.name}{{\n"
            f"    Position: {obj.location.x:.3f} {obj.location.y:.3f} {obj.location.z:.3f}\n"
            f"    Driver: false\n"
            f"}}"
        )
        context.window_manager.clipboard = data
        self.report({'INFO'}, "Seat JSON JSON in Clipboard!")
        return {'FINISHED'}

# Registrierung
classes = [
    DYNAMX_PT_MainPanel,
    DYNAMX_OT_CopyWheel,
    DYNAMX_OT_CopySteeringWheel,
    DYNAMX_OT_CopyHitbox,
    DYNAMX_OT_CopySeat
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
