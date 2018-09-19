#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class XXXXsdasdasd(object):

    def __init__(self):
        self._wasfdasdf = None

    @property
    def wasfdasdf(self):
        return self._wasfdasdf

    @wasfdasdf.setter
    def wasfdasdf(self, value):
        self._wasfdasdf = value


    def to_alipay_dict(self):
        params = dict()
        if self.wasfdasdf:
            if hasattr(self.wasfdasdf, 'to_alipay_dict'):
                params['wasfdasdf'] = self.wasfdasdf.to_alipay_dict()
            else:
                params['wasfdasdf'] = self.wasfdasdf
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XXXXsdasdasd()
        if 'wasfdasdf' in d:
            o.wasfdasdf = d['wasfdasdf']
        return o


