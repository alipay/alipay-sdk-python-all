#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndustryItemSkuSyncResultDTO(object):

    def __init__(self):
        self._platform_sku_id = None
        self._sku_id = None

    @property
    def platform_sku_id(self):
        return self._platform_sku_id

    @platform_sku_id.setter
    def platform_sku_id(self, value):
        self._platform_sku_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.platform_sku_id:
            if hasattr(self.platform_sku_id, 'to_alipay_dict'):
                params['platform_sku_id'] = self.platform_sku_id.to_alipay_dict()
            else:
                params['platform_sku_id'] = self.platform_sku_id
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryItemSkuSyncResultDTO()
        if 'platform_sku_id' in d:
            o.platform_sku_id = d['platform_sku_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


