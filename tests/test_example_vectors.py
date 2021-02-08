#!/usr/bin/env python3
import pytest
from pymugi import Mugi

test_vectors = [
    {
    'name': 'Mugi Spec v1.2 - Test Vector Example 1',
    'key': '00000000000000000000000000000000',
    'iv' : '00000000000000000000000000000000',
    'result' : [
            0xc76e14e70836e6b6,
            0xcb0e9c5a0bf03e1e,
            0xacf9af49ebe6d67,
            0xd5726e374b1397ac,
            0xdac3838528c1e592,
            0x8a132730ef2bb752,
            0xbd6229599f6d9ac2,
            0x7c04760502f1e182,
        ]
    },{
    'name': 'Mugi Spec v1.2 - Test Vector Example 2',
    'key': '000102030405060708090A0B0C0D0E0F',
    'iv' : 'F0E0D0C0B0A090807060504030201000',
    'result': [
            0xbc62430614b79b71,
            0x71a66681c35542de,
            0x7aba5b4fb80e82d7,
            0xb96982890b6e143,
            0x4930b5d033157f46,
            0xb96ed8499a282645,
            0xdbeb1ef16d329b15,
            0x34a9192c4ddcf34e
        ]
    }
]

def test_vector_examples():
    for test in test_vectors:
        k = bytes.fromhex(test['key'])
        i = bytes.fromhex(test['iv'])
        m = Mugi(k, i)
        p = m.prng()
        expected = [hex(x) for x in test['result']]
        result = [hex(next(p)) for _ in range(8)]
        assert result == expected


