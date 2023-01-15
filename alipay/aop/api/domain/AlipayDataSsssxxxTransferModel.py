#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataSsssxxxTransferModel(object):

    def __init__(self):
        self._ddd = None

    @property
    def ddd(self):
        return self._ddd

    @ddd.setter
    def ddd(self, value):
        self._ddd = value


    def to_alipay_dict(self):
        params = dict()
        if self.ddd:
            if hasattr(self.ddd, 'to_alipay_dict'):
                params['ddd'] = self.ddd.to_alipay_dict()
            else:
                params['ddd'] = self.ddd
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataSsssxxxTransferModel()
        if 'ddd' in d:
            o.ddd = d['ddd']
        return o


