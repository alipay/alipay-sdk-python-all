#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanHonorContractdetailQueryModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._channel_customer_id = None
        self._contract_id = None
        self._loan_apply_no = None
        self._open_id = None
        self._out_trace_id = None
        self._pre_consult_id = None
        self._product_code = None
        self._request_source = None
        self._type = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def channel_customer_id(self):
        return self._channel_customer_id

    @channel_customer_id.setter
    def channel_customer_id(self, value):
        self._channel_customer_id = value
    @property
    def contract_id(self):
        return self._contract_id

    @contract_id.setter
    def contract_id(self, value):
        self._contract_id = value
    @property
    def loan_apply_no(self):
        return self._loan_apply_no

    @loan_apply_no.setter
    def loan_apply_no(self, value):
        self._loan_apply_no = value
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
    def pre_consult_id(self):
        return self._pre_consult_id

    @pre_consult_id.setter
    def pre_consult_id(self, value):
        self._pre_consult_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def request_source(self):
        return self._request_source

    @request_source.setter
    def request_source(self, value):
        self._request_source = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.channel_customer_id:
            if hasattr(self.channel_customer_id, 'to_alipay_dict'):
                params['channel_customer_id'] = self.channel_customer_id.to_alipay_dict()
            else:
                params['channel_customer_id'] = self.channel_customer_id
        if self.contract_id:
            if hasattr(self.contract_id, 'to_alipay_dict'):
                params['contract_id'] = self.contract_id.to_alipay_dict()
            else:
                params['contract_id'] = self.contract_id
        if self.loan_apply_no:
            if hasattr(self.loan_apply_no, 'to_alipay_dict'):
                params['loan_apply_no'] = self.loan_apply_no.to_alipay_dict()
            else:
                params['loan_apply_no'] = self.loan_apply_no
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
        if self.pre_consult_id:
            if hasattr(self.pre_consult_id, 'to_alipay_dict'):
                params['pre_consult_id'] = self.pre_consult_id.to_alipay_dict()
            else:
                params['pre_consult_id'] = self.pre_consult_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.request_source:
            if hasattr(self.request_source, 'to_alipay_dict'):
                params['request_source'] = self.request_source.to_alipay_dict()
            else:
                params['request_source'] = self.request_source
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanHonorContractdetailQueryModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'channel_customer_id' in d:
            o.channel_customer_id = d['channel_customer_id']
        if 'contract_id' in d:
            o.contract_id = d['contract_id']
        if 'loan_apply_no' in d:
            o.loan_apply_no = d['loan_apply_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_trace_id' in d:
            o.out_trace_id = d['out_trace_id']
        if 'pre_consult_id' in d:
            o.pre_consult_id = d['pre_consult_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'request_source' in d:
            o.request_source = d['request_source']
        if 'type' in d:
            o.type = d['type']
        return o


