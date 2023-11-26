from pybind11.setup_helpers import Pybind11Extension, build_ext


class my_build_ext(build_ext):
    def build_extensions(self):
        if self.compiler.compiler_type == "unix":
            for e in self.extensions:
                e.extra_compile_args = ["-std=c++17", "-msse4.2", "-mavx2"]
        elif self.compiler.compiler_type == "msvc":
            for e in self.extensions:
                e.extra_compile_args = ["/std:c++17", "/arch:AVX2"]

        build_ext.build_extensions(self)


def build(setup_kwargs):
    ext_modules = [
        Pybind11Extension("cmajiang",
            [
                "src_cpp/cmajiang.cpp",
                "src_cpp/game.cpp",
                "src_cpp/he.cpp",
                "src_cpp/hule.cpp",
                "src_cpp/shan.cpp",
                "src_cpp/shoupai.cpp",
                "src_cpp/xiangting.cpp",
                "src_cpp/feature.cpp",
                "src_cpp/random.cpp",
                "src_cpp/paipu.cpp",
                "src_cpp/svg.cpp",
                "src_cpp/tinyxml2.cpp",
            ],
            language="c++",
            include_dirs=[
                "src_cpp",
            ]
        ),
    ]
    setup_kwargs.update({
        "ext_modules": ext_modules,
        "cmd_class": {"build_ext": my_build_ext},
        "zip_safe": False,
    })