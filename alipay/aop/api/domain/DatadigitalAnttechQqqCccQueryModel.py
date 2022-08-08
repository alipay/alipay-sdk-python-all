#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAnttechQqqCccQueryModel(object):

    def __init__(self):
        self._province_code = None
        self._re = None

    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def re(self):
        return self._re

    @re.setter
    def re(self, value):
        self._re = value


    def to_alipay_dict(self):
        params = dict()
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.re:
            if hasattr(self.re, 'to_alipay_dict'):
                params['re'] = self.re.to_alipay_dict()
            else:
                params['re'] = self.re
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAnttechQqqCccQueryModel()
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 're' in d:
            o.re = d['re']
        return o


