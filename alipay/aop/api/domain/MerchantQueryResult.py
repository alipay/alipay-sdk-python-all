#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantQueryResult(object):

    def __init__(self):
        self._alias_name = None
        self._cert_no = None
        self._city = None
        self._detail_address = None
        self._distinct = None
        self._mcc_code = None
        self._merchant_type = None
        self._name = None
        self._province = None

    @property
    def alias_name(self):
        return self._alias_name

    @alias_name.setter
    def alias_name(self, value):
        self._alias_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def detail_address(self):
        return self._detail_address

    @detail_address.setter
    def detail_address(self, value):
        self._detail_address = value
    @property
    def distinct(self):
        return self._distinct

    @distinct.setter
    def distinct(self, value):
        self._distinct = value
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
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
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value


    def to_alipay_dict(self):
        params = dict()
        if self.alias_name:
            if hasattr(self.alias_name, 'to_alipay_dict'):
                params['alias_name'] = self.alias_name.to_alipay_dict()
            else:
                params['alias_name'] = self.alias_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.detail_address:
            if hasattr(self.detail_address, 'to_alipay_dict'):
                params['detail_address'] = self.detail_address.to_alipay_dict()
            else:
                params['detail_address'] = self.detail_address
        if self.distinct:
            if hasattr(self.distinct, 'to_alipay_dict'):
                params['distinct'] = self.distinct.to_alipay_dict()
            else:
                params['distinct'] = self.distinct
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = self.mcc_code.to_alipay_dict()
            else:
                params['mcc_code'] = self.mcc_code
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
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantQueryResult()
        if 'alias_name' in d:
            o.alias_name = d['alias_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'city' in d:
            o.city = d['city']
        if 'detail_address' in d:
            o.detail_address = d['detail_address']
        if 'distinct' in d:
            o.distinct = d['distinct']
        if 'mcc_code' in d:
            o.mcc_code = d['mcc_code']
        if 'merchant_type' in d:
            o.merchant_type = d['merchant_type']
        if 'name' in d:
            o.name = d['name']
        if 'province' in d:
            o.province = d['province']
        return o


