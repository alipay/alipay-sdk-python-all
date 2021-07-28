#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppDedfDdQueryModel(object):

    def __init__(self):
        self._zyde = None

    @property
    def zyde(self):
        return self._zyde

    @zyde.setter
    def zyde(self, value):
        self._zyde = value


    def to_alipay_dict(self):
        params = dict()
        if self.zyde:
            if hasattr(self.zyde, 'to_alipay_dict'):
                params['zyde'] = self.zyde.to_alipay_dict()
            else:
                params['zyde'] = self.zyde
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppDedfDdQueryModel()
        if 'zyde' in d:
            o.zyde = d['zyde']
        return o


