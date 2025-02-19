#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SkuCodeUpdateFailInfoDTO(object):

    def __init__(self):
        self._desc = None
        self._source_sku_code = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def source_sku_code(self):
        return self._source_sku_code

    @source_sku_code.setter
    def source_sku_code(self, value):
        self._source_sku_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.source_sku_code:
            if hasattr(self.source_sku_code, 'to_alipay_dict'):
                params['source_sku_code'] = self.source_sku_code.to_alipay_dict()
            else:
                params['source_sku_code'] = self.source_sku_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SkuCodeUpdateFailInfoDTO()
        if 'desc' in d:
            o.desc = d['desc']
        if 'source_sku_code' in d:
            o.source_sku_code = d['source_sku_code']
        return o


