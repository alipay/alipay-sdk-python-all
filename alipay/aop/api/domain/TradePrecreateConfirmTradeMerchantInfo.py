#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradePrecreateConfirmTradeMerchantInfo(object):

    def __init__(self):
        self._city_code = None
        self._city_name_sc = None
        self._id = None
        self._mcc = None
        self._merchant_type = None
        self._name = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name_sc(self):
        return self._city_name_sc

    @city_name_sc.setter
    def city_name_sc(self, value):
        self._city_name_sc = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def mcc(self):
        return self._mcc

    @mcc.setter
    def mcc(self, value):
        self._mcc = value
    @property
    def merchant_type(self):
        return self._merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self._merchant_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name_sc:
            if hasattr(self.city_name_sc, 'to_alipay_dict'):
                params['city_name_sc'] = self.city_name_sc.to_alipay_dict()
            else:
                params['city_name_sc'] = self.city_name_sc
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.mcc:
            if hasattr(self.mcc, 'to_alipay_dict'):
                params['mcc'] = self.mcc.to_alipay_dict()
            else:
                params['mcc'] = self.mcc
        if self.merchant_type:
            if hasattr(self.merchant_type, 'to_alipay_dict'):
                params['merchant_type'] = self.merchant_type.to_alipay_dict()
            else:
                params['merchant_type'] = self.merchant_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradePrecreateConfirmTradeMerchantInfo()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name_sc' in d:
            o.city_name_sc = d['city_name_sc']
        if 'id' in d:
            o.id = d['id']
        if 'mcc' in d:
            o.mcc = d['mcc']
        if 'merchant_type' in d:
            o.merchant_type = d['merchant_type']
        if 'name' in d:
            o.name = d['name']
        return o


