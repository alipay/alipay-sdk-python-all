#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppSmgMsgSendModel(object):

    def __init__(self):
        self._numberone = None
        self._numbertowe = None

    @property
    def numberone(self):
        return self._numberone

    @numberone.setter
    def numberone(self, value):
        self._numberone = value
    @property
    def numbertowe(self):
        return self._numbertowe

    @numbertowe.setter
    def numbertowe(self, value):
        self._numbertowe = value


    def to_alipay_dict(self):
        params = dict()
        if self.numberone:
            if hasattr(self.numberone, 'to_alipay_dict'):
                params['numberone'] = self.numberone.to_alipay_dict()
            else:
                params['numberone'] = self.numberone
        if self.numbertowe:
            if hasattr(self.numbertowe, 'to_alipay_dict'):
                params['numbertowe'] = self.numbertowe.to_alipay_dict()
            else:
                params['numbertowe'] = self.numbertowe
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppSmgMsgSendModel()
        if 'numberone' in d:
            o.numberone = d['numberone']
        if 'numbertowe' in d:
            o.numbertowe = d['numbertowe']
        return o


