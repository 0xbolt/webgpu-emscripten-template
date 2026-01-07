import os

EMSDK_PATH = os.environ.get('EMSDK')
if not EMSDK_PATH:
    print('EMSDK not set. You must source emsdk/emsdk_env.sh before running this script.')
    exit(1)

dotclangd_path = os.path.join(os.path.dirname(__file__), '.clangd')
if os.path.exists(dotclangd_path):
    print('Please manually delete the already existing .clangd file if you wish to renegerate it.')
    exit(1)

dotclangd_str = """\
CompileFlags:
  Add:
    - --target=wasm32-unknown-emscripten
    - --sysroot={EMSDK_PATH}/upstream/emscripten/cache/sysroot
    - -isystem{EMSDK_PATH}/upstream/emscripten/cache/sysroot/include/c++/v1
    - -isystem{EMSDK_PATH}/upstream/emscripten/cache/sysroot/include
    - -isystem{EMSDK_PATH}/upstream/emscripten/cache/sysroot/include/compat
    - -I{EMSDK_PATH}/upstream/emscripten/cache/ports/emdawnwebgpu/emdawnwebgpu_pkg/webgpu_cpp/include/
    - -I{EMSDK_PATH}/upstream/emscripten/cache/ports/emdawnwebgpu/emdawnwebgpu_pkg/webgpu/include/
    - -I{EMSDK_PATH}/upstream/emscripten/cache/ports/contrib.glfw3/include/
    - -DEMSCRIPTEN
  Remove:
    - --use-port=contrib.glfw3
    - --use-port=emdawnwebgpu
""".format(EMSDK_PATH=EMSDK_PATH)

with open(dotclangd_path, 'x') as f:
    f.write(dotclangd_str)
