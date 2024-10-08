#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SkuPriceDeatail import SkuPriceDeatail


class AlipayCommerceMedicalItemPriceModifyModel(object):

    def __init__(self):
        self._skus_data = None
        self._store_code = None

    @property
    def skus_data(self):
        return self._skus_data

    @skus_data.setter
    def skus_data(self, value):
        if isinstance(value, list):
            self._skus_data = list()
            for i in value:
                if isinstance(i, SkuPriceDeatail):
                    self._skus_data.append(i)
                else:
                    self._skus_data.append(SkuPriceDeatail.from_alipay_dict(i))
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.skus_data:
            if isinstance(self.skus_data, list):
                for i in range(0, len(self.skus_data)):
                    element = self.skus_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.skus_data[i] = element.to_alipay_dict()
            if hasattr(self.skus_data, 'to_alipay_dict'):
                params['skus_data'] = self.skus_data.to_alipay_dict()
            else:
                params['skus_data'] = self.skus_data
        if self.store_code:
            if hasattr(self.store_code, 'to_alipay_dict'):
                params['store_code'] = self.store_code.to_alipay_dict()
            else:
                params['store_code'] = self.store_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalItemPriceModifyModel()
        if 'skus_data' in d:
            o.skus_data = d['skus_data']
        if 'store_code' in d:
            o.store_code = d['store_code']
        return o


