#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingToolXuanyitestQueryModel(object):

    def __init__(self):
        self._ssss = None
        self._xxx = None

    @property
    def ssss(self):
        return self._ssss

    @ssss.setter
    def ssss(self, value):
        self._ssss = value
    @property
    def xxx(self):
        return self._xxx

    @xxx.setter
    def xxx(self, value):
        self._xxx = value


    def to_alipay_dict(self):
        params = dict()
        if self.ssss:
            if hasattr(self.ssss, 'to_alipay_dict'):
                params['ssss'] = self.ssss.to_alipay_dict()
            else:
                params['ssss'] = self.ssss
        if self.xxx:
            if hasattr(self.xxx, 'to_alipay_dict'):
                params['xxx'] = self.xxx.to_alipay_dict()
            else:
                params['xxx'] = self.xxx
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingToolXuanyitestQueryModel()
        if 'ssss' in d:
            o.ssss = d['ssss']
        if 'xxx' in d:
            o.xxx = d['xxx']
        return o


