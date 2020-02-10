"""Testing for the python bindings of the C++ flagser library."""

import os

import pytest
from numpy.testing import assert_almost_equal

from pyflagser import loadflag, flagser

flag_files = []

dirname = os.path.join(os.path.dirname(__file__), "../../flagser/test")
for file in os.listdir(dirname):
    if file.endswith(".flag"):
        flag_files.append(os.path.join(dirname, file))

betti = {
    'a.flag': [1, 2, 0],
    'b.flag': [1, 0, 0],
    'c.flag': [1, 5],
    'd.flag': [1, 0, 1],
    'e.flag': [1, 0, 0, 0],
    'f.flag': [1, 0, 0],
    'd2.flag': [1, 1],
    'd3.flag': [1, 0, 2],
    'd3-allzero.flag': [1, 0, 2],
    'double-d3.flag': [1, 0, 5],
    'double-d3-allzero.flag': [1, 0, 5],
    'd4.flag': [1, 0, 0, 9],
    'd4-allzero.flag': [1, 0, 0, 9],
    'd5.flag': [1, 0, 0, 0, 44],
    'd7.flag': [1, 0, 0, 0, 0, 0, 1854],
    'medium-test-data.flag': [14237, 39477, 378, 0],
    'd10.flag': [1, 0, 0, 0, 0, 0, 0, 0, 0, 1334961],
}


@pytest.mark.parametrize("flag_file, betti",
                         [(flag_file, betti[os.path.split(flag_file)[1]])
                          for flag_file in flag_files
                          if os.path.split(flag_file)[1] in betti.keys()])
def test_flagser(flag_file, betti):
    flag_matrix = loadflag(flag_file)

    ret = flagser(flag_matrix)
    assert_almost_equal(ret['betti'], betti)
