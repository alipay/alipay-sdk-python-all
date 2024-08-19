#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CaSdnDTO(object):

    def __init__(self):
        self._c = None
        self._cn = None
        self._o = None
        self._ou = None
        self._telephone_number = None

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = value
    @property
    def cn(self):
        return self._cn

    @cn.setter
    def cn(self, value):
        self._cn = value
    @property
    def o(self):
        return self._o

    @o.setter
    def o(self, value):
        self._o = value
    @property
    def ou(self):
        return self._ou

    @ou.setter
    def ou(self, value):
        self._ou = value
    @property
    def telephone_number(self):
        return self._telephone_number

    @telephone_number.setter
    def telephone_number(self, value):
        self._telephone_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.c:
            if hasattr(self.c, 'to_alipay_dict'):
                params['c'] = self.c.to_alipay_dict()
            else:
                params['c'] = self.c
        if self.cn:
            if hasattr(self.cn, 'to_alipay_dict'):
                params['cn'] = self.cn.to_alipay_dict()
            else:
                params['cn'] = self.cn
        if self.o:
            if hasattr(self.o, 'to_alipay_dict'):
                params['o'] = self.o.to_alipay_dict()
            else:
                params['o'] = self.o
        if self.ou:
            if hasattr(self.ou, 'to_alipay_dict'):
                params['ou'] = self.ou.to_alipay_dict()
            else:
                params['ou'] = self.ou
        if self.telephone_number:
            if hasattr(self.telephone_number, 'to_alipay_dict'):
                params['telephone_number'] = self.telephone_number.to_alipay_dict()
            else:
                params['telephone_number'] = self.telephone_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CaSdnDTO()
        if 'c' in d:
            o.c = d['c']
        if 'cn' in d:
            o.cn = d['cn']
        if 'o' in d:
            o.o = d['o']
        if 'ou' in d:
            o.ou = d['ou']
        if 'telephone_number' in d:
            o.telephone_number = d['telephone_number']
        return o


