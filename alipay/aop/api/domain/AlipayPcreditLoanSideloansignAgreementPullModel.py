#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanSideloansignAgreementPullModel(object):

    def __init__(self):
        self._agreement_type = None
        self._alipay_user_id = None
        self._extension = None
        self._fund_supplier_code = None
        self._open_id = None
        self._product_code = None

    @property
    def agreement_type(self):
        return self._agreement_type

    @agreement_type.setter
    def agreement_type(self, value):
        self._agreement_type = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_type:
            if hasattr(self.agreement_type, 'to_alipay_dict'):
                params['agreement_type'] = self.agreement_type.to_alipay_dict()
            else:
                params['agreement_type'] = self.agreement_type
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanSideloansignAgreementPullModel()
        if 'agreement_type' in d:
            o.agreement_type = d['agreement_type']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'extension' in d:
            o.extension = d['extension']
        if 'fund_supplier_code' in d:
            o.fund_supplier_code = d['fund_supplier_code']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


