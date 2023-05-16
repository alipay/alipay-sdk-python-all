#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcShop import EcShop


class AlipayCommerceEcShopCreateModel(object):

    def __init__(self):
        self._operator_id = None
        self._service_product_id = None
        self._shop_info = None

    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def service_product_id(self):
        return self._service_product_id

    @service_product_id.setter
    def service_product_id(self, value):
        self._service_product_id = value
    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        if isinstance(value, EcShop):
            self._shop_info = value
        else:
            self._shop_info = EcShop.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.service_product_id:
            if hasattr(self.service_product_id, 'to_alipay_dict'):
                params['service_product_id'] = self.service_product_id.to_alipay_dict()
            else:
                params['service_product_id'] = self.service_product_id
        if self.shop_info:
            if hasattr(self.shop_info, 'to_alipay_dict'):
                params['shop_info'] = self.shop_info.to_alipay_dict()
            else:
                params['shop_info'] = self.shop_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcShopCreateModel()
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'service_product_id' in d:
            o.service_product_id = d['service_product_id']
        if 'shop_info' in d:
            o.shop_info = d['shop_info']
        return o


