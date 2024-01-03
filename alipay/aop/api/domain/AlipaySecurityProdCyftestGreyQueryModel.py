#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdCyftestGreyQueryModel(object):

    def __init__(self):
        self._testone = None

    @property
    def testone(self):
        return self._testone

    @testone.setter
    def testone(self, value):
        self._testone = value


    def to_alipay_dict(self):
        params = dict()
        if self.testone:
            if hasattr(self.testone, 'to_alipay_dict'):
                params['testone'] = self.testone.to_alipay_dict()
            else:
                params['testone'] = self.testone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdCyftestGreyQueryModel()
        if 'testone' in d:
            o.testone = d['testone']
        return o


