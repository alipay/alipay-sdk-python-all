#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbAdvertSubjectVoucher(object):

    def __init__(self):
        self._brand_name = None
        self._city_ids = None
        self._merchant_name = None
        self._purchase_mode = None
        self._voucher_id = None
        self._voucher_name = None
        self._voucher_type = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def city_ids(self):
        return self._city_ids

    @city_ids.setter
    def city_ids(self, value):
        if isinstance(value, list):
            self._city_ids = list()
            for i in value:
                self._city_ids.append(i)
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def purchase_mode(self):
        return self._purchase_mode

    @purchase_mode.setter
    def purchase_mode(self, value):
        self._purchase_mode = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.city_ids:
            if isinstance(self.city_ids, list):
                for i in range(0, len(self.city_ids)):
                    element = self.city_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.city_ids[i] = element.to_alipay_dict()
            if hasattr(self.city_ids, 'to_alipay_dict'):
                params['city_ids'] = self.city_ids.to_alipay_dict()
            else:
                params['city_ids'] = self.city_ids
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.purchase_mode:
            if hasattr(self.purchase_mode, 'to_alipay_dict'):
                params['purchase_mode'] = self.purchase_mode.to_alipay_dict()
            else:
                params['purchase_mode'] = self.purchase_mode
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertSubjectVoucher()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'city_ids' in d:
            o.city_ids = d['city_ids']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'purchase_mode' in d:
            o.purchase_mode = d['purchase_mode']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


