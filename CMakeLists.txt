cmake_minimum_required(VERSION 4.2)
project(WebgpuEmscriptenTemplate)

if(NOT EMSCRIPTEN)
    MESSAGE(FATAL_ERROR "Emscripten is required to compile this project.")
endif()

if(NOT DEFINED ENV{EMSDK} OR "$ENV{EMSDK}" STREQUAL "")
  message(FATAL_ERROR "Please source emsdk_env.sh.")
endif()

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(main main.cpp webgpu_glfw.cpp)
set_target_properties(main PROPERTIES
    OUTPUT_NAME index
    SUFFIX ".html")
target_compile_options(main PRIVATE
    --use-port=contrib.glfw3
    --use-port=emdawnwebgpu)
target_link_options(main PRIVATE
    --use-port=contrib.glfw3
    --use-port=emdawnwebgpu
    "SHELL:-sENVIRONMENT='web'"
    -sALLOW_MEMORY_GROWTH=1
    -sASYNCIFY=1
    $<$<CONFIG:Debug>:-g>
    $<$<CONFIG:Debug>:-O0>
    $<$<CONFIG:Release>:-Oz>
    $<$<CONFIG:Release>:--shell-file=${CMAKE_SOURCE_DIR}/shell.html>)