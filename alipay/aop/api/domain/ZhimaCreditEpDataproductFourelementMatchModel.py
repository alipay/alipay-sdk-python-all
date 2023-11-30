#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpDataproductFourelementMatchModel(object):

    def __init__(self):
        self._credit_code = None
        self._ent_name = None
        self._fr_cert_no = None
        self._fr_name = None
        self._product_code = None
        self._reg_no = None

    @property
    def credit_code(self):
        return self._credit_code

    @credit_code.setter
    def credit_code(self, value):
        self._credit_code = value
    @property
    def ent_name(self):
        return self._ent_name

    @ent_name.setter
    def ent_name(self, value):
        self._ent_name = value
    @property
    def fr_cert_no(self):
        return self._fr_cert_no

    @fr_cert_no.setter
    def fr_cert_no(self, value):
        self._fr_cert_no = value
    @property
    def fr_name(self):
        return self._fr_name

    @fr_name.setter
    def fr_name(self, value):
        self._fr_name = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.credit_code:
            if hasattr(self.credit_code, 'to_alipay_dict'):
                params['credit_code'] = self.credit_code.to_alipay_dict()
            else:
                params['credit_code'] = self.credit_code
        if self.ent_name:
            if hasattr(self.ent_name, 'to_alipay_dict'):
                params['ent_name'] = self.ent_name.to_alipay_dict()
            else:
                params['ent_name'] = self.ent_name
        if self.fr_cert_no:
            if hasattr(self.fr_cert_no, 'to_alipay_dict'):
                params['fr_cert_no'] = self.fr_cert_no.to_alipay_dict()
            else:
                params['fr_cert_no'] = self.fr_cert_no
        if self.fr_name:
            if hasattr(self.fr_name, 'to_alipay_dict'):
                params['fr_name'] = self.fr_name.to_alipay_dict()
            else:
                params['fr_name'] = self.fr_name
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpDataproductFourelementMatchModel()
        if 'credit_code' in d:
            o.credit_code = d['credit_code']
        if 'ent_name' in d:
            o.ent_name = d['ent_name']
        if 'fr_cert_no' in d:
            o.fr_cert_no = d['fr_cert_no']
        if 'fr_name' in d:
            o.fr_name = d['fr_name']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'reg_no' in d:
            o.reg_no = d['reg_no']
        return o


