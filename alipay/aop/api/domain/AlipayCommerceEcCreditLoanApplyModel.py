#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcCreditLoanApplyModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._credit_channel_code = None
        self._enterprise_id = None
        self._loan_amount = None
        self._out_biz_no = None
        self._remark = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def credit_channel_code(self):
        return self._credit_channel_code

    @credit_channel_code.setter
    def credit_channel_code(self, value):
        self._credit_channel_code = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.credit_channel_code:
            if hasattr(self.credit_channel_code, 'to_alipay_dict'):
                params['credit_channel_code'] = self.credit_channel_code.to_alipay_dict()
            else:
                params['credit_channel_code'] = self.credit_channel_code
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.loan_amount:
            if hasattr(self.loan_amount, 'to_alipay_dict'):
                params['loan_amount'] = self.loan_amount.to_alipay_dict()
            else:
                params['loan_amount'] = self.loan_amount
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcCreditLoanApplyModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'credit_channel_code' in d:
            o.credit_channel_code = d['credit_channel_code']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'loan_amount' in d:
            o.loan_amount = d['loan_amount']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'remark' in d:
            o.remark = d['remark']
        return o


