#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SkuCodeMappingParam(object):

    def __init__(self):
        self._source_sku_code = None
        self._target_sku_code = None

    @property
    def source_sku_code(self):
        return self._source_sku_code

    @source_sku_code.setter
    def source_sku_code(self, value):
        self._source_sku_code = value
    @property
    def target_sku_code(self):
        return self._target_sku_code

    @target_sku_code.setter
    def target_sku_code(self, value):
        self._target_sku_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.source_sku_code:
            if hasattr(self.source_sku_code, 'to_alipay_dict'):
                params['source_sku_code'] = self.source_sku_code.to_alipay_dict()
            else:
                params['source_sku_code'] = self.source_sku_code
        if self.target_sku_code:
            if hasattr(self.target_sku_code, 'to_alipay_dict'):
                params['target_sku_code'] = self.target_sku_code.to_alipay_dict()
            else:
                params['target_sku_code'] = self.target_sku_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SkuCodeMappingParam()
        if 'source_sku_code' in d:
            o.source_sku_code = d['source_sku_code']
        if 'target_sku_code' in d:
            o.target_sku_code = d['target_sku_code']
        return o


