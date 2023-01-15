#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechAiCvRsResultGetModel(object):

    def __init__(self):
        self._geo = None

    @property
    def geo(self):
        return self._geo

    @geo.setter
    def geo(self, value):
        self._geo = value


    def to_alipay_dict(self):
        params = dict()
        if self.geo:
            if hasattr(self.geo, 'to_alipay_dict'):
                params['geo'] = self.geo.to_alipay_dict()
            else:
                params['geo'] = self.geo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechAiCvRsResultGetModel()
        if 'geo' in d:
            o.geo = d['geo']
        return o


