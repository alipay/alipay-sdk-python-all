#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppYufanlingsanyaowuYufalingsanyaowuQueryModel(object):

    def __init__(self):
        self._province_code = None

    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        if isinstance(value, list):
            self._province_code = list()
            for i in value:
                self._province_code.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.province_code:
            if isinstance(self.province_code, list):
                for i in range(0, len(self.province_code)):
                    element = self.province_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.province_code[i] = element.to_alipay_dict()
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppYufanlingsanyaowuYufalingsanyaowuQueryModel()
        if 'province_code' in d:
            o.province_code = d['province_code']
        return o


