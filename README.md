# webgpu-emscripten-template
A minimal WebGPU emscripten template.

## Requirements
- [emsdk](https://github.com/emscripten-core/emsdk)
- clang
- [WebAssembly DWARF Debugging VSCode Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.wasm-dwarf-debugging)
- ninja

This template was tested on MacOS only, although it should work fine on Linux. I don't think it works on Windows.

I highly recommend that you use emsdk. In particular, CMakeLists.txt is configured such that the project stops compilation if emsdk_env.sh was not sourced.

## Build
```
# Debug build
emcmake cmake -B build -GNinja -DCMAKE_BUILD_TYPE=Debug && cmake --build build
# Release build
emcmake cmake -B build-release -GNinja -DCMAKE_BUILD_TYPE=Release && cmake --build build-release
```

Please check the compiler options set for these two different types in [`CMakeLists.txt`](CMakeLists.txt)

You may then serve the `./build` folder and open `./build/main.html` file in the browser.

## Intellisense
If you use clangd, a `dotclangd_gen.py` script is provided that can create an adequate `.clangd` configuration file.

## Debug
An appropriate [VSCode launch configuration](.vscode/launch.json) is provided for debugging. Please note that:
- It is necessary to serve the build folder before starting debugging, for which you may run the provided ["serve" task](.vscode/tasks.json).
- The [WebAssembly DWARF Debugging VSCode Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.wasm-dwarf-debugging) should be installed so that the inlined WASM debug symbols may be properly recognized.

## References
- [emscripten-glfw](https://github.com/pongasoft/emscripten-glfw)
- [emdawnwebgpu](https://github.com/google/dawn/tree/main/src/emdawnwebgpu/pkg)
- [emcc (Emscripten Docs)](https://emscripten.org/docs/tools_reference/emcc.html)
- [emcc settings (Emscripten Docs)](https://emscripten.org/docs/tools_reference/settings_reference.html)
- [Building, Shipping and Debugging a C++ WebAssembly App (Article)](https://www.willusher.io/blog/build-ship-debug-wasm/)
- [WASM Debugging with Emscripten and VSCode (Article)](https://floooh.github.io/2023/11/11/emscripten-ide.html)
- [Build an app with WebGPU (Article)](https://developer.chrome.com/docs/web-platform/webgpu/build-app)
- [Debugging Assembly (VSCode Docs)](https://code.visualstudio.com/docs/nodejs/nodejs-debugging#_debugging-webassembly)
- [Deprecation of -sUSE_WEBGPU](https://github.com/emscripten-core/emscripten/issues/24265)
- [Usage of `--use-port=contrib.glfw3`](https://github.com/pongasoft/emscripten-glfw/blob/1f81297e958559a52d78be6fd326e47f16156eff/README.md#:~:text=With%20CMake%2C%20you%20need%20to%20provide%20the%20option%20both%20for%20compile,target_link_options(%24%7Btarget%7D%20PUBLIC%20%22%2D%2Duse%2Dport%3Dcontrib.glfw3%22))
- [Usage of `--use-port=emdawnwebgpu`](<https://dawn.googlesource.com/dawn/+/01940842b667a7812d0e4ca0ef4367fbec294241/src/emdawnwebgpu/pkg/README.md#:~:text=and%20configures%20it.-,Pass%20the%20following%20flag%20to%20emcc%20during%20both%20compilation%20and%20linking,%2D%2Duse%2Dport%3Demdawnwebgpu,-Latest%3A%20%E2%80%9CRemote%E2%80%9D%20port>)
- [Dear ImGui: Standalone Example Application for GLFW + WebGPU](https://github.com/ocornut/imgui/tree/7b3ad4a282dc6f5007c49d35853e32f364e3e3d7/examples/example_glfw_wgpu)
- [Deploying Emscripten Compiled Pages (Emscripten Docs)](https://emscripten.org/docs/compiling/Deploying-Pages.html)
