#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditScoreBriefGetModel(object):

    def __init__(self):
        self._admittance_score = None
        self._cert_no = None
        self._cert_type = None
        self._linked_merchant_id = None
        self._name = None
        self._open_id = None
        self._product_code = None
        self._transaction_id = None

    @property
    def admittance_score(self):
        return self._admittance_score

    @admittance_score.setter
    def admittance_score(self, value):
        self._admittance_score = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def linked_merchant_id(self):
        return self._linked_merchant_id

    @linked_merchant_id.setter
    def linked_merchant_id(self, value):
        self._linked_merchant_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.admittance_score:
            if hasattr(self.admittance_score, 'to_alipay_dict'):
                params['admittance_score'] = self.admittance_score.to_alipay_dict()
            else:
                params['admittance_score'] = self.admittance_score
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.linked_merchant_id:
            if hasattr(self.linked_merchant_id, 'to_alipay_dict'):
                params['linked_merchant_id'] = self.linked_merchant_id.to_alipay_dict()
            else:
                params['linked_merchant_id'] = self.linked_merchant_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditScoreBriefGetModel()
        if 'admittance_score' in d:
            o.admittance_score = d['admittance_score']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'linked_merchant_id' in d:
            o.linked_merchant_id = d['linked_merchant_id']
        if 'name' in d:
            o.name = d['name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        return o


