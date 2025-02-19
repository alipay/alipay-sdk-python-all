#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleSkuDTO import RecycleSkuDTO


class RecycleItemDTO(object):

    def __init__(self):
        self._product_code = None
        self._skus = None
        self._snapshot_id = None

    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def skus(self):
        return self._skus

    @skus.setter
    def skus(self, value):
        if isinstance(value, list):
            self._skus = list()
            for i in value:
                if isinstance(i, RecycleSkuDTO):
                    self._skus.append(i)
                else:
                    self._skus.append(RecycleSkuDTO.from_alipay_dict(i))
    @property
    def snapshot_id(self):
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, value):
        self._snapshot_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.skus:
            if isinstance(self.skus, list):
                for i in range(0, len(self.skus)):
                    element = self.skus[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.skus[i] = element.to_alipay_dict()
            if hasattr(self.skus, 'to_alipay_dict'):
                params['skus'] = self.skus.to_alipay_dict()
            else:
                params['skus'] = self.skus
        if self.snapshot_id:
            if hasattr(self.snapshot_id, 'to_alipay_dict'):
                params['snapshot_id'] = self.snapshot_id.to_alipay_dict()
            else:
                params['snapshot_id'] = self.snapshot_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleItemDTO()
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'skus' in d:
            o.skus = d['skus']
        if 'snapshot_id' in d:
            o.snapshot_id = d['snapshot_id']
        return o


