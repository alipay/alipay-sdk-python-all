#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpCreditunionPaSubscribeModel(object):

    def __init__(self):
        self._auth_id = None
        self._business_person = None
        self._ent_name = None
        self._merchant_request_id = None
        self._product_code = None
        self._reg_no = None
        self._type = None
        self._uscc = None

    @property
    def auth_id(self):
        return self._auth_id

    @auth_id.setter
    def auth_id(self, value):
        self._auth_id = value
    @property
    def business_person(self):
        return self._business_person

    @business_person.setter
    def business_person(self, value):
        self._business_person = value
    @property
    def ent_name(self):
        return self._ent_name

    @ent_name.setter
    def ent_name(self, value):
        self._ent_name = value
    @property
    def merchant_request_id(self):
        return self._merchant_request_id

    @merchant_request_id.setter
    def merchant_request_id(self, value):
        self._merchant_request_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_id:
            if hasattr(self.auth_id, 'to_alipay_dict'):
                params['auth_id'] = self.auth_id.to_alipay_dict()
            else:
                params['auth_id'] = self.auth_id
        if self.business_person:
            if hasattr(self.business_person, 'to_alipay_dict'):
                params['business_person'] = self.business_person.to_alipay_dict()
            else:
                params['business_person'] = self.business_person
        if self.ent_name:
            if hasattr(self.ent_name, 'to_alipay_dict'):
                params['ent_name'] = self.ent_name.to_alipay_dict()
            else:
                params['ent_name'] = self.ent_name
        if self.merchant_request_id:
            if hasattr(self.merchant_request_id, 'to_alipay_dict'):
                params['merchant_request_id'] = self.merchant_request_id.to_alipay_dict()
            else:
                params['merchant_request_id'] = self.merchant_request_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.reg_no:
            if hasattr(self.reg_no, 'to_alipay_dict'):
                params['reg_no'] = self.reg_no.to_alipay_dict()
            else:
                params['reg_no'] = self.reg_no
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.uscc:
            if hasattr(self.uscc, 'to_alipay_dict'):
                params['uscc'] = self.uscc.to_alipay_dict()
            else:
                params['uscc'] = self.uscc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpCreditunionPaSubscribeModel()
        if 'auth_id' in d:
            o.auth_id = d['auth_id']
        if 'business_person' in d:
            o.business_person = d['business_person']
        if 'ent_name' in d:
            o.ent_name = d['ent_name']
        if 'merchant_request_id' in d:
            o.merchant_request_id = d['merchant_request_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'reg_no' in d:
            o.reg_no = d['reg_no']
        if 'type' in d:
            o.type = d['type']
        if 'uscc' in d:
            o.uscc = d['uscc']
        return o


