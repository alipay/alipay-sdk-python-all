#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanSideloansignCreditApplyModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._credit_apply_no = None
        self._credit_type = None
        self._customer_id = None
        self._extension = None
        self._fund_supplier_code = None
        self._open_id = None
        self._product_code = None
        self._verify_id = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def credit_apply_no(self):
        return self._credit_apply_no

    @credit_apply_no.setter
    def credit_apply_no(self, value):
        self._credit_apply_no = value
    @property
    def credit_type(self):
        return self._credit_type

    @credit_type.setter
    def credit_type(self, value):
        self._credit_type = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, value):
        self._extension = value
    @property
    def fund_supplier_code(self):
        return self._fund_supplier_code

    @fund_supplier_code.setter
    def fund_supplier_code(self, value):
        self._fund_supplier_code = value
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
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.credit_apply_no:
            if hasattr(self.credit_apply_no, 'to_alipay_dict'):
                params['credit_apply_no'] = self.credit_apply_no.to_alipay_dict()
            else:
                params['credit_apply_no'] = self.credit_apply_no
        if self.credit_type:
            if hasattr(self.credit_type, 'to_alipay_dict'):
                params['credit_type'] = self.credit_type.to_alipay_dict()
            else:
                params['credit_type'] = self.credit_type
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.extension:
            if hasattr(self.extension, 'to_alipay_dict'):
                params['extension'] = self.extension.to_alipay_dict()
            else:
                params['extension'] = self.extension
        if self.fund_supplier_code:
            if hasattr(self.fund_supplier_code, 'to_alipay_dict'):
                params['fund_supplier_code'] = self.fund_supplier_code.to_alipay_dict()
            else:
                params['fund_supplier_code'] = self.fund_supplier_code
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
        if self.verify_id:
            if hasattr(self.verify_id, 'to_alipay_dict'):
                params['verify_id'] = self.verify_id.to_alipay_dict()
            else:
                params['verify_id'] = self.verify_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanSideloansignCreditApplyModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'credit_apply_no' in d:
            o.credit_apply_no = d['credit_apply_no']
        if 'credit_type' in d:
            o.credit_type = d['credit_type']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'extension' in d:
            o.extension = d['extension']
        if 'fund_supplier_code' in d:
            o.fund_supplier_code = d['fund_supplier_code']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'verify_id' in d:
            o.verify_id = d['verify_id']
        return o


