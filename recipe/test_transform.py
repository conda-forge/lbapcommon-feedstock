"""Test that LbAPCommon can transform YAML by propagating defaults.

This requires qjs (QuickJS) to be installed in the environment.
"""
from LbAPCommon.transforms.runner import transform_yaml

INFO_YAML_WITH_DEFAULTS = """\
defaults:
  application: DaVinci/v64r7
  wg: B2OC

TestJob_MagDown:
  input:
    bk_query: /some/path
"""

result = transform_yaml(INFO_YAML_WITH_DEFAULTS)

# Verify the job exists in output
assert "TestJob_MagDown:" in result, "Job not found in output"

# Verify defaults were propagated to the job
assert "application: DaVinci/v64r7" in result, "application not propagated"
assert "wg: B2OC" in result, "wg not propagated"

# The defaults section should be removed after propagation
assert "defaults:" not in result, "defaults section should be removed"

print("YAML transformation test passed!")
