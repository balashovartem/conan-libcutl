from conans import ConanFile, CMake, tools, ConfigureEnvironment
import os

channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "balashovartem")

class LibCutlConan(ConanFile):
    name = "libcutl"
    version = "1.10.0"
    license = "MIT"
    url = "https://github.com/balashovartem/conan-libcutl"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    source_tgz = "http://www.codesynthesis.com/download/libcutl/1.10/libcutl-1.10.0.tar.gz"

    def source(self):
        self.output.info("Downloading %s" % self.source_tgz)
        tools.download(self.source_tgz, "libcutl-1.10.0.tar.gz")
        tools.unzip("libcutl-1.10.0.tar.gz", ".")
        os.unlink("libcutl-1.10.0.tar.gz")

    def build(self):
	env = ConfigureEnvironment(self.deps_cpp_info, self.settings)
	self.run(" cd %s/libcutl-1.10.0 && %s ./configure --prefix=%s/install" % (self.conanfile_directory, env.command_line, self.conanfile_directory ) )
	self.run(" cd %s/libcutl-1.10.0 && %s make install"  % (self.conanfile_directory, env.command_line)  )

    def package(self):
        self.copy("*", dst="./", src="install", keep_path=True)

    def package_info(self):
        self.cpp_info.libs = ["hello"]
