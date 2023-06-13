import bpy
import random

def array_multiple(array_count, duplicate): 
    name = 'single_grass'
    bpy.data.objects[name].select_set(True) # 2.8+
    bpy.ops.object.modifier_add(type='ARRAY')

    bpy.context.object.modifiers["Array"].count = array_count
    bpy.context.object.modifiers["Array"].relative_offset_displace[0] = 1.1
    bpy.ops.object.modifier_apply(modifier="Array")

    for x in range(duplicate):
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0)})
        bpy.ops.transform.translate(value=(0, 1, 0))

def select_all_and_random(name, duplicate):
    bpy.data.objects[name].select_set(True) # 2.8+

    for x in range(duplicate-1): 
        if len(str(x+1)) == 1: 
            new_name = name + '.00' + str(x+1)
            bpy.data.objects[new_name].select_set(True) 
        if len(str(x+1)) == 2: 
            new_name = name + '.0' + str(x+1)
            bpy.data.objects[new_name].select_set(True) 
        if len(str(x+1)) == 3: 
            new_name = name + '.' + str(x+1)
            bpy.data.objects[new_name].select_set(True) 

    bpy.ops.mesh.separate(type='LOOSE')
    bpy.ops.object.randomize_transform(loc=(3, 4, 0.5), rot=(0.5, 0.3, 0.2), scale=(0.7, 2, 0.5))
    bpy.ops.object.join()

array_multiple(10, 5)
select_all_and_random('single_grass', 5)
