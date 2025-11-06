#!/usr/bin/env python3
"""
Test script to verify OpenGL installation and basic functionality.
Run this before using the GUI viewer to check if OpenGL is properly set up.
"""

import sys

def test_imports():
    """Test if all required packages can be imported."""
    print("Testing package imports...")
    results = {}
    
    # Core dependencies
    try:
        import numpy
        results['numpy'] = f"✅ {numpy.__version__}"
    except ImportError as e:
        results['numpy'] = f"❌ Not installed ({e})"
    
    # OpenGL
    try:
        import OpenGL
        from OpenGL.GL import glGetString, GL_VERSION
        results['PyOpenGL'] = f"✅ {OpenGL.__version__}"
    except ImportError as e:
        results['PyOpenGL'] = f"❌ Not installed ({e})"
    
    # ModernGL
    try:
        import moderngl
        results['moderngl'] = f"✅ {moderngl.__version__}"
    except ImportError as e:
        results['moderngl'] = f"❌ Not installed ({e})"
    
    # PIL/Pillow
    try:
        import PIL
        results['Pillow'] = f"✅ {PIL.__version__}"
    except ImportError as e:
        results['Pillow'] = f"❌ Not installed ({e})"
    
    # Optional: tkinterdnd2
    try:
        import tkinterdnd2
        results['tkinterdnd2'] = f"✅ Installed (drag-and-drop enabled)"
    except ImportError:
        results['tkinterdnd2'] = "⚠️  Not installed (optional - drag-and-drop disabled)"
    
    # Matplotlib (fallback)
    try:
        import matplotlib
        results['matplotlib'] = f"✅ {matplotlib.__version__} (fallback renderer)"
    except ImportError as e:
        results['matplotlib'] = f"⚠️  Not installed ({e})"
    
    return results

def test_opengl_context():
    """Test if OpenGL context can be created."""
    print("\nTesting OpenGL context creation...")
    try:
        import moderngl
        ctx = moderngl.create_standalone_context()
        info = ctx.info
        print(f"✅ OpenGL context created successfully")
        print(f"   Vendor: {info.get('GL_VENDOR', 'Unknown')}")
        print(f"   Renderer: {info.get('GL_RENDERER', 'Unknown')}")
        print(f"   Version: {info.get('GL_VERSION', 'Unknown')}")
        ctx.release()
        return True
    except Exception as e:
        print(f"❌ Failed to create OpenGL context: {e}")
        return False

def test_shader_compilation():
    """Test if shaders can be compiled."""
    print("\nTesting shader compilation...")
    try:
        import moderngl
        ctx = moderngl.create_standalone_context()
        
        vertex_shader = '''
            #version 330
            in vec3 in_pos;
            void main() {
                gl_Position = vec4(in_pos, 1.0);
            }
        '''
        
        fragment_shader = '''
            #version 330
            out vec4 fragColor;
            void main() {
                fragColor = vec4(1.0, 0.0, 0.0, 1.0);
            }
        '''
        
        prog = ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        print("✅ Shader compilation successful")
        ctx.release()
        return True
    except Exception as e:
        print(f"❌ Shader compilation failed: {e}")
        return False

def main():
    print("=" * 60)
    print("OpenGL Installation Test for SHAPE Viewer")
    print("=" * 60)
    
    # Test imports
    results = test_imports()
    print("\nPackage Status:")
    for pkg, status in results.items():
        print(f"  {pkg:15s}: {status}")
    
    # Count failures
    failures = sum(1 for v in results.values() if '❌' in v)
    
    if failures > 0:
        print(f"\n❌ {failures} required package(s) missing!")
        print("\nTo install missing packages:")
        print("  Windows: python\\install_opengl.bat")
        print("  Linux/Mac: bash python/install_opengl.sh")
        print("  Or: pip install PyOpenGL PyOpenGL-accelerate moderngl pillow")
        return 1
    
    # Test OpenGL functionality
    context_ok = test_opengl_context()
    shader_ok = test_shader_compilation()
    
    print("\n" + "=" * 60)
    if context_ok and shader_ok:
        print("✅ All tests passed! OpenGL is ready to use.")
        print("\nYou can now run the GUI viewer:")
        print("  python python/examples/gui_shape_viewer.py")
    else:
        print("⚠️  Some OpenGL tests failed.")
        print("\nThe viewer will fall back to matplotlib rendering.")
        print("Update your graphics drivers if you want OpenGL acceleration.")
    print("=" * 60)
    
    return 0 if (context_ok and shader_ok) else 2

if __name__ == '__main__':
    sys.exit(main())
