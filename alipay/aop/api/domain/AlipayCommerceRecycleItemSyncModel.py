#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleDeliveryConfigDTO import RecycleDeliveryConfigDTO
from alipay.aop.api.domain.RecycleSkuDTO import RecycleSkuDTO


class AlipayCommerceRecycleItemSyncModel(object):

    def __init__(self):
        self._delivery_configs = None
        self._out_biz_id = None
        self._product_code = None
        self._skus = None

    @property
    def delivery_configs(self):
        return self._delivery_configs

    @delivery_configs.setter
    def delivery_configs(self, value):
        if isinstance(value, list):
            self._delivery_configs = list()
            for i in value:
                if isinstance(i, RecycleDeliveryConfigDTO):
                    self._delivery_configs.append(i)
                else:
                    self._delivery_configs.append(RecycleDeliveryConfigDTO.from_alipay_dict(i))
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_configs:
            if isinstance(self.delivery_configs, list):
                for i in range(0, len(self.delivery_configs)):
                    element = self.delivery_configs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_configs[i] = element.to_alipay_dict()
            if hasattr(self.delivery_configs, 'to_alipay_dict'):
                params['delivery_configs'] = self.delivery_configs.to_alipay_dict()
            else:
                params['delivery_configs'] = self.delivery_configs
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRecycleItemSyncModel()
        if 'delivery_configs' in d:
            o.delivery_configs = d['delivery_configs']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'skus' in d:
            o.skus = d['skus']
        return o


