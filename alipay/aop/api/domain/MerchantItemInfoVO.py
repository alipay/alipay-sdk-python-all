#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantSkuInfoVO import MerchantSkuInfoVO


class MerchantItemInfoVO(object):

    def __init__(self):
        self._out_item_id = None
        self._skus = None

    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def skus(self):
        return self._skus

    @skus.setter
    def skus(self, value):
        if isinstance(value, list):
            self._skus = list()
            for i in value:
                if isinstance(i, MerchantSkuInfoVO):
                    self._skus.append(i)
                else:
                    self._skus.append(MerchantSkuInfoVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantItemInfoVO()
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'skus' in d:
            o.skus = d['skus']
        return o


