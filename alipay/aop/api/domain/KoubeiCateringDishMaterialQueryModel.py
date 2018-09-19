#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringDishMaterialQueryModel(object):

    def __init__(self):
        self._material_id = None
        self._merchant_id = None

    @property
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, value):
        self._material_id = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.material_id:
            if hasattr(self.material_id, 'to_alipay_dict'):
                params['material_id'] = self.material_id.to_alipay_dict()
            else:
                params['material_id'] = self.material_id
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishMaterialQueryModel()
        if 'material_id' in d:
            o.material_id = d['material_id']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        return o


