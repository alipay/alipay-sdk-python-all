#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AddressInfo import AddressInfo


class Aaabbbaaaa(object):

    def __init__(self):
        self._aaaa = None
        self._bbbb = None

    @property
    def aaaa(self):
        return self._aaaa

    @aaaa.setter
    def aaaa(self, value):
        if isinstance(value, AddressInfo):
            self._aaaa = value
        else:
            self._aaaa = AddressInfo.from_alipay_dict(value)
    @property
    def bbbb(self):
        return self._bbbb

    @bbbb.setter
    def bbbb(self, value):
        self._bbbb = value


    def to_alipay_dict(self):
        params = dict()
        if self.aaaa:
            if hasattr(self.aaaa, 'to_alipay_dict'):
                params['aaaa'] = self.aaaa.to_alipay_dict()
            else:
                params['aaaa'] = self.aaaa
        if self.bbbb:
            if hasattr(self.bbbb, 'to_alipay_dict'):
                params['bbbb'] = self.bbbb.to_alipay_dict()
            else:
                params['bbbb'] = self.bbbb
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Aaabbbaaaa()
        if 'aaaa' in d:
            o.aaaa = d['aaaa']
        if 'bbbb' in d:
            o.bbbb = d['bbbb']
        return o


