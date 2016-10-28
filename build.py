from conan.packager import ConanMultiPackager

if __name__ == "__main__":

    builder = ConanMultiPackager()
    builder.add_common_builds()
    filtered_builds = []
    for settings, options in builder.builds:
        if settings["compiler.version"] == "4.8" or settings["compiler.version"] == "5.2":
             filtered_builds.append([settings, options])
    builder.builds = filtered_builds
    builder.run()