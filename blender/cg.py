import bpy
import mathutils
from mathutils import Vector

def triangles (verts):
    """enumerate triangles in a face"""
    for i in range (1, len(verts)-1):
        yield (verts[0], verts[i], verts[i+1])

def cg_mesh (obj):
    """center of mass (and volume) of a mesh"""

    center = Vector()
    volume = 0
    mesh = obj.to_mesh (bpy.context.scene, True, 'PREVIEW')
    for face in mesh.polygons:
        f = face.vertices
        for t in triangles (f):
            a,b,c = (mesh.vertices[v].co for v in t)
            v = a.cross(b).dot(c) / 6
            center += v * (a+b+c) / 4
            volume += v
    bpy.data.meshes.remove(mesh)

    if volume == 0: print ("ZERO VOLUME", obj.name)
    else          : center /= volume

    return obj.matrix_world * center

# puts the cursor at the active object's center of mass
bpy.context.scene.cursor_location = cg_mesh (bpy.context.scene.objects.active)