#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSmsgDataSetModel(object):

    def __init__(self):
        self._paramone = None
        self._paramtwo = None

    @property
    def paramone(self):
        return self._paramone

    @paramone.setter
    def paramone(self, value):
        self._paramone = value
    @property
    def paramtwo(self):
        return self._paramtwo

    @paramtwo.setter
    def paramtwo(self, value):
        self._paramtwo = value


    def to_alipay_dict(self):
        params = dict()
        if self.paramone:
            if hasattr(self.paramone, 'to_alipay_dict'):
                params['paramone'] = self.paramone.to_alipay_dict()
            else:
                params['paramone'] = self.paramone
        if self.paramtwo:
            if hasattr(self.paramtwo, 'to_alipay_dict'):
                params['paramtwo'] = self.paramtwo.to_alipay_dict()
            else:
                params['paramtwo'] = self.paramtwo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSmsgDataSetModel()
        if 'paramone' in d:
            o.paramone = d['paramone']
        if 'paramtwo' in d:
            o.paramtwo = d['paramtwo']
        return o


