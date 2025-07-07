#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FreightFlowOppositeAccountInfo(object):

    def __init__(self):
        self._account_cert_no = None
        self._account_cert_type = None
        self._account_customer_type = None
        self._account_inst_code = None
        self._account_no = None
        self._account_type = None

    @property
    def account_cert_no(self):
        return self._account_cert_no

    @account_cert_no.setter
    def account_cert_no(self, value):
        self._account_cert_no = value
    @property
    def account_cert_type(self):
        return self._account_cert_type

    @account_cert_type.setter
    def account_cert_type(self, value):
        self._account_cert_type = value
    @property
    def account_customer_type(self):
        return self._account_customer_type

    @account_customer_type.setter
    def account_customer_type(self, value):
        self._account_customer_type = value
    @property
    def account_inst_code(self):
        return self._account_inst_code

    @account_inst_code.setter
    def account_inst_code(self, value):
        self._account_inst_code = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_cert_no:
            if hasattr(self.account_cert_no, 'to_alipay_dict'):
                params['account_cert_no'] = self.account_cert_no.to_alipay_dict()
            else:
                params['account_cert_no'] = self.account_cert_no
        if self.account_cert_type:
            if hasattr(self.account_cert_type, 'to_alipay_dict'):
                params['account_cert_type'] = self.account_cert_type.to_alipay_dict()
            else:
                params['account_cert_type'] = self.account_cert_type
        if self.account_customer_type:
            if hasattr(self.account_customer_type, 'to_alipay_dict'):
                params['account_customer_type'] = self.account_customer_type.to_alipay_dict()
            else:
                params['account_customer_type'] = self.account_customer_type
        if self.account_inst_code:
            if hasattr(self.account_inst_code, 'to_alipay_dict'):
                params['account_inst_code'] = self.account_inst_code.to_alipay_dict()
            else:
                params['account_inst_code'] = self.account_inst_code
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FreightFlowOppositeAccountInfo()
        if 'account_cert_no' in d:
            o.account_cert_no = d['account_cert_no']
        if 'account_cert_type' in d:
            o.account_cert_type = d['account_cert_type']
        if 'account_customer_type' in d:
            o.account_customer_type = d['account_customer_type']
        if 'account_inst_code' in d:
            o.account_inst_code = d['account_inst_code']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        return o


