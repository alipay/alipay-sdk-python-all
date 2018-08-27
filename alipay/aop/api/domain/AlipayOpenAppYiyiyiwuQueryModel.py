#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppYiyiyiwuQueryModel(object):

    def __init__(self):
        self._rucan = None

    @property
    def rucan(self):
        return self._rucan

    @rucan.setter
    def rucan(self, value):
        self._rucan = value


    def to_alipay_dict(self):
        params = dict()
        if self.rucan:
            if hasattr(self.rucan, 'to_alipay_dict'):
                params['rucan'] = self.rucan.to_alipay_dict()
            else:
                params['rucan'] = self.rucan
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppYiyiyiwuQueryModel()
        if 'rucan' in d:
            o.rucan = d['rucan']
        return o


