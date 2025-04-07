#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasOpenAccountConsultModel(object):

    def __init__(self):
        self._account_name = None
        self._account_no = None
        self._bank_code = None
        self._biller_code = None
        self._country = None
        self._receipt_method = None
        self._school_id = None
        self._swift_code = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def biller_code(self):
        return self._biller_code

    @biller_code.setter
    def biller_code(self, value):
        self._biller_code = value
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
    @property
    def receipt_method(self):
        return self._receipt_method

    @receipt_method.setter
    def receipt_method(self, value):
        self._receipt_method = value
    @property
    def school_id(self):
        return self._school_id

    @school_id.setter
    def school_id(self, value):
        self._school_id = value
    @property
    def swift_code(self):
        return self._swift_code

    @swift_code.setter
    def swift_code(self, value):
        self._swift_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        if self.biller_code:
            if hasattr(self.biller_code, 'to_alipay_dict'):
                params['biller_code'] = self.biller_code.to_alipay_dict()
            else:
                params['biller_code'] = self.biller_code
        if self.country:
            if hasattr(self.country, 'to_alipay_dict'):
                params['country'] = self.country.to_alipay_dict()
            else:
                params['country'] = self.country
        if self.receipt_method:
            if hasattr(self.receipt_method, 'to_alipay_dict'):
                params['receipt_method'] = self.receipt_method.to_alipay_dict()
            else:
                params['receipt_method'] = self.receipt_method
        if self.school_id:
            if hasattr(self.school_id, 'to_alipay_dict'):
                params['school_id'] = self.school_id.to_alipay_dict()
            else:
                params['school_id'] = self.school_id
        if self.swift_code:
            if hasattr(self.swift_code, 'to_alipay_dict'):
                params['swift_code'] = self.swift_code.to_alipay_dict()
            else:
                params['swift_code'] = self.swift_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasOpenAccountConsultModel()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'biller_code' in d:
            o.biller_code = d['biller_code']
        if 'country' in d:
            o.country = d['country']
        if 'receipt_method' in d:
            o.receipt_method = d['receipt_method']
        if 'school_id' in d:
            o.school_id = d['school_id']
        if 'swift_code' in d:
            o.swift_code = d['swift_code']
        return o


