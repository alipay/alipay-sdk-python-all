#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAuthUnifygwtestQueryModel(object):

    def __init__(self):
        self._str = None

    @property
    def str(self):
        return self._str

    @str.setter
    def str(self, value):
        self._str = value


    def to_alipay_dict(self):
        params = dict()
        if self.str:
            if hasattr(self.str, 'to_alipay_dict'):
                params['str'] = self.str.to_alipay_dict()
            else:
                params['str'] = self.str
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAuthUnifygwtestQueryModel()
        if 'str' in d:
            o.str = d['str']
        return o


