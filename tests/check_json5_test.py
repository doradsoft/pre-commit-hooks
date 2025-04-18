from __future__ import annotations

import pytest

from pre_commit_hooks.check_json5 import main
from testing.util import get_resource_path


@pytest.mark.parametrize(
    ('filename', 'expected_retval'), (
        ('bad_json5.notjson', 1),
        ('ok_json5.json', 0),
        ('duplicate_key_json5.notjson', 1),
    ),
)
def test_main(capsys, filename, expected_retval):
    ret = main([get_resource_path(filename)])
    assert ret == expected_retval
    if expected_retval == 1:
        stdout, _ = capsys.readouterr()
        assert filename in stdout


def test_non_utf8_file(tmpdir):
    f = tmpdir.join('t.json5')
    f.write_binary(b'\xa9\xfe\x12')
    assert main((str(f),))
