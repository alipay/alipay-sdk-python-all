#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoLogisticsExpressPriceModifyModel(object):

    def __init__(self):
        self._area_type = None
        self._extra_weight_price = None
        self._extra_weight_unit = None
        self._from_code = None
        self._logis_merch_code = None
        self._preset_weight = None
        self._preset_weight_price = None
        self._product_type_code = None
        self._to_code = None

    @property
    def area_type(self):
        return self._area_type

    @area_type.setter
    def area_type(self, value):
        self._area_type = value
    @property
    def extra_weight_price(self):
        return self._extra_weight_price

    @extra_weight_price.setter
    def extra_weight_price(self, value):
        self._extra_weight_price = value
    @property
    def extra_weight_unit(self):
        return self._extra_weight_unit

    @extra_weight_unit.setter
    def extra_weight_unit(self, value):
        self._extra_weight_unit = value
    @property
    def from_code(self):
        return self._from_code

    @from_code.setter
    def from_code(self, value):
        self._from_code = value
    @property
    def logis_merch_code(self):
        return self._logis_merch_code

    @logis_merch_code.setter
    def logis_merch_code(self, value):
        self._logis_merch_code = value
    @property
    def preset_weight(self):
        return self._preset_weight

    @preset_weight.setter
    def preset_weight(self, value):
        self._preset_weight = value
    @property
    def preset_weight_price(self):
        return self._preset_weight_price

    @preset_weight_price.setter
    def preset_weight_price(self, value):
        self._preset_weight_price = value
    @property
    def product_type_code(self):
        return self._product_type_code

    @product_type_code.setter
    def product_type_code(self, value):
        self._product_type_code = value
    @property
    def to_code(self):
        return self._to_code

    @to_code.setter
    def to_code(self, value):
        self._to_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_type:
            if hasattr(self.area_type, 'to_alipay_dict'):
                params['area_type'] = self.area_type.to_alipay_dict()
            else:
                params['area_type'] = self.area_type
        if self.extra_weight_price:
            if hasattr(self.extra_weight_price, 'to_alipay_dict'):
                params['extra_weight_price'] = self.extra_weight_price.to_alipay_dict()
            else:
                params['extra_weight_price'] = self.extra_weight_price
        if self.extra_weight_unit:
            if hasattr(self.extra_weight_unit, 'to_alipay_dict'):
                params['extra_weight_unit'] = self.extra_weight_unit.to_alipay_dict()
            else:
                params['extra_weight_unit'] = self.extra_weight_unit
        if self.from_code:
            if hasattr(self.from_code, 'to_alipay_dict'):
                params['from_code'] = self.from_code.to_alipay_dict()
            else:
                params['from_code'] = self.from_code
        if self.logis_merch_code:
            if hasattr(self.logis_merch_code, 'to_alipay_dict'):
                params['logis_merch_code'] = self.logis_merch_code.to_alipay_dict()
            else:
                params['logis_merch_code'] = self.logis_merch_code
        if self.preset_weight:
            if hasattr(self.preset_weight, 'to_alipay_dict'):
                params['preset_weight'] = self.preset_weight.to_alipay_dict()
            else:
                params['preset_weight'] = self.preset_weight
        if self.preset_weight_price:
            if hasattr(self.preset_weight_price, 'to_alipay_dict'):
                params['preset_weight_price'] = self.preset_weight_price.to_alipay_dict()
            else:
                params['preset_weight_price'] = self.preset_weight_price
        if self.product_type_code:
            if hasattr(self.product_type_code, 'to_alipay_dict'):
                params['product_type_code'] = self.product_type_code.to_alipay_dict()
            else:
                params['product_type_code'] = self.product_type_code
        if self.to_code:
            if hasattr(self.to_code, 'to_alipay_dict'):
                params['to_code'] = self.to_code.to_alipay_dict()
            else:
                params['to_code'] = self.to_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoLogisticsExpressPriceModifyModel()
        if 'area_type' in d:
            o.area_type = d['area_type']
        if 'extra_weight_price' in d:
            o.extra_weight_price = d['extra_weight_price']
        if 'extra_weight_unit' in d:
            o.extra_weight_unit = d['extra_weight_unit']
        if 'from_code' in d:
            o.from_code = d['from_code']
        if 'logis_merch_code' in d:
            o.logis_merch_code = d['logis_merch_code']
        if 'preset_weight' in d:
            o.preset_weight = d['preset_weight']
        if 'preset_weight_price' in d:
            o.preset_weight_price = d['preset_weight_price']
        if 'product_type_code' in d:
            o.product_type_code = d['product_type_code']
        if 'to_code' in d:
            o.to_code = d['to_code']
        return o


