#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GavintestNewLeveaOne import GavintestNewLeveaOne


class AlipayOpenPublicComptestCreateModel(object):

    def __init__(self):
        self._address = None
        self._string = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        if isinstance(value, list):
            self._string = list()
            for i in value:
                if isinstance(i, GavintestNewLeveaOne):
                    self._string.append(i)
                else:
                    self._string.append(GavintestNewLeveaOne.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.string:
            if isinstance(self.string, list):
                for i in range(0, len(self.string)):
                    element = self.string[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.string[i] = element.to_alipay_dict()
            if hasattr(self.string, 'to_alipay_dict'):
                params['string'] = self.string.to_alipay_dict()
            else:
                params['string'] = self.string
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicComptestCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'string' in d:
            o.string = d['string']
        return o


