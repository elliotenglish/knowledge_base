# Build Systems

## Bazel

### Foreign Rules CC

- `out_shared_libs` must include all libraries that will be the bazel-bin output. In general this includes the version numbers of the shared object extension. e.g. libsomething.so.4.1. Check what readelf displays in the dependent executable.
- `deps` can include dependencies allowing the target being specified to full fit within the bazel dependency hierarchy. The includes/libraries of the dependencies can be past in the various other options strings using the `$EXT_BUILD_DEPS` variable. Some notes on these are here (https://github.com/bazel-contrib/rules_foreign_cc/blob/21e463ed4498d1eb7f5eb0ac78302d03f55de92f/foreign_cc/private/framework.bzl#L371). Note that this functionality seems to be broken currently (https://github.com/bazel-contrib/rules_foreign_cc/issues/418) as include directories are reconstructed flattened.
- The version of `make` used by foreign_rules_cc is fixed by default and is not the system make (https://github.com/bazel-contrib/rules_foreign_cc/issues/898). When initializing foreign_rules_cc call the initializer as follows `rules_foreign_cc_dependencies(register_built_tools=False)` in order to to use only the preinstalled tools. Currently you can't switch only make while keeping the rest of the defaults (cmake, etc.).
