#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtHrcominsuInsuclaimQueryModel(object):

    def __init__(self):
        self._data_key = None

    @property
    def data_key(self):
        return self._data_key

    @data_key.setter
    def data_key(self, value):
        self._data_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_key:
            if hasattr(self.data_key, 'to_alipay_dict'):
                params['data_key'] = self.data_key.to_alipay_dict()
            else:
                params['data_key'] = self.data_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtHrcominsuInsuclaimQueryModel()
        if 'data_key' in d:
            o.data_key = d['data_key']
        return o


