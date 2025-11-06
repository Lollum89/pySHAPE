#!/usr/bin/env python3
"""
Minimal test to verify OpenGL rendering works with a simple triangle.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
import moderngl
from PIL import Image

# Create context
ctx = moderngl.create_standalone_context()

# Simple shaders
prog = ctx.program(
    vertex_shader='''
        #version 330
        in vec2 in_pos;
        in vec3 in_color;
        out vec3 v_color;
        void main() {
            gl_Position = vec4(in_pos, 0.0, 1.0);
            v_color = in_color;
        }
    ''',
    fragment_shader='''
        #version 330
        in vec3 v_color;
        out vec4 f_color;
        void main() {
            f_color = vec4(v_color, 1.0);
        }
    '''
)

# Triangle data (position + color)
vertices = np.array([
    # x, y, r, g, b
    0.0, 0.6, 1.0, 0.0, 0.0,  # top - red
    -0.6, -0.6, 0.0, 1.0, 0.0,  # bottom left - green
    0.6, -0.6, 0.0, 0.0, 1.0,  # bottom right - blue
], dtype='f4')

vbo = ctx.buffer(vertices.tobytes())
vao = ctx.vertex_array(prog, [(vbo, '2f 3f', 'in_pos', 'in_color')])

# Create framebuffer
fbo = ctx.framebuffer(
    color_attachments=[ctx.texture((512, 512), 4)]
)

# Render
fbo.use()
ctx.clear(0.1, 0.1, 0.1, 1.0)
vao.render(moderngl.TRIANGLES)

# Read and save
data = fbo.read(components=4)
img = Image.frombytes('RGBA', (512, 512), data).transpose(Image.FLIP_TOP_BOTTOM)
output_path = Path(__file__).parent / "test_render.png"
img.save(output_path)

print(f"✅ Render test successful!")
print(f"   Output saved to: {output_path}")
print(f"   Open the image to verify - you should see a colored triangle.")
