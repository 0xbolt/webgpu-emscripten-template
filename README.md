# webgpu-emscripten-template

## Setup
```
# Build
emcmake cmake -B build -GNinja && cmake --build build
# Run
python3 http.server build
```

## References
- https://github.com/emscripten-core/emsdk
- https://emscripten.org/index.html
- https://github.com/pongasoft/emscripten-glfw
- https://www.willusher.io/blog/build-ship-debug-wasm/
- https://floooh.github.io/2023/11/11/emscripten-ide.html
- https://github.com/emscripten-core/emscripten/blob/main/cmake/Modules/Platform/Emscripten.cmake