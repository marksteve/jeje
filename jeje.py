import codecs
import re
import random

"""
jeje.py

A simple jeje encoder

In [1]: import jeje

In [2]: u"Mininaniko ni Moniko ang makina ng manika ni Monika".encode("jeje")
Out[2]: u'MiNhInhaNhikh0 nhi m0nHIkh0 HAng MHakhINHa ng MhAnHIkha nHi mh0NkhaH'

NOTE: Encoders shouldn't work like this. This is just a demo.

"""


pat_h = re.compile('([^h])([aeiou])')
pat_h2 = re.compile('([aeiou])$')
pat_mv = re.compile('^(.+)[aeuiou](.+)')
P = lambda p: random.randint(0, 100) < p


def jejefy(s):
    s = s.lower()
    if P(33):  # remove vowels
        s = pat_mv.sub(r'\1\2', s)
    if P(66):
        s = s.replace('h', 'j')
    if P(33):
        s = pat_h.sub(r'\1h\2', s)
    if P(66):
        s = pat_h2.sub(r'\1h', s)
    if P(33):
        s = s.replace('e', '3')
    if P(66):
        s = s.replace('o', '0')
    if P(33):
        s = s.replace('i', '1')
    if P(66):
        s = s.replace('s', 'z')
    s = ''.join([c.upper() if P(33) else c for c in s])
    return s


class JejeCodec(codecs.Codec):
    def encode(self, s, errors='strict'):
        s = jejefy(s)
        return s, len(s)

    def decode(self, s, errors='strict'):
        raise RuntimeError("You can't decode Jeje")


def jeje(s):
    if s == 'jeje':
        return codecs.CodecInfo(
            name="jeje",
            encode=JejeCodec().encode,
            decode=JejeCodec().decode)
    return None

