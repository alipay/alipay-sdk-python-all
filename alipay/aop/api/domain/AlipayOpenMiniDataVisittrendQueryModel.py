#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniDataVisittrendQueryModel(object):

    def __init__(self):
        self._time_unit = None

    @property
    def time_unit(self):
        return self._time_unit

    @time_unit.setter
    def time_unit(self, value):
        self._time_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.time_unit:
            if hasattr(self.time_unit, 'to_alipay_dict'):
                params['time_unit'] = self.time_unit.to_alipay_dict()
            else:
                params['time_unit'] = self.time_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniDataVisittrendQueryModel()
        if 'time_unit' in d:
            o.time_unit = d['time_unit']
        return o


