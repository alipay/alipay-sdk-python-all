#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtHrcominsuInsuclaimProgQueryModel(object):

    def __init__(self):
        self._data_key = None
        self._is_submit = None

    @property
    def data_key(self):
        return self._data_key

    @data_key.setter
    def data_key(self, value):
        self._data_key = value
    @property
    def is_submit(self):
        return self._is_submit

    @is_submit.setter
    def is_submit(self, value):
        self._is_submit = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_key:
            if hasattr(self.data_key, 'to_alipay_dict'):
                params['data_key'] = self.data_key.to_alipay_dict()
            else:
                params['data_key'] = self.data_key
        if self.is_submit:
            if hasattr(self.is_submit, 'to_alipay_dict'):
                params['is_submit'] = self.is_submit.to_alipay_dict()
            else:
                params['is_submit'] = self.is_submit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtHrcominsuInsuclaimProgQueryModel()
        if 'data_key' in d:
            o.data_key = d['data_key']
        if 'is_submit' in d:
            o.is_submit = d['is_submit']
        return o


