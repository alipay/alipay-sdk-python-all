#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOpenbizmockNewinterfaceQueryModel(object):

    def __init__(self):
        self._string_2 = None
        self._string_un = None

    @property
    def string_2(self):
        return self._string_2

    @string_2.setter
    def string_2(self, value):
        self._string_2 = value
    @property
    def string_un(self):
        return self._string_un

    @string_un.setter
    def string_un(self, value):
        self._string_un = value


    def to_alipay_dict(self):
        params = dict()
        if self.string_2:
            if hasattr(self.string_2, 'to_alipay_dict'):
                params['string_2'] = self.string_2.to_alipay_dict()
            else:
                params['string_2'] = self.string_2
        if self.string_un:
            if hasattr(self.string_un, 'to_alipay_dict'):
                params['string_un'] = self.string_un.to_alipay_dict()
            else:
                params['string_un'] = self.string_un
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOpenbizmockNewinterfaceQueryModel()
        if 'string_2' in d:
            o.string_2 = d['string_2']
        if 'string_un' in d:
            o.string_un = d['string_un']
        return o


