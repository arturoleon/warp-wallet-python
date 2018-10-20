import unittest
from warpwallet import utils


class TestUtils(unittest.TestCase):
    def test_varint(self):
        self.assertEqual(utils.varint(0x42), '\x42')
        self.assertEqual(utils.varint(0x123), '\xfd\x23\x01')
        self.assertEqual(utils.varint(0x12345678), '\xfe\x78\x56\x34\x12')
        self.assertEqual(utils.processVarInt(utils.varint(0x42)), [0x42, 1])
        self.assertEqual(utils.processVarInt(utils.varint(0x1234)), [0x1234, 3])

    def test_varstr(self):
        self.assertEqual(utils.varstr('abc'), '\x03abc')
        self.assertEqual(utils.processVarStr('\x03abc'), ['abc', 4])

    def test_process_addr(self):
        self.assertEqual(utils.processAddr('x'*20 + '\x62\x91\x98\x16\x20\x8d'),
                         '98.145.152.22:8333')

    def test_count_leading_characters(self):
        self.assertEqual(utils.countLeadingChars('a\0bcd\0', '\0'), 0)
        self.assertEqual(utils.countLeadingChars('\0\0a\0bcd\0', '\0'), 2)
        self.assertEqual(utils.countLeadingChars('1a\0bcd\0', '1'), 1)

    def test_base256(self):
        self.assertEqual(utils.base256encode(utils.base256decode('abc')), 'abc')
        self.assertEqual(utils.base256encode(0x4142), 'AB')
        self.assertEqual(utils.base256decode('AB'), 0x4142)

    def test_base58(self):
        self.assertEqual(utils.base58encode(utils.base58decode('abc')), 'abc')
        self.assertEqual(utils.base58decode('121'), 58)
        self.assertEqual(utils.base58decode('5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ'),
                         0x800C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D507A5B8D)

    def test_base58check(self):
        self.assertEqual(utils.base58CheckDecode(utils.base58CheckEncode(42, 'abc')), 'abc')
        self.assertEqual(utils.base58CheckDecode(utils.base58CheckEncode(0, '\0\0abc')), '\0\0abc')
        s = utils.base256encode(0x0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D)
        b = utils.base58CheckEncode(0x80, s)
        self.assertEqual(b, "5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ")

if __name__ == '__main__':
    unittest.main()
