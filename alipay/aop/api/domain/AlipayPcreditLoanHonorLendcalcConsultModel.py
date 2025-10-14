#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanHonorLendcalcConsultModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._bank_contract_id = None
        self._channel_customer_id = None
        self._coupon_no = None
        self._loan_amount = None
        self._need_contract = None
        self._open_id = None
        self._out_trace_id = None
        self._product_code = None
        self._repay_method = None
        self._request_source = None
        self._total_term = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def bank_contract_id(self):
        return self._bank_contract_id

    @bank_contract_id.setter
    def bank_contract_id(self, value):
        self._bank_contract_id = value
    @property
    def channel_customer_id(self):
        return self._channel_customer_id

    @channel_customer_id.setter
    def channel_customer_id(self, value):
        self._channel_customer_id = value
    @property
    def coupon_no(self):
        return self._coupon_no

    @coupon_no.setter
    def coupon_no(self, value):
        self._coupon_no = value
    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def need_contract(self):
        return self._need_contract

    @need_contract.setter
    def need_contract(self, value):
        self._need_contract = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_trace_id(self):
        return self._out_trace_id

    @out_trace_id.setter
    def out_trace_id(self, value):
        self._out_trace_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def repay_method(self):
        return self._repay_method

    @repay_method.setter
    def repay_method(self, value):
        self._repay_method = value
    @property
    def request_source(self):
        return self._request_source

    @request_source.setter
    def request_source(self, value):
        self._request_source = value
    @property
    def total_term(self):
        return self._total_term

    @total_term.setter
    def total_term(self, value):
        self._total_term = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.bank_contract_id:
            if hasattr(self.bank_contract_id, 'to_alipay_dict'):
                params['bank_contract_id'] = self.bank_contract_id.to_alipay_dict()
            else:
                params['bank_contract_id'] = self.bank_contract_id
        if self.channel_customer_id:
            if hasattr(self.channel_customer_id, 'to_alipay_dict'):
                params['channel_customer_id'] = self.channel_customer_id.to_alipay_dict()
            else:
                params['channel_customer_id'] = self.channel_customer_id
        if self.coupon_no:
            if hasattr(self.coupon_no, 'to_alipay_dict'):
                params['coupon_no'] = self.coupon_no.to_alipay_dict()
            else:
                params['coupon_no'] = self.coupon_no
        if self.loan_amount:
            if hasattr(self.loan_amount, 'to_alipay_dict'):
                params['loan_amount'] = self.loan_amount.to_alipay_dict()
            else:
                params['loan_amount'] = self.loan_amount
        if self.need_contract:
            if hasattr(self.need_contract, 'to_alipay_dict'):
                params['need_contract'] = self.need_contract.to_alipay_dict()
            else:
                params['need_contract'] = self.need_contract
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_trace_id:
            if hasattr(self.out_trace_id, 'to_alipay_dict'):
                params['out_trace_id'] = self.out_trace_id.to_alipay_dict()
            else:
                params['out_trace_id'] = self.out_trace_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.repay_method:
            if hasattr(self.repay_method, 'to_alipay_dict'):
                params['repay_method'] = self.repay_method.to_alipay_dict()
            else:
                params['repay_method'] = self.repay_method
        if self.request_source:
            if hasattr(self.request_source, 'to_alipay_dict'):
                params['request_source'] = self.request_source.to_alipay_dict()
            else:
                params['request_source'] = self.request_source
        if self.total_term:
            if hasattr(self.total_term, 'to_alipay_dict'):
                params['total_term'] = self.total_term.to_alipay_dict()
            else:
                params['total_term'] = self.total_term
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanHonorLendcalcConsultModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'bank_contract_id' in d:
            o.bank_contract_id = d['bank_contract_id']
        if 'channel_customer_id' in d:
            o.channel_customer_id = d['channel_customer_id']
        if 'coupon_no' in d:
            o.coupon_no = d['coupon_no']
        if 'loan_amount' in d:
            o.loan_amount = d['loan_amount']
        if 'need_contract' in d:
            o.need_contract = d['need_contract']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_trace_id' in d:
            o.out_trace_id = d['out_trace_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'repay_method' in d:
            o.repay_method = d['repay_method']
        if 'request_source' in d:
            o.request_source = d['request_source']
        if 'total_term' in d:
            o.total_term = d['total_term']
        return o


