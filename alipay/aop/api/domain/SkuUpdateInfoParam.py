#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InquiryInfoParam import InquiryInfoParam
from alipay.aop.api.domain.InspectInfoParam import InspectInfoParam


class SkuUpdateInfoParam(object):

    def __init__(self):
        self._external_key = None
        self._inquiry_info = None
        self._inspect_info = None
        self._name = None
        self._shelf_code = None
        self._show_to_customer = None
        self._sku_code = None
        self._upc = None
        self._volume_high = None
        self._volume_length = None
        self._volume_width = None
        self._weight = None
        self._weight_unit = None

    @property
    def external_key(self):
        return self._external_key

    @external_key.setter
    def external_key(self, value):
        self._external_key = value
    @property
    def inquiry_info(self):
        return self._inquiry_info

    @inquiry_info.setter
    def inquiry_info(self, value):
        if isinstance(value, InquiryInfoParam):
            self._inquiry_info = value
        else:
            self._inquiry_info = InquiryInfoParam.from_alipay_dict(value)
    @property
    def inspect_info(self):
        return self._inspect_info

    @inspect_info.setter
    def inspect_info(self, value):
        if isinstance(value, InspectInfoParam):
            self._inspect_info = value
        else:
            self._inspect_info = InspectInfoParam.from_alipay_dict(value)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def shelf_code(self):
        return self._shelf_code

    @shelf_code.setter
    def shelf_code(self, value):
        self._shelf_code = value
    @property
    def show_to_customer(self):
        return self._show_to_customer

    @show_to_customer.setter
    def show_to_customer(self, value):
        self._show_to_customer = value
    @property
    def sku_code(self):
        return self._sku_code

    @sku_code.setter
    def sku_code(self, value):
        self._sku_code = value
    @property
    def upc(self):
        return self._upc

    @upc.setter
    def upc(self, value):
        self._upc = value
    @property
    def volume_high(self):
        return self._volume_high

    @volume_high.setter
    def volume_high(self, value):
        self._volume_high = value
    @property
    def volume_length(self):
        return self._volume_length

    @volume_length.setter
    def volume_length(self, value):
        self._volume_length = value
    @property
    def volume_width(self):
        return self._volume_width

    @volume_width.setter
    def volume_width(self, value):
        self._volume_width = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value
    @property
    def weight_unit(self):
        return self._weight_unit

    @weight_unit.setter
    def weight_unit(self, value):
        self._weight_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_key:
            if hasattr(self.external_key, 'to_alipay_dict'):
                params['external_key'] = self.external_key.to_alipay_dict()
            else:
                params['external_key'] = self.external_key
        if self.inquiry_info:
            if hasattr(self.inquiry_info, 'to_alipay_dict'):
                params['inquiry_info'] = self.inquiry_info.to_alipay_dict()
            else:
                params['inquiry_info'] = self.inquiry_info
        if self.inspect_info:
            if hasattr(self.inspect_info, 'to_alipay_dict'):
                params['inspect_info'] = self.inspect_info.to_alipay_dict()
            else:
                params['inspect_info'] = self.inspect_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.shelf_code:
            if hasattr(self.shelf_code, 'to_alipay_dict'):
                params['shelf_code'] = self.shelf_code.to_alipay_dict()
            else:
                params['shelf_code'] = self.shelf_code
        if self.show_to_customer:
            if hasattr(self.show_to_customer, 'to_alipay_dict'):
                params['show_to_customer'] = self.show_to_customer.to_alipay_dict()
            else:
                params['show_to_customer'] = self.show_to_customer
        if self.sku_code:
            if hasattr(self.sku_code, 'to_alipay_dict'):
                params['sku_code'] = self.sku_code.to_alipay_dict()
            else:
                params['sku_code'] = self.sku_code
        if self.upc:
            if hasattr(self.upc, 'to_alipay_dict'):
                params['upc'] = self.upc.to_alipay_dict()
            else:
                params['upc'] = self.upc
        if self.volume_high:
            if hasattr(self.volume_high, 'to_alipay_dict'):
                params['volume_high'] = self.volume_high.to_alipay_dict()
            else:
                params['volume_high'] = self.volume_high
        if self.volume_length:
            if hasattr(self.volume_length, 'to_alipay_dict'):
                params['volume_length'] = self.volume_length.to_alipay_dict()
            else:
                params['volume_length'] = self.volume_length
        if self.volume_width:
            if hasattr(self.volume_width, 'to_alipay_dict'):
                params['volume_width'] = self.volume_width.to_alipay_dict()
            else:
                params['volume_width'] = self.volume_width
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        if self.weight_unit:
            if hasattr(self.weight_unit, 'to_alipay_dict'):
                params['weight_unit'] = self.weight_unit.to_alipay_dict()
            else:
                params['weight_unit'] = self.weight_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SkuUpdateInfoParam()
        if 'external_key' in d:
            o.external_key = d['external_key']
        if 'inquiry_info' in d:
            o.inquiry_info = d['inquiry_info']
        if 'inspect_info' in d:
            o.inspect_info = d['inspect_info']
        if 'name' in d:
            o.name = d['name']
        if 'shelf_code' in d:
            o.shelf_code = d['shelf_code']
        if 'show_to_customer' in d:
            o.show_to_customer = d['show_to_customer']
        if 'sku_code' in d:
            o.sku_code = d['sku_code']
        if 'upc' in d:
            o.upc = d['upc']
        if 'volume_high' in d:
            o.volume_high = d['volume_high']
        if 'volume_length' in d:
            o.volume_length = d['volume_length']
        if 'volume_width' in d:
            o.volume_width = d['volume_width']
        if 'weight' in d:
            o.weight = d['weight']
        if 'weight_unit' in d:
            o.weight_unit = d['weight_unit']
        return o


