#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SkuUpdateFailInfoDTO(object):

    def __init__(self):
        self._desc = None
        self._sku_code = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def sku_code(self):
        return self._sku_code

    @sku_code.setter
    def sku_code(self, value):
        self._sku_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.sku_code:
            if hasattr(self.sku_code, 'to_alipay_dict'):
                params['sku_code'] = self.sku_code.to_alipay_dict()
            else:
                params['sku_code'] = self.sku_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SkuUpdateFailInfoDTO()
        if 'desc' in d:
            o.desc = d['desc']
        if 'sku_code' in d:
            o.sku_code = d['sku_code']
        return o


