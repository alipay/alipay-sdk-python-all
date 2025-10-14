#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanHonorBudgetQueryModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._budget_type = None
        self._channel_customer_id = None
        self._open_id = None
        self._out_order_no = None
        self._out_trace_id = None
        self._product_code = None
        self._repay_amount = None
        self._request_source = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def budget_type(self):
        return self._budget_type

    @budget_type.setter
    def budget_type(self, value):
        self._budget_type = value
    @property
    def channel_customer_id(self):
        return self._channel_customer_id

    @channel_customer_id.setter
    def channel_customer_id(self, value):
        self._channel_customer_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
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
    def repay_amount(self):
        return self._repay_amount

    @repay_amount.setter
    def repay_amount(self, value):
        self._repay_amount = value
    @property
    def request_source(self):
        return self._request_source

    @request_source.setter
    def request_source(self, value):
        self._request_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.budget_type:
            if hasattr(self.budget_type, 'to_alipay_dict'):
                params['budget_type'] = self.budget_type.to_alipay_dict()
            else:
                params['budget_type'] = self.budget_type
        if self.channel_customer_id:
            if hasattr(self.channel_customer_id, 'to_alipay_dict'):
                params['channel_customer_id'] = self.channel_customer_id.to_alipay_dict()
            else:
                params['channel_customer_id'] = self.channel_customer_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
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
        if self.repay_amount:
            if hasattr(self.repay_amount, 'to_alipay_dict'):
                params['repay_amount'] = self.repay_amount.to_alipay_dict()
            else:
                params['repay_amount'] = self.repay_amount
        if self.request_source:
            if hasattr(self.request_source, 'to_alipay_dict'):
                params['request_source'] = self.request_source.to_alipay_dict()
            else:
                params['request_source'] = self.request_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanHonorBudgetQueryModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'budget_type' in d:
            o.budget_type = d['budget_type']
        if 'channel_customer_id' in d:
            o.channel_customer_id = d['channel_customer_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_trace_id' in d:
            o.out_trace_id = d['out_trace_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'repay_amount' in d:
            o.repay_amount = d['repay_amount']
        if 'request_source' in d:
            o.request_source = d['request_source']
        return o


