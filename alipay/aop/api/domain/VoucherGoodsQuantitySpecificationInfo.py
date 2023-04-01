#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherGoodsQuantitySpecificationInfo(object):

    def __init__(self):
        self._directional_type = None
        self._specification_quantity = None
        self._specification_unit = None

    @property
    def directional_type(self):
        return self._directional_type

    @directional_type.setter
    def directional_type(self, value):
        self._directional_type = value
    @property
    def specification_quantity(self):
        return self._specification_quantity

    @specification_quantity.setter
    def specification_quantity(self, value):
        self._specification_quantity = value
    @property
    def specification_unit(self):
        return self._specification_unit

    @specification_unit.setter
    def specification_unit(self, value):
        self._specification_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.directional_type:
            if hasattr(self.directional_type, 'to_alipay_dict'):
                params['directional_type'] = self.directional_type.to_alipay_dict()
            else:
                params['directional_type'] = self.directional_type
        if self.specification_quantity:
            if hasattr(self.specification_quantity, 'to_alipay_dict'):
                params['specification_quantity'] = self.specification_quantity.to_alipay_dict()
            else:
                params['specification_quantity'] = self.specification_quantity
        if self.specification_unit:
            if hasattr(self.specification_unit, 'to_alipay_dict'):
                params['specification_unit'] = self.specification_unit.to_alipay_dict()
            else:
                params['specification_unit'] = self.specification_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherGoodsQuantitySpecificationInfo()
        if 'directional_type' in d:
            o.directional_type = d['directional_type']
        if 'specification_quantity' in d:
            o.specification_quantity = d['specification_quantity']
        if 'specification_unit' in d:
            o.specification_unit = d['specification_unit']
        return o


