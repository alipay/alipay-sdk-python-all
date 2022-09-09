#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingMiniapptestQueryModel(object):

    def __init__(self):
        self._xxxx = None

    @property
    def xxxx(self):
        return self._xxxx

    @xxxx.setter
    def xxxx(self, value):
        self._xxxx = value


    def to_alipay_dict(self):
        params = dict()
        if self.xxxx:
            if hasattr(self.xxxx, 'to_alipay_dict'):
                params['xxxx'] = self.xxxx.to_alipay_dict()
            else:
                params['xxxx'] = self.xxxx
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingMiniapptestQueryModel()
        if 'xxxx' in d:
            o.xxxx = d['xxxx']
        return o


