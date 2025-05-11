#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalSkuSyncModel(object):

    def __init__(self):
        self._sku_info = None
        self._sku_init = None

    @property
    def sku_info(self):
        return self._sku_info

    @sku_info.setter
    def sku_info(self, value):
        self._sku_info = value
    @property
    def sku_init(self):
        return self._sku_init

    @sku_init.setter
    def sku_init(self, value):
        self._sku_init = value


    def to_alipay_dict(self):
        params = dict()
        if self.sku_info:
            if hasattr(self.sku_info, 'to_alipay_dict'):
                params['sku_info'] = self.sku_info.to_alipay_dict()
            else:
                params['sku_info'] = self.sku_info
        if self.sku_init:
            if hasattr(self.sku_init, 'to_alipay_dict'):
                params['sku_init'] = self.sku_init.to_alipay_dict()
            else:
                params['sku_init'] = self.sku_init
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalSkuSyncModel()
        if 'sku_info' in d:
            o.sku_info = d['sku_info']
        if 'sku_init' in d:
            o.sku_init = d['sku_init']
        return o


