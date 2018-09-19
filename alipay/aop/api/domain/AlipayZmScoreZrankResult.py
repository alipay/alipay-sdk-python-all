#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayZmScoreZrankResult(object):

    def __init__(self):
        self._zrank = None

    @property
    def zrank(self):
        return self._zrank

    @zrank.setter
    def zrank(self, value):
        self._zrank = value


    def to_alipay_dict(self):
        params = dict()
        if self.zrank:
            if hasattr(self.zrank, 'to_alipay_dict'):
                params['zrank'] = self.zrank.to_alipay_dict()
            else:
                params['zrank'] = self.zrank
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayZmScoreZrankResult()
        if 'zrank' in d:
            o.zrank = d['zrank']
        return o


