#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalMedicineShopQueryModel(object):

    def __init__(self):
        self._out_store_id = None
        self._shop_id = None

    @property
    def out_store_id(self):
        return self._out_store_id

    @out_store_id.setter
    def out_store_id(self, value):
        self._out_store_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_store_id:
            if hasattr(self.out_store_id, 'to_alipay_dict'):
                params['out_store_id'] = self.out_store_id.to_alipay_dict()
            else:
                params['out_store_id'] = self.out_store_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMedicineShopQueryModel()
        if 'out_store_id' in d:
            o.out_store_id = d['out_store_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


