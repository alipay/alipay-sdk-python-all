#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceSchemaapiRainyfirstQueryModel(object):

    def __init__(self):
        self._string_tc_01 = None

    @property
    def string_tc_01(self):
        return self._string_tc_01

    @string_tc_01.setter
    def string_tc_01(self, value):
        self._string_tc_01 = value


    def to_alipay_dict(self):
        params = dict()
        if self.string_tc_01:
            if hasattr(self.string_tc_01, 'to_alipay_dict'):
                params['string_tc_01'] = self.string_tc_01.to_alipay_dict()
            else:
                params['string_tc_01'] = self.string_tc_01
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceSchemaapiRainyfirstQueryModel()
        if 'string_tc_01' in d:
            o.string_tc_01 = d['string_tc_01']
        return o


