#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateMerchantDTO(object):

    def __init__(self):
        self._brand_id = None
        self._brand_id_source = None
        self._brand_name = None
        self._life_code = None
        self._merchant_name = None
        self._merchant_tel = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def brand_id_source(self):
        return self._brand_id_source

    @brand_id_source.setter
    def brand_id_source(self, value):
        self._brand_id_source = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def life_code(self):
        return self._life_code

    @life_code.setter
    def life_code(self, value):
        self._life_code = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_tel(self):
        return self._merchant_tel

    @merchant_tel.setter
    def merchant_tel(self, value):
        self._merchant_tel = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.brand_id_source:
            if hasattr(self.brand_id_source, 'to_alipay_dict'):
                params['brand_id_source'] = self.brand_id_source.to_alipay_dict()
            else:
                params['brand_id_source'] = self.brand_id_source
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.life_code:
            if hasattr(self.life_code, 'to_alipay_dict'):
                params['life_code'] = self.life_code.to_alipay_dict()
            else:
                params['life_code'] = self.life_code
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.merchant_tel:
            if hasattr(self.merchant_tel, 'to_alipay_dict'):
                params['merchant_tel'] = self.merchant_tel.to_alipay_dict()
            else:
                params['merchant_tel'] = self.merchant_tel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateMerchantDTO()
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_id_source' in d:
            o.brand_id_source = d['brand_id_source']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'life_code' in d:
            o.life_code = d['life_code']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_tel' in d:
            o.merchant_tel = d['merchant_tel']
        return o


