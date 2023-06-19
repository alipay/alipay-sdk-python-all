#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainDefinFwhSignApplyModel(object):

    def __init__(self):
        self._expiry_period = None
        self._merchant_id_number = None
        self._merchant_id_type = None
        self._merchant_name = None
        self._outer_logon_id = None
        self._product_agrt_code = None
        self._request_no = None
        self._sign_link_expiry_period = None

    @property
    def expiry_period(self):
        return self._expiry_period

    @expiry_period.setter
    def expiry_period(self, value):
        self._expiry_period = value
    @property
    def merchant_id_number(self):
        return self._merchant_id_number

    @merchant_id_number.setter
    def merchant_id_number(self, value):
        self._merchant_id_number = value
    @property
    def merchant_id_type(self):
        return self._merchant_id_type

    @merchant_id_type.setter
    def merchant_id_type(self, value):
        self._merchant_id_type = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def outer_logon_id(self):
        return self._outer_logon_id

    @outer_logon_id.setter
    def outer_logon_id(self, value):
        self._outer_logon_id = value
    @property
    def product_agrt_code(self):
        return self._product_agrt_code

    @product_agrt_code.setter
    def product_agrt_code(self, value):
        self._product_agrt_code = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def sign_link_expiry_period(self):
        return self._sign_link_expiry_period

    @sign_link_expiry_period.setter
    def sign_link_expiry_period(self, value):
        self._sign_link_expiry_period = value


    def to_alipay_dict(self):
        params = dict()
        if self.expiry_period:
            if hasattr(self.expiry_period, 'to_alipay_dict'):
                params['expiry_period'] = self.expiry_period.to_alipay_dict()
            else:
                params['expiry_period'] = self.expiry_period
        if self.merchant_id_number:
            if hasattr(self.merchant_id_number, 'to_alipay_dict'):
                params['merchant_id_number'] = self.merchant_id_number.to_alipay_dict()
            else:
                params['merchant_id_number'] = self.merchant_id_number
        if self.merchant_id_type:
            if hasattr(self.merchant_id_type, 'to_alipay_dict'):
                params['merchant_id_type'] = self.merchant_id_type.to_alipay_dict()
            else:
                params['merchant_id_type'] = self.merchant_id_type
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.outer_logon_id:
            if hasattr(self.outer_logon_id, 'to_alipay_dict'):
                params['outer_logon_id'] = self.outer_logon_id.to_alipay_dict()
            else:
                params['outer_logon_id'] = self.outer_logon_id
        if self.product_agrt_code:
            if hasattr(self.product_agrt_code, 'to_alipay_dict'):
                params['product_agrt_code'] = self.product_agrt_code.to_alipay_dict()
            else:
                params['product_agrt_code'] = self.product_agrt_code
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.sign_link_expiry_period:
            if hasattr(self.sign_link_expiry_period, 'to_alipay_dict'):
                params['sign_link_expiry_period'] = self.sign_link_expiry_period.to_alipay_dict()
            else:
                params['sign_link_expiry_period'] = self.sign_link_expiry_period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinFwhSignApplyModel()
        if 'expiry_period' in d:
            o.expiry_period = d['expiry_period']
        if 'merchant_id_number' in d:
            o.merchant_id_number = d['merchant_id_number']
        if 'merchant_id_type' in d:
            o.merchant_id_type = d['merchant_id_type']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'outer_logon_id' in d:
            o.outer_logon_id = d['outer_logon_id']
        if 'product_agrt_code' in d:
            o.product_agrt_code = d['product_agrt_code']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'sign_link_expiry_period' in d:
            o.sign_link_expiry_period = d['sign_link_expiry_period']
        return o


